from dataclasses import dataclass
import logging

from cmaismenosParser import cmaismenosParser
from cmaismenosVisitor import cmaismenosVisitor


INTEIRO = "inteiro"
TEXTO = "texto"
BOOLEANO = "booleano"
DESCONHECIDO = "desconhecido"


@dataclass
class SimboloSemantico:
    nome: str
    tipo: str
    linha: int
    coluna: int


@dataclass
class ErroSemantico:
    codigo: str
    mensagem: str
    linha: int
    coluna: int
    lexema: str
    contexto: str
    sugestao: str

    def formatar(self) -> str:
        return (
            f"{self.codigo} [Linha {self.linha}, Coluna {self.coluna}] "
            f"Lexema: '{self.lexema}' | Contexto: {self.contexto} | "
            f"Mensagem: {self.mensagem} | Sugestão: {self.sugestao}"
        )


class AnalisadorSemantico(cmaismenosVisitor):
    def __init__(self, nome_registrador="semantica"):
        self.escopos = [{}]
        self.erros = []
        self.registrador = logging.getLogger(nome_registrador)

    def analisar(self, arvore):
        self.visit(arvore)
        return self.erros

    def tem_erros(self):
        return len(self.erros) > 0

    def registrar_no_log(self):
        if not self.erros:
            self.registrador.info("Análise semântica concluída sem erros.")
            return

        self.registrador.error("Análise semântica encontrou %d erro(s).", len(self.erros))
        for erro in self.erros:
            self.registrador.error(erro.formatar())

    def _entrar_escopo(self):
        self.escopos.append({})

    def _sair_escopo(self):
        self.escopos.pop()

    def _escopo_atual(self):
        return self.escopos[-1]

    def _buscar(self, nome):
        for escopo in reversed(self.escopos):
            if nome in escopo:
                return escopo[nome]
        return None

    def _declarar(self, token, tipo):
        nome = token.getText()
        if nome in self._escopo_atual():
            anterior = self._escopo_atual()[nome]
            self._adicionar_erro(
                "SEM-002",
                token,
                f"Variável '{nome}' já foi declarada neste escopo.",
                "declaração de variável",
                (
                    f"Use outro nome ou remova a declaração duplicada. "
                    f"A declaração anterior está na linha {anterior.linha}, coluna {anterior.coluna}."
                ),
            )
            return

        self._escopo_atual()[nome] = SimboloSemantico(
            nome=nome,
            tipo=tipo,
            linha=token.symbol.line,
            coluna=token.symbol.column,
        )

    def _adicionar_erro(self, codigo, token_ou_contexto, mensagem, contexto, sugestao):
        token = self._obter_token(token_ou_contexto)
        lexema = token.text if token and token.text is not None else token_ou_contexto.getText()
        linha = token.line if token else 0
        coluna = token.column if token else 0
        erro = ErroSemantico(codigo, mensagem, linha, coluna, lexema, contexto, sugestao)
        self.erros.append(erro)
        print(f"ERRO SEMÂNTICO: {erro.formatar()}")

    def _obter_token(self, token_ou_contexto):
        if hasattr(token_ou_contexto, "symbol"):
            return token_ou_contexto.symbol
        if hasattr(token_ou_contexto, "start"):
            return token_ou_contexto.start
        return None

    def _fator_e_zero_literal(self, fator):
        numero = fator.NUMERO()
        if numero is not None:
            return numero.getText() == "0"
        return self._expressao_e_zero_literal(fator.expressao())

    def _expressao_e_zero_literal(self, expressao):
        if expressao is None or len(expressao.termo()) != 1:
            return False
        return self._termo_e_zero_literal(expressao.termo(0))

    def _termo_e_zero_literal(self, termo):
        if termo is None or len(termo.fator()) != 1:
            return False
        return self._fator_e_zero_literal(termo.fator(0))

    def visitPrograma(self, ctx: cmaismenosParser.ProgramaContext):
        for comando in ctx.comando():
            self.visit(comando)

    def visitBloco(self, ctx: cmaismenosParser.BlocoContext):
        self._entrar_escopo()
        for comando in ctx.comando():
            self.visit(comando)
        self._sair_escopo()

    def visitDeclaracaoInt(self, ctx: cmaismenosParser.DeclaracaoIntContext):
        token_nome = ctx.ID()
        tipo_expressao = self.visit(ctx.expressao())
        if tipo_expressao != INTEIRO and tipo_expressao != DESCONHECIDO:
            self._adicionar_erro(
                "SEM-003",
                token_nome,
                f"Variável inteira '{token_nome.getText()}' recebeu expressão do tipo {tipo_expressao}.",
                "declaração inteira",
                "Inicialize variáveis do tipo 'i' apenas com números ou expressões inteiras.",
            )
        self._declarar(token_nome, INTEIRO)

    def visitDeclaracaoStr(self, ctx: cmaismenosParser.DeclaracaoStrContext):
        self._declarar(ctx.ID(), TEXTO)

    def visitAtribuicao(self, ctx: cmaismenosParser.AtribuicaoContext):
        token_nome = ctx.ID()
        nome = token_nome.getText()
        simbolo = self._buscar(nome)
        tipo_expressao = self.visit(ctx.expressao())

        if simbolo is None:
            self._adicionar_erro(
                "SEM-001",
                token_nome,
                f"Variável '{nome}' usada em atribuição antes de ser declarada.",
                "atribuição",
                f"Declare '{nome}' com 'i' ou 's' antes de atribuir um valor.",
            )
            return

        if tipo_expressao != DESCONHECIDO and simbolo.tipo != tipo_expressao:
            self._adicionar_erro(
                "SEM-003",
                token_nome,
                (
                    f"Variável '{nome}' é do tipo {simbolo.tipo}, "
                    f"mas recebeu expressão do tipo {tipo_expressao}."
                ),
                "atribuição",
                "Atribua um valor compatível com o tipo declarado da variável.",
            )

    def visitEntrada(self, ctx: cmaismenosParser.EntradaContext):
        token_nome = ctx.ID()
        nome = token_nome.getText()
        if self._buscar(nome) is None:
            self._adicionar_erro(
                "SEM-001",
                token_nome,
                f"Variável '{nome}' usada em leitura antes de ser declarada.",
                "entrada de dados",
                f"Declare '{nome}' antes de chamar rd({nome}).",
            )

    def visitSaida(self, ctx: cmaismenosParser.SaidaContext):
        if ctx.STRING():
            return
        self.visit(ctx.expressao())

    def visitCondicional(self, ctx: cmaismenosParser.CondicionalContext):
        for expressao in ctx.expressaoLogica():
            tipo_expressao = self.visit(expressao)
            if tipo_expressao != BOOLEANO and tipo_expressao != DESCONHECIDO:
                self._adicionar_erro(
                    "SEM-004",
                    expressao,
                    "Condição do comando 'if' deve produzir um valor booleano.",
                    "condicional",
                    "Use uma comparação como x == 1, x < 10 ou combine comparações com and/or.",
                )

        for bloco in ctx.bloco():
            self.visit(bloco)

    def visitRepeticao(self, ctx: cmaismenosParser.RepeticaoContext):
        tipo_expressao = self.visit(ctx.expressaoLogica())
        if tipo_expressao != BOOLEANO and tipo_expressao != DESCONHECIDO:
            self._adicionar_erro(
                "SEM-004",
                ctx.expressaoLogica(),
                "Condição do comando 'wl' deve produzir um valor booleano.",
                "repetição",
                "Use uma comparação como x < 10 depois de 'wl'.",
            )
        self.visit(ctx.bloco())

    def visitExpressao(self, ctx: cmaismenosParser.ExpressaoContext):
        tipos_termo = [self.visit(termo) for termo in ctx.termo()]
        if len(tipos_termo) == 1:
            return tipos_termo[0]

        for tipo_termo in tipos_termo:
            if tipo_termo != INTEIRO and tipo_termo != DESCONHECIDO:
                self._adicionar_erro(
                    "SEM-005",
                    ctx,
                    "Operadores '+' e '-' só podem ser usados com inteiros.",
                    "expressão aritmética",
                    "Remova strings da expressão ou use apenas variáveis inteiras.",
                )
                return DESCONHECIDO
        return INTEIRO

    def visitTermo(self, ctx: cmaismenosParser.TermoContext):
        fatores = ctx.fator()
        tipos_fator = [self.visit(fator) for fator in fatores]
        if len(tipos_fator) == 1:
            return tipos_fator[0]

        for indice, filho in enumerate(ctx.children[:-1]):
            if filho.getText() == "/":
                divisor = ctx.children[indice + 1]
                if isinstance(divisor, cmaismenosParser.FatorContext) and self._fator_e_zero_literal(divisor):
                    self._adicionar_erro(
                        "SEM-007",
                        divisor,
                        "Divisão por zero não é permitida.",
                        "termo aritmético",
                        "Use um divisor diferente de zero.",
                    )

        for tipo_fator in tipos_fator:
            if tipo_fator != INTEIRO and tipo_fator != DESCONHECIDO:
                self._adicionar_erro(
                    "SEM-005",
                    ctx,
                    "Operadores '*' e '/' só podem ser usados com inteiros.",
                    "termo aritmético",
                    "Use multiplicação e divisão apenas com números ou variáveis inteiras.",
                )
                return DESCONHECIDO
        return INTEIRO

    def visitFator(self, ctx: cmaismenosParser.FatorContext):
        if ctx.NUMERO():
            return INTEIRO

        if ctx.ID():
            token_nome = ctx.ID()
            nome = token_nome.getText()
            simbolo = self._buscar(nome)
            if simbolo is None:
                self._adicionar_erro(
                    "SEM-001",
                    token_nome,
                    f"Variável '{nome}' usada antes de ser declarada.",
                    "uso de variável",
                    f"Declare '{nome}' antes de usar esse identificador em uma expressão.",
                )
                return DESCONHECIDO
            return simbolo.tipo

        return self.visit(ctx.expressao())

    def visitExpressaoLogica(self, ctx: cmaismenosParser.ExpressaoLogicaContext):
        for termo in ctx.termoLogico():
            tipo_termo = self.visit(termo)
            if tipo_termo != BOOLEANO and tipo_termo != DESCONHECIDO:
                self._adicionar_erro(
                    "SEM-004",
                    termo,
                    "Operadores lógicos 'and' e 'or' exigem expressões booleanas.",
                    "expressão lógica",
                    "Combine apenas comparações ou expressões lógicas entre parênteses.",
                )
                return DESCONHECIDO
        return BOOLEANO

    def visitTermoLogico(self, ctx: cmaismenosParser.TermoLogicoContext):
        if ctx.comparacao():
            tipo_resultado = self.visit(ctx.comparacao())
        else:
            tipo_resultado = self.visit(ctx.expressaoLogica())

        if ctx.NOT() and tipo_resultado != BOOLEANO and tipo_resultado != DESCONHECIDO:
            self._adicionar_erro(
                "SEM-004",
                ctx,
                "Operador '!' só pode negar uma expressão booleana.",
                "negação lógica",
                "Use '!' antes de uma comparação ou expressão lógica entre parênteses.",
            )
            return DESCONHECIDO

        return tipo_resultado

    def visitComparacao(self, ctx: cmaismenosParser.ComparacaoContext):
        tipo_esquerda = self.visit(ctx.expressao(0))
        tipo_direita = self.visit(ctx.expressao(1))
        operador = ctx.getChild(1).getText()

        if DESCONHECIDO in (tipo_esquerda, tipo_direita):
            return DESCONHECIDO

        if operador == "==" and tipo_esquerda != tipo_direita:
            self._adicionar_erro(
                "SEM-006",
                ctx,
                (
                    "Comparação '==' recebeu valores de tipos diferentes: "
                    f"{tipo_esquerda} e {tipo_direita}."
                ),
                "comparação",
                "Compare valores do mesmo tipo.",
            )
            return DESCONHECIDO

        if operador in ("<", ">") and (tipo_esquerda != INTEIRO or tipo_direita != INTEIRO):
            self._adicionar_erro(
                "SEM-006",
                ctx,
                f"Comparação '{operador}' só pode ser usada com inteiros.",
                "comparação",
                "Use '<' e '>' apenas entre números ou variáveis inteiras.",
            )
            return DESCONHECIDO

        return BOOLEANO
