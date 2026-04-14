# Generated from cmaismenos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .cmaismenosParser import cmaismenosParser
else:
    from cmaismenosParser import cmaismenosParser

# This class defines a complete listener for a parse tree produced by cmaismenosParser.
class cmaismenosListener(ParseTreeListener):

    # Enter a parse tree produced by cmaismenosParser#programa.
    def enterPrograma(self, ctx:cmaismenosParser.ProgramaContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#programa.
    def exitPrograma(self, ctx:cmaismenosParser.ProgramaContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#comando.
    def enterComando(self, ctx:cmaismenosParser.ComandoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#comando.
    def exitComando(self, ctx:cmaismenosParser.ComandoContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#atribuicao.
    def enterAtribuicao(self, ctx:cmaismenosParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#atribuicao.
    def exitAtribuicao(self, ctx:cmaismenosParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#declaracao.
    def enterDeclaracao(self, ctx:cmaismenosParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#declaracao.
    def exitDeclaracao(self, ctx:cmaismenosParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#declaracaoInt.
    def enterDeclaracaoInt(self, ctx:cmaismenosParser.DeclaracaoIntContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#declaracaoInt.
    def exitDeclaracaoInt(self, ctx:cmaismenosParser.DeclaracaoIntContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#declaracaoStr.
    def enterDeclaracaoStr(self, ctx:cmaismenosParser.DeclaracaoStrContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#declaracaoStr.
    def exitDeclaracaoStr(self, ctx:cmaismenosParser.DeclaracaoStrContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#entrada.
    def enterEntrada(self, ctx:cmaismenosParser.EntradaContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#entrada.
    def exitEntrada(self, ctx:cmaismenosParser.EntradaContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#saida.
    def enterSaida(self, ctx:cmaismenosParser.SaidaContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#saida.
    def exitSaida(self, ctx:cmaismenosParser.SaidaContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#condicional.
    def enterCondicional(self, ctx:cmaismenosParser.CondicionalContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#condicional.
    def exitCondicional(self, ctx:cmaismenosParser.CondicionalContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#repeticao.
    def enterRepeticao(self, ctx:cmaismenosParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#repeticao.
    def exitRepeticao(self, ctx:cmaismenosParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#bloco.
    def enterBloco(self, ctx:cmaismenosParser.BlocoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#bloco.
    def exitBloco(self, ctx:cmaismenosParser.BlocoContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#expressao.
    def enterExpressao(self, ctx:cmaismenosParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#expressao.
    def exitExpressao(self, ctx:cmaismenosParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#termo.
    def enterTermo(self, ctx:cmaismenosParser.TermoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#termo.
    def exitTermo(self, ctx:cmaismenosParser.TermoContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#fator.
    def enterFator(self, ctx:cmaismenosParser.FatorContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#fator.
    def exitFator(self, ctx:cmaismenosParser.FatorContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#expressaoLogica.
    def enterExpressaoLogica(self, ctx:cmaismenosParser.ExpressaoLogicaContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#expressaoLogica.
    def exitExpressaoLogica(self, ctx:cmaismenosParser.ExpressaoLogicaContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#termoLogico.
    def enterTermoLogico(self, ctx:cmaismenosParser.TermoLogicoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#termoLogico.
    def exitTermoLogico(self, ctx:cmaismenosParser.TermoLogicoContext):
        pass


    # Enter a parse tree produced by cmaismenosParser#comparacao.
    def enterComparacao(self, ctx:cmaismenosParser.ComparacaoContext):
        pass

    # Exit a parse tree produced by cmaismenosParser#comparacao.
    def exitComparacao(self, ctx:cmaismenosParser.ComparacaoContext):
        pass



del cmaismenosParser