# Generated from SimpleC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,3,3,58,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,82,8,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,3,8,92,8,8,1,8,1,8,1,8,1,8,5,8,98,8,8,10,8,12,8,
        101,9,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,5,10,110,8,10,10,10,12,10,
        113,9,10,1,10,1,10,1,11,1,11,1,11,5,11,120,8,11,10,11,12,11,123,
        9,11,1,12,1,12,1,12,5,12,128,8,12,10,12,12,12,131,9,12,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,139,8,13,1,14,1,14,1,14,5,14,144,8,14,10,
        14,12,14,147,9,14,1,15,3,15,150,8,15,1,15,1,15,1,15,1,15,1,15,3,
        15,157,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,167,8,16,
        1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,3,1,
        0,5,6,1,0,7,8,1,0,21,22,170,0,37,1,0,0,0,2,48,1,0,0,0,4,50,1,0,0,
        0,6,57,1,0,0,0,8,59,1,0,0,0,10,65,1,0,0,0,12,71,1,0,0,0,14,77,1,
        0,0,0,16,86,1,0,0,0,18,102,1,0,0,0,20,107,1,0,0,0,22,116,1,0,0,0,
        24,124,1,0,0,0,26,138,1,0,0,0,28,140,1,0,0,0,30,149,1,0,0,0,32,166,
        1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,
        37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,0,0,1,41,1,1,0,
        0,0,42,49,3,6,3,0,43,49,3,12,6,0,44,49,3,14,7,0,45,49,3,16,8,0,46,
        49,3,18,9,0,47,49,3,4,2,0,48,42,1,0,0,0,48,43,1,0,0,0,48,44,1,0,
        0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,3,1,0,0,0,50,51,
        5,26,0,0,51,52,5,4,0,0,52,53,3,22,11,0,53,54,5,9,0,0,54,5,1,0,0,
        0,55,58,3,8,4,0,56,58,3,10,5,0,57,55,1,0,0,0,57,56,1,0,0,0,58,7,
        1,0,0,0,59,60,5,1,0,0,60,61,5,26,0,0,61,62,5,4,0,0,62,63,3,22,11,
        0,63,64,5,9,0,0,64,9,1,0,0,0,65,66,5,2,0,0,66,67,5,26,0,0,67,68,
        5,4,0,0,68,69,5,25,0,0,69,70,5,9,0,0,70,11,1,0,0,0,71,72,5,14,0,
        0,72,73,5,10,0,0,73,74,5,26,0,0,74,75,5,11,0,0,75,76,5,9,0,0,76,
        13,1,0,0,0,77,78,5,15,0,0,78,81,5,10,0,0,79,82,3,22,11,0,80,82,5,
        25,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,83,1,0,0,0,83,84,5,11,0,0,
        84,85,5,9,0,0,85,15,1,0,0,0,86,87,5,16,0,0,87,88,3,28,14,0,88,91,
        3,20,10,0,89,90,5,17,0,0,90,92,3,20,10,0,91,89,1,0,0,0,91,92,1,0,
        0,0,92,99,1,0,0,0,93,94,5,18,0,0,94,95,3,28,14,0,95,96,3,20,10,0,
        96,98,1,0,0,0,97,93,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,
        1,0,0,0,100,17,1,0,0,0,101,99,1,0,0,0,102,103,5,20,0,0,103,104,3,
        28,14,0,104,105,5,19,0,0,105,106,3,20,10,0,106,19,1,0,0,0,107,111,
        5,12,0,0,108,110,3,2,1,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,
        1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,115,
        5,13,0,0,115,21,1,0,0,0,116,121,3,24,12,0,117,118,7,0,0,0,118,120,
        3,24,12,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,
        1,0,0,0,122,23,1,0,0,0,123,121,1,0,0,0,124,129,3,26,13,0,125,126,
        7,1,0,0,126,128,3,26,13,0,127,125,1,0,0,0,128,131,1,0,0,0,129,127,
        1,0,0,0,129,130,1,0,0,0,130,25,1,0,0,0,131,129,1,0,0,0,132,139,5,
        27,0,0,133,139,5,26,0,0,134,135,5,10,0,0,135,136,3,22,11,0,136,137,
        5,11,0,0,137,139,1,0,0,0,138,132,1,0,0,0,138,133,1,0,0,0,138,134,
        1,0,0,0,139,27,1,0,0,0,140,145,3,30,15,0,141,142,7,2,0,0,142,144,
        3,30,15,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,
        1,0,0,0,146,29,1,0,0,0,147,145,1,0,0,0,148,150,5,23,0,0,149,148,
        1,0,0,0,149,150,1,0,0,0,150,156,1,0,0,0,151,157,3,32,16,0,152,153,
        5,10,0,0,153,154,3,28,14,0,154,155,5,11,0,0,155,157,1,0,0,0,156,
        151,1,0,0,0,156,152,1,0,0,0,157,31,1,0,0,0,158,159,3,22,11,0,159,
        160,5,3,0,0,160,161,3,22,11,0,161,167,1,0,0,0,162,163,3,22,11,0,
        163,164,5,24,0,0,164,165,3,22,11,0,165,167,1,0,0,0,166,158,1,0,0,
        0,166,162,1,0,0,0,167,33,1,0,0,0,14,37,48,57,81,91,99,111,121,129,
        138,145,149,156,166
    ]

class SimpleCParser ( Parser ):

    grammarFileName = "SimpleC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'i'", "'s'", "'=='", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "';'", "'('", "')'", "'{'", "'}'", "'rd'", 
                     "'pt'", "'if'", "'el'", "'ei'", "'do'", "'wl'", "'and'", 
                     "'or'", "'!'", "'<'" ]

    symbolicNames = [ "<INVALID>", "TIPO_INT", "TIPO_STR", "IGUAL", "ATRIBUICAO", 
                      "SOMA", "SUBTRACAO", "MULTIPLICACAO", "DIVISAO", "PONTO_VIRGULA", 
                      "ABRE_PARENTESES", "FECHA_PARENTESES", "ABRE_CHAVES", 
                      "FECHA_CHAVES", "RD", "PT", "IF", "EL", "EI", "DO", 
                      "WL", "AND", "OR", "NOT", "MENOR", "STRING", "ID", 
                      "NUMERO", "ESPACO" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_atribuicao = 2
    RULE_declaracao = 3
    RULE_declaracaoInt = 4
    RULE_declaracaoStr = 5
    RULE_entrada = 6
    RULE_saida = 7
    RULE_condicional = 8
    RULE_repeticao = 9
    RULE_bloco = 10
    RULE_expressao = 11
    RULE_termo = 12
    RULE_fator = 13
    RULE_expressaoLogica = 14
    RULE_termoLogico = 15
    RULE_comparacao = 16

    ruleNames =  [ "programa", "comando", "atribuicao", "declaracao", "declaracaoInt", 
                   "declaracaoStr", "entrada", "saida", "condicional", "repeticao", 
                   "bloco", "expressao", "termo", "fator", "expressaoLogica", 
                   "termoLogico", "comparacao" ]

    EOF = Token.EOF
    TIPO_INT=1
    TIPO_STR=2
    IGUAL=3
    ATRIBUICAO=4
    SOMA=5
    SUBTRACAO=6
    MULTIPLICACAO=7
    DIVISAO=8
    PONTO_VIRGULA=9
    ABRE_PARENTESES=10
    FECHA_PARENTESES=11
    ABRE_CHAVES=12
    FECHA_CHAVES=13
    RD=14
    PT=15
    IF=16
    EL=17
    EI=18
    DO=19
    WL=20
    AND=21
    OR=22
    NOT=23
    MENOR=24
    STRING=25
    ID=26
    NUMERO=27
    ESPACO=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SimpleCParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.ComandoContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.ComandoContext,i)


        def getRuleIndex(self):
            return SimpleCParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = SimpleCParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68272134) != 0):
                self.state = 34
                self.comando()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(SimpleCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self):
            return self.getTypedRuleContext(SimpleCParser.DeclaracaoContext,0)


        def entrada(self):
            return self.getTypedRuleContext(SimpleCParser.EntradaContext,0)


        def saida(self):
            return self.getTypedRuleContext(SimpleCParser.SaidaContext,0)


        def condicional(self):
            return self.getTypedRuleContext(SimpleCParser.CondicionalContext,0)


        def repeticao(self):
            return self.getTypedRuleContext(SimpleCParser.RepeticaoContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(SimpleCParser.AtribuicaoContext,0)


        def getRuleIndex(self):
            return SimpleCParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = SimpleCParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.declaracao()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.entrada()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.saida()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.condicional()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.repeticao()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.atribuicao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleCParser.ID, 0)

        def ATRIBUICAO(self):
            return self.getToken(SimpleCParser.ATRIBUICAO, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleCParser.ExpressaoContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(SimpleCParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = SimpleCParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(SimpleCParser.ID)
            self.state = 51
            self.match(SimpleCParser.ATRIBUICAO)
            self.state = 52
            self.expressao()
            self.state = 53
            self.match(SimpleCParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracaoInt(self):
            return self.getTypedRuleContext(SimpleCParser.DeclaracaoIntContext,0)


        def declaracaoStr(self):
            return self.getTypedRuleContext(SimpleCParser.DeclaracaoStrContext,0)


        def getRuleIndex(self):
            return SimpleCParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)




    def declaracao(self):

        localctx = SimpleCParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.declaracaoInt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.declaracaoStr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoIntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_INT(self):
            return self.getToken(SimpleCParser.TIPO_INT, 0)

        def ID(self):
            return self.getToken(SimpleCParser.ID, 0)

        def ATRIBUICAO(self):
            return self.getToken(SimpleCParser.ATRIBUICAO, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleCParser.ExpressaoContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(SimpleCParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_declaracaoInt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoInt" ):
                listener.enterDeclaracaoInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoInt" ):
                listener.exitDeclaracaoInt(self)




    def declaracaoInt(self):

        localctx = SimpleCParser.DeclaracaoIntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracaoInt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(SimpleCParser.TIPO_INT)
            self.state = 60
            self.match(SimpleCParser.ID)
            self.state = 61
            self.match(SimpleCParser.ATRIBUICAO)
            self.state = 62
            self.expressao()
            self.state = 63
            self.match(SimpleCParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoStrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_STR(self):
            return self.getToken(SimpleCParser.TIPO_STR, 0)

        def ID(self):
            return self.getToken(SimpleCParser.ID, 0)

        def ATRIBUICAO(self):
            return self.getToken(SimpleCParser.ATRIBUICAO, 0)

        def STRING(self):
            return self.getToken(SimpleCParser.STRING, 0)

        def PONTO_VIRGULA(self):
            return self.getToken(SimpleCParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_declaracaoStr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoStr" ):
                listener.enterDeclaracaoStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoStr" ):
                listener.exitDeclaracaoStr(self)




    def declaracaoStr(self):

        localctx = SimpleCParser.DeclaracaoStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracaoStr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(SimpleCParser.TIPO_STR)
            self.state = 66
            self.match(SimpleCParser.ID)
            self.state = 67
            self.match(SimpleCParser.ATRIBUICAO)
            self.state = 68
            self.match(SimpleCParser.STRING)
            self.state = 69
            self.match(SimpleCParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RD(self):
            return self.getToken(SimpleCParser.RD, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(SimpleCParser.ABRE_PARENTESES, 0)

        def ID(self):
            return self.getToken(SimpleCParser.ID, 0)

        def FECHA_PARENTESES(self):
            return self.getToken(SimpleCParser.FECHA_PARENTESES, 0)

        def PONTO_VIRGULA(self):
            return self.getToken(SimpleCParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_entrada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrada" ):
                listener.enterEntrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrada" ):
                listener.exitEntrada(self)




    def entrada(self):

        localctx = SimpleCParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(SimpleCParser.RD)
            self.state = 72
            self.match(SimpleCParser.ABRE_PARENTESES)
            self.state = 73
            self.match(SimpleCParser.ID)
            self.state = 74
            self.match(SimpleCParser.FECHA_PARENTESES)
            self.state = 75
            self.match(SimpleCParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PT(self):
            return self.getToken(SimpleCParser.PT, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(SimpleCParser.ABRE_PARENTESES, 0)

        def FECHA_PARENTESES(self):
            return self.getToken(SimpleCParser.FECHA_PARENTESES, 0)

        def PONTO_VIRGULA(self):
            return self.getToken(SimpleCParser.PONTO_VIRGULA, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleCParser.ExpressaoContext,0)


        def STRING(self):
            return self.getToken(SimpleCParser.STRING, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_saida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaida" ):
                listener.enterSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaida" ):
                listener.exitSaida(self)




    def saida(self):

        localctx = SimpleCParser.SaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SimpleCParser.PT)
            self.state = 78
            self.match(SimpleCParser.ABRE_PARENTESES)
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 26, 27]:
                self.state = 79
                self.expressao()
                pass
            elif token in [25]:
                self.state = 80
                self.match(SimpleCParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 83
            self.match(SimpleCParser.FECHA_PARENTESES)
            self.state = 84
            self.match(SimpleCParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SimpleCParser.IF, 0)

        def expressaoLogica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.ExpressaoLogicaContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.ExpressaoLogicaContext,i)


        def bloco(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.BlocoContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.BlocoContext,i)


        def EL(self):
            return self.getToken(SimpleCParser.EL, 0)

        def EI(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.EI)
            else:
                return self.getToken(SimpleCParser.EI, i)

        def getRuleIndex(self):
            return SimpleCParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = SimpleCParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(SimpleCParser.IF)
            self.state = 87
            self.expressaoLogica()
            self.state = 88
            self.bloco()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 89
                self.match(SimpleCParser.EL)
                self.state = 90
                self.bloco()


            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 93
                self.match(SimpleCParser.EI)
                self.state = 94
                self.expressaoLogica()
                self.state = 95
                self.bloco()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WL(self):
            return self.getToken(SimpleCParser.WL, 0)

        def expressaoLogica(self):
            return self.getTypedRuleContext(SimpleCParser.ExpressaoLogicaContext,0)


        def DO(self):
            return self.getToken(SimpleCParser.DO, 0)

        def bloco(self):
            return self.getTypedRuleContext(SimpleCParser.BlocoContext,0)


        def getRuleIndex(self):
            return SimpleCParser.RULE_repeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeticao" ):
                listener.enterRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeticao" ):
                listener.exitRepeticao(self)




    def repeticao(self):

        localctx = SimpleCParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(SimpleCParser.WL)
            self.state = 103
            self.expressaoLogica()
            self.state = 104
            self.match(SimpleCParser.DO)
            self.state = 105
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_CHAVES(self):
            return self.getToken(SimpleCParser.ABRE_CHAVES, 0)

        def FECHA_CHAVES(self):
            return self.getToken(SimpleCParser.FECHA_CHAVES, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.ComandoContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.ComandoContext,i)


        def getRuleIndex(self):
            return SimpleCParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)




    def bloco(self):

        localctx = SimpleCParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(SimpleCParser.ABRE_CHAVES)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68272134) != 0):
                self.state = 108
                self.comando()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(SimpleCParser.FECHA_CHAVES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.TermoContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.TermoContext,i)


        def SOMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.SOMA)
            else:
                return self.getToken(SimpleCParser.SOMA, i)

        def SUBTRACAO(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.SUBTRACAO)
            else:
                return self.getToken(SimpleCParser.SUBTRACAO, i)

        def getRuleIndex(self):
            return SimpleCParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)




    def expressao(self):

        localctx = SimpleCParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.termo()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 117
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 118
                self.termo()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.FatorContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.FatorContext,i)


        def MULTIPLICACAO(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.MULTIPLICACAO)
            else:
                return self.getToken(SimpleCParser.MULTIPLICACAO, i)

        def DIVISAO(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.DIVISAO)
            else:
                return self.getToken(SimpleCParser.DIVISAO, i)

        def getRuleIndex(self):
            return SimpleCParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = SimpleCParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.fator()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 125
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 126
                self.fator()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(SimpleCParser.NUMERO, 0)

        def ID(self):
            return self.getToken(SimpleCParser.ID, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(SimpleCParser.ABRE_PARENTESES, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleCParser.ExpressaoContext,0)


        def FECHA_PARENTESES(self):
            return self.getToken(SimpleCParser.FECHA_PARENTESES, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)




    def fator(self):

        localctx = SimpleCParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fator)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(SimpleCParser.NUMERO)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(SimpleCParser.ID)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.match(SimpleCParser.ABRE_PARENTESES)
                self.state = 135
                self.expressao()
                self.state = 136
                self.match(SimpleCParser.FECHA_PARENTESES)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoLogicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termoLogico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.TermoLogicoContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.TermoLogicoContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.AND)
            else:
                return self.getToken(SimpleCParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.OR)
            else:
                return self.getToken(SimpleCParser.OR, i)

        def getRuleIndex(self):
            return SimpleCParser.RULE_expressaoLogica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoLogica" ):
                listener.enterExpressaoLogica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoLogica" ):
                listener.exitExpressaoLogica(self)




    def expressaoLogica(self):

        localctx = SimpleCParser.ExpressaoLogicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expressaoLogica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.termoLogico()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 141
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 142
                self.termoLogico()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoLogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacao(self):
            return self.getTypedRuleContext(SimpleCParser.ComparacaoContext,0)


        def ABRE_PARENTESES(self):
            return self.getToken(SimpleCParser.ABRE_PARENTESES, 0)

        def expressaoLogica(self):
            return self.getTypedRuleContext(SimpleCParser.ExpressaoLogicaContext,0)


        def FECHA_PARENTESES(self):
            return self.getToken(SimpleCParser.FECHA_PARENTESES, 0)

        def NOT(self):
            return self.getToken(SimpleCParser.NOT, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_termoLogico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoLogico" ):
                listener.enterTermoLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoLogico" ):
                listener.exitTermoLogico(self)




    def termoLogico(self):

        localctx = SimpleCParser.TermoLogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_termoLogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 148
                self.match(SimpleCParser.NOT)


            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 151
                self.comparacao()
                pass

            elif la_ == 2:
                self.state = 152
                self.match(SimpleCParser.ABRE_PARENTESES)
                self.state = 153
                self.expressaoLogica()
                self.state = 154
                self.match(SimpleCParser.FECHA_PARENTESES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.ExpressaoContext,i)


        def IGUAL(self):
            return self.getToken(SimpleCParser.IGUAL, 0)

        def MENOR(self):
            return self.getToken(SimpleCParser.MENOR, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_comparacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacao" ):
                listener.enterComparacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacao" ):
                listener.exitComparacao(self)




    def comparacao(self):

        localctx = SimpleCParser.ComparacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparacao)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.expressao()
                self.state = 159
                self.match(SimpleCParser.IGUAL)
                self.state = 160
                self.expressao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.expressao()
                self.state = 163
                self.match(SimpleCParser.MENOR)
                self.state = 164
                self.expressao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





