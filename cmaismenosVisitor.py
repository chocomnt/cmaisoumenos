# Generated from cmaismenos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .cmaismenosParser import cmaismenosParser
else:
    from cmaismenosParser import cmaismenosParser

# This class defines a complete generic visitor for a parse tree produced by cmaismenosParser.

class cmaismenosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cmaismenosParser#programa.
    def visitPrograma(self, ctx:cmaismenosParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#comando.
    def visitComando(self, ctx:cmaismenosParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#atribuicao.
    def visitAtribuicao(self, ctx:cmaismenosParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#declaracao.
    def visitDeclaracao(self, ctx:cmaismenosParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#declaracaoInt.
    def visitDeclaracaoInt(self, ctx:cmaismenosParser.DeclaracaoIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#declaracaoStr.
    def visitDeclaracaoStr(self, ctx:cmaismenosParser.DeclaracaoStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#entrada.
    def visitEntrada(self, ctx:cmaismenosParser.EntradaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#saida.
    def visitSaida(self, ctx:cmaismenosParser.SaidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#condicional.
    def visitCondicional(self, ctx:cmaismenosParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#repeticao.
    def visitRepeticao(self, ctx:cmaismenosParser.RepeticaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#bloco.
    def visitBloco(self, ctx:cmaismenosParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#expressao.
    def visitExpressao(self, ctx:cmaismenosParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#termo.
    def visitTermo(self, ctx:cmaismenosParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#fator.
    def visitFator(self, ctx:cmaismenosParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#expressaoLogica.
    def visitExpressaoLogica(self, ctx:cmaismenosParser.ExpressaoLogicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#termoLogico.
    def visitTermoLogico(self, ctx:cmaismenosParser.TermoLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cmaismenosParser#comparacao.
    def visitComparacao(self, ctx:cmaismenosParser.ComparacaoContext):
        return self.visitChildren(ctx)



del cmaismenosParser