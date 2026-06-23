from cmaismenosVisitor import cmaismenosVisitor
from cmaismenosParser import cmaismenosParser


class GeradorPython(cmaismenosVisitor):
    def __init__(self):
        self.linhas = []
        self.indentacao = 0
        self.tipos = {}

    def gerar(self, arvore):
        self.visit(arvore)
        return "\n".join(self.linhas) + "\n"

    def _emitir(self, linha):
        self.linhas.append("    " * self.indentacao + linha)

    def visitPrograma(self, ctx: cmaismenosParser.ProgramaContext):
        for comando in ctx.comando():
            self.visit(comando)

    def visitDeclaracaoInt(self, ctx: cmaismenosParser.DeclaracaoIntContext):
        nome = ctx.ID().getText()
        self.tipos[nome] = "int"
        valor = self.visit(ctx.expressao())
        self._emitir(f"{nome} = {valor}")

    def visitDeclaracaoStr(self, ctx: cmaismenosParser.DeclaracaoStrContext):
        nome = ctx.ID().getText()
        self.tipos[nome] = "str"
        valor = ctx.STRING().getText()
        self._emitir(f"{nome} = {valor}")

    def visitAtribuicao(self, ctx: cmaismenosParser.AtribuicaoContext):
        nome = ctx.ID().getText()
        valor = self.visit(ctx.expressao())
        self._emitir(f"{nome} = {valor}")

    def visitEntrada(self, ctx: cmaismenosParser.EntradaContext):
        nome = ctx.ID().getText()
        if self.tipos.get(nome) == "int":
            self._emitir(f"{nome} = int(input())")
        else:
            self._emitir(f"{nome} = input()")

    def visitSaida(self, ctx: cmaismenosParser.SaidaContext):
        if ctx.STRING():
            self._emitir(f"print({ctx.STRING().getText()})")
        else:
            valor = self.visit(ctx.expressao())
            self._emitir(f"print({valor})")

    def visitCondicional(self, ctx: cmaismenosParser.CondicionalContext):
        filhos = list(ctx.children)
        condicao_if = self.visit(filhos[1])
        self._emitir(f"if {condicao_if}:")
        self.indentacao += 1
        self.visit(filhos[2])
        self.indentacao -= 1

        indice = 3
        if indice < len(filhos) and hasattr(filhos[indice], 'getText') and filhos[indice].getText() == 'el':
            self._emitir("else:")
            self.indentacao += 1
            self.visit(filhos[indice + 1])
            self.indentacao -= 1
            indice += 2

        while indice < len(filhos):
            if hasattr(filhos[indice], 'getText') and filhos[indice].getText() == 'ei':
                condicao_elif = self.visit(filhos[indice + 1])
                self._emitir(f"elif {condicao_elif}:")
                self.indentacao += 1
                self.visit(filhos[indice + 2])
                self.indentacao -= 1
                indice += 3
            else:
                indice += 1

    def visitRepeticao(self, ctx: cmaismenosParser.RepeticaoContext):
        condicao = self.visit(ctx.expressaoLogica())
        self._emitir(f"while {condicao}:")
        self.indentacao += 1
        self.visit(ctx.bloco())
        self.indentacao -= 1

    def visitBloco(self, ctx: cmaismenosParser.BlocoContext):
        for comando in ctx.comando():
            self.visit(comando)

    def visitExpressao(self, ctx: cmaismenosParser.ExpressaoContext):
        resultado = self.visit(ctx.termo(0))
        for i in range(1, len(ctx.termo())):
            op = ctx.getChild(2 * i - 1).getText()
            direita = self.visit(ctx.termo(i))
            resultado = f"{resultado} {op} {direita}"
        return resultado

    def visitTermo(self, ctx: cmaismenosParser.TermoContext):
        resultado = self.visit(ctx.fator(0))
        for i in range(1, len(ctx.fator())):
            op = ctx.getChild(2 * i - 1).getText()
            direita = self.visit(ctx.fator(i))
            if op == "/":
                resultado = f"{resultado} // {direita}"
            else:
                resultado = f"{resultado} {op} {direita}"
        return resultado

    def visitFator(self, ctx: cmaismenosParser.FatorContext):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        if ctx.ID():
            return ctx.ID().getText()
        return f"({self.visit(ctx.expressao())})"

    def visitExpressaoLogica(self, ctx: cmaismenosParser.ExpressaoLogicaContext):
        resultado = self.visit(ctx.termoLogico(0))
        for i in range(1, len(ctx.termoLogico())):
            op = ctx.getChild(2 * i - 1).getText()
            direita = self.visit(ctx.termoLogico(i))
            resultado = f"{resultado} {op} {direita}"
        return resultado

    def visitTermoLogico(self, ctx: cmaismenosParser.TermoLogicoContext):
        if ctx.comparacao():
            resultado = self.visit(ctx.comparacao())
        else:
            resultado = self.visit(ctx.expressaoLogica())
        if ctx.NOT():
            return f"not {resultado}"
        return resultado

    def visitComparacao(self, ctx: cmaismenosParser.ComparacaoContext):
        esquerda = self.visit(ctx.expressao(0))
        operador = ctx.getChild(1).getText()
        direita = self.visit(ctx.expressao(1))
        return f"{esquerda} {operador} {direita}"
