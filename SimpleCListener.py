# Generated from SimpleC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete listener for a parse tree produced by SimpleCParser.
class SimpleCListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleCParser#programa.
    def enterPrograma(self, ctx:SimpleCParser.ProgramaContext):
        pass

    # Exit a parse tree produced by SimpleCParser#programa.
    def exitPrograma(self, ctx:SimpleCParser.ProgramaContext):
        pass


    # Enter a parse tree produced by SimpleCParser#comando.
    def enterComando(self, ctx:SimpleCParser.ComandoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#comando.
    def exitComando(self, ctx:SimpleCParser.ComandoContext):
        pass


    # Enter a parse tree produced by SimpleCParser#atribuicao.
    def enterAtribuicao(self, ctx:SimpleCParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#atribuicao.
    def exitAtribuicao(self, ctx:SimpleCParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declaracao.
    def enterDeclaracao(self, ctx:SimpleCParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declaracao.
    def exitDeclaracao(self, ctx:SimpleCParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declaracaoInt.
    def enterDeclaracaoInt(self, ctx:SimpleCParser.DeclaracaoIntContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declaracaoInt.
    def exitDeclaracaoInt(self, ctx:SimpleCParser.DeclaracaoIntContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declaracaoStr.
    def enterDeclaracaoStr(self, ctx:SimpleCParser.DeclaracaoStrContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declaracaoStr.
    def exitDeclaracaoStr(self, ctx:SimpleCParser.DeclaracaoStrContext):
        pass


    # Enter a parse tree produced by SimpleCParser#entrada.
    def enterEntrada(self, ctx:SimpleCParser.EntradaContext):
        pass

    # Exit a parse tree produced by SimpleCParser#entrada.
    def exitEntrada(self, ctx:SimpleCParser.EntradaContext):
        pass


    # Enter a parse tree produced by SimpleCParser#saida.
    def enterSaida(self, ctx:SimpleCParser.SaidaContext):
        pass

    # Exit a parse tree produced by SimpleCParser#saida.
    def exitSaida(self, ctx:SimpleCParser.SaidaContext):
        pass


    # Enter a parse tree produced by SimpleCParser#condicional.
    def enterCondicional(self, ctx:SimpleCParser.CondicionalContext):
        pass

    # Exit a parse tree produced by SimpleCParser#condicional.
    def exitCondicional(self, ctx:SimpleCParser.CondicionalContext):
        pass


    # Enter a parse tree produced by SimpleCParser#repeticao.
    def enterRepeticao(self, ctx:SimpleCParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#repeticao.
    def exitRepeticao(self, ctx:SimpleCParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by SimpleCParser#bloco.
    def enterBloco(self, ctx:SimpleCParser.BlocoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#bloco.
    def exitBloco(self, ctx:SimpleCParser.BlocoContext):
        pass


    # Enter a parse tree produced by SimpleCParser#expressao.
    def enterExpressao(self, ctx:SimpleCParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#expressao.
    def exitExpressao(self, ctx:SimpleCParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by SimpleCParser#termo.
    def enterTermo(self, ctx:SimpleCParser.TermoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#termo.
    def exitTermo(self, ctx:SimpleCParser.TermoContext):
        pass


    # Enter a parse tree produced by SimpleCParser#fator.
    def enterFator(self, ctx:SimpleCParser.FatorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#fator.
    def exitFator(self, ctx:SimpleCParser.FatorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#expressaoLogica.
    def enterExpressaoLogica(self, ctx:SimpleCParser.ExpressaoLogicaContext):
        pass

    # Exit a parse tree produced by SimpleCParser#expressaoLogica.
    def exitExpressaoLogica(self, ctx:SimpleCParser.ExpressaoLogicaContext):
        pass


    # Enter a parse tree produced by SimpleCParser#termoLogico.
    def enterTermoLogico(self, ctx:SimpleCParser.TermoLogicoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#termoLogico.
    def exitTermoLogico(self, ctx:SimpleCParser.TermoLogicoContext):
        pass


    # Enter a parse tree produced by SimpleCParser#comparacao.
    def enterComparacao(self, ctx:SimpleCParser.ComparacaoContext):
        pass

    # Exit a parse tree produced by SimpleCParser#comparacao.
    def exitComparacao(self, ctx:SimpleCParser.ComparacaoContext):
        pass



del SimpleCParser