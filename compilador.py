import argparse
import logging
import sys

from antlr4 import CommonTokenStream, FileStream, Token
from antlr4.error.ErrorListener import ErrorListener

from cmaismenosLexer import cmaismenosLexer
from cmaismenosParser import cmaismenosParser
from interpretador import Interpretador
from semantica import AnalisadorSemantico


class InterfaceArgumentos(argparse.ArgumentParser):
    def format_usage(self):
        return super().format_usage().replace("usage:", "uso:")

    def format_help(self):
        return super().format_help().replace("usage:", "uso:")

    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, f"{self.prog}: erro: {_traduzir_mensagem_sintatica(message)}\n")


class OuvinteDeErros(ErrorListener):
    def __init__(self):
        super().__init__()
        self.erros = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        palavras_reservadas = ["i", "s", "rd", "pt", "if", "el", "ei", "do", "wl", "and", "or", "!"]
        lexema = offendingSymbol.text if offendingSymbol is not None else ""

        if ("expecting ID" in msg or "missing ID" in msg) and lexema in palavras_reservadas:
            tipo_erro = "ERRO SINTÁTICO"
            mensagem = f"A palavra '{lexema}' é reservada da linguagem e não pode ser usada como nome de variável."
        elif "token recognition error" in msg:
            tipo_erro = "ERRO LÉXICO"
            mensagem = _traduzir_mensagem_lexica(msg)
        elif "extraneous input" in msg:
            tipo_erro = "ERRO SINTÁTICO"
            mensagem = _traduzir_mensagem_sintatica(msg)
        else:
            tipo_erro = "ERRO SINTÁTICO"
            mensagem = _traduzir_mensagem_sintatica(msg)

        erro = f"{tipo_erro} [Linha {line}, Coluna {column}] Lexema: '{lexema}' | Mensagem: {mensagem}"
        self.erros.append(erro)
        print(erro)
        logging.error(erro)

    def tem_erros(self):
        return len(self.erros) > 0


def _traduzir_mensagem_lexica(mensagem):
    if "token recognition error at:" in mensagem:
        trecho = mensagem.split("token recognition error at:", 1)[1].strip()
        return f"Token não reconhecido pelo analisador léxico: {trecho}."
    return mensagem


def _traduzir_mensagem_sintatica(mensagem):
    traducoes = {
        "missing": "faltando",
        "mismatched input": "entrada incompatível",
        "expecting": "esperado",
        "extraneous input": "entrada inesperada",
        "no viable alternative at input": "nenhuma alternativa válida para a entrada",
    }
    mensagem_traduzida = mensagem
    for original, traduzido in traducoes.items():
        mensagem_traduzida = mensagem_traduzida.replace(original, traduzido)
    return mensagem_traduzida


def configurar_log(caminho_log):
    logging.basicConfig(
        filename=caminho_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )


def gerar_arvore_dot(arvore, nome_arquivo="arvore.dot"):
    def texto_do_no(no):
        if hasattr(no, "getText"):
            return no.getText()
        return str(no)

    def escapar_rotulo(texto):
        return texto.replace("\\", "\\\\").replace('"', '\\"')

    def percorrer_arvore(no, id_pai, contador):
        id_no = f"no{contador[0]}"
        contador[0] += 1
        rotulo = escapar_rotulo(texto_do_no(no))
        linhas_dot.append(f'  {id_no} [label="{rotulo}"];')

        if id_pai:
            linhas_dot.append(f"  {id_pai} -> {id_no};")

        if hasattr(no, "children") and no.children:
            for filho in no.children:
                percorrer_arvore(filho, id_no, contador)

    linhas_dot = ["digraph ArvoreSintatica {", "  node [shape=box];"]
    percorrer_arvore(arvore, None, [0])
    linhas_dot.append("}")

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(linhas_dot))

    print(f"Árvore sintática gerada em {nome_arquivo}")


def criar_analisadores(caminho_fonte):
    fluxo = FileStream(caminho_fonte, encoding="utf-8")
    analisador_lexico = cmaismenosLexer(fluxo)

    erros_lexicos = OuvinteDeErros()
    analisador_lexico.removeErrorListeners()
    analisador_lexico.addErrorListener(erros_lexicos)

    tokens = CommonTokenStream(analisador_lexico)
    tokens.fill()

    for token in tokens.tokens:
        if token.type != Token.EOF:
            tipo_token = (
                analisador_lexico.symbolicNames[token.type]
                if token.type < len(analisador_lexico.symbolicNames)
                else str(token.type)
            )
            logging.info("Token: <%s, '%s', %s, %s>", tipo_token, token.text, token.line, token.column)

    analisador_sintatico = cmaismenosParser(tokens)
    erros_sintaticos = OuvinteDeErros()
    analisador_sintatico.removeErrorListeners()
    analisador_sintatico.addErrorListener(erros_sintaticos)

    return analisador_sintatico, erros_lexicos, erros_sintaticos


def compilar(argumentos):
    configurar_log(argumentos.log)
    print("============ COMPILADOR CMAISMENOS ================")
    print(f"Arquivo fonte: {argumentos.arquivo}")
    print(f"Arquivo de log: {argumentos.log}")

    logging.info("Iniciando compilação do arquivo %s.", argumentos.arquivo)
    analisador_sintatico, erros_lexicos, erros_sintaticos = criar_analisadores(argumentos.arquivo)

    print("\n============ ANÁLISE SINTÁTICA ================")
    logging.info("Iniciando análise sintática.")
    arvore = analisador_sintatico.programa()
    logging.info("Análise sintática concluída.")

    if (
        erros_lexicos.tem_erros()
        or erros_sintaticos.tem_erros()
        or analisador_sintatico.getNumberOfSyntaxErrors() > 0
    ):
        print("\nErro: análise léxica ou sintática falhou. Corrija o código e tente novamente.")
        return 1

    print("Análise léxica e sintática concluída sem erros.")

    print("\n============ ANÁLISE SEMÂNTICA ================")
    logging.info("Iniciando análise semântica.")
    analisador_semantico = AnalisadorSemantico()
    erros_semanticos = analisador_semantico.analisar(arvore)
    analisador_semantico.registrar_no_log()
    logging.info("Análise semântica concluída.")

    if erros_semanticos:
        print(f"\nErro: análise semântica encontrou {len(erros_semanticos)} falha(s).")
        print(f"Consulte {argumentos.log} para ver o log detalhado dos erros.")
        return 1

    print("Análise semântica concluída sem erros.")

    if argumentos.mostrar_arvore:
        print("\n============ ÁRVORE SINTÁTICA ================")
        print(arvore.toStringTree(recog=analisador_sintatico))

    if not argumentos.sem_arvore_dot:
        gerar_arvore_dot(arvore, argumentos.arvore_dot)

    if argumentos.somente_analisar:
        print("\nCompilação encerrada após as análises solicitadas.")
        return 0

    print("\n============ EXECUÇÃO ================")
    interpretador = Interpretador()
    interpretador.visit(arvore)
    print("======================================")
    return 0


def criar_interface():
    interface = InterfaceArgumentos(
        prog="compilador.py",
        description="Interface de linha de comando do compilador da linguagem cmaismenos.",
        add_help=False,
    )
    interface._positionals.title = "argumentos"
    interface._optionals.title = "opções"
    interface.add_argument(
        "-h",
        "--ajuda",
        action="help",
        default=argparse.SUPPRESS,
        help="mostra esta mensagem de ajuda e encerra",
    )
    interface.add_argument(
        "arquivo",
        nargs="?",
        default="entrada.cmm",
        help="arquivo fonte .cmm que será analisado e executado; padrão: entrada.cmm",
    )
    interface.add_argument(
        "--somente-analisar",
        action="store_true",
        help="executa as análises léxica, sintática e semântica sem rodar o interpretador",
    )
    interface.add_argument(
        "--mostrar-arvore",
        action="store_true",
        help="mostra a árvore sintática textual no terminal",
    )
    interface.add_argument(
        "--sem-arvore-dot",
        action="store_true",
        help="não gera o arquivo DOT da árvore sintática",
    )
    interface.add_argument(
        "--arvore-dot",
        default="arvore.dot",
        help="nome do arquivo DOT gerado; padrão: arvore.dot",
    )
    interface.add_argument(
        "--log",
        default="compilador.log",
        help="nome do arquivo de log; padrão: compilador.log",
    )
    return interface


def main():
    interface = criar_interface()
    argumentos = interface.parse_args()
    return compilar(argumentos)


if __name__ == "__main__":
    sys.exit(main())
