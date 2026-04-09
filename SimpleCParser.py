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
        4,1,7,28,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,9,
        2,1,2,0,0,3,0,2,4,0,0,26,0,7,1,0,0,0,2,13,1,0,0,0,4,19,1,0,0,0,6,
        8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,
        1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,5,1,0,0,14,15,5,5,0,0,15,
        16,5,2,0,0,16,17,3,4,2,0,17,18,5,4,0,0,18,3,1,0,0,0,19,24,5,6,0,
        0,20,21,5,3,0,0,21,23,5,6,0,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,
        1,0,0,0,24,25,1,0,0,0,25,5,1,0,0,0,26,24,1,0,0,0,2,9,24
    ]

class SimpleCParser ( Parser ):

    grammarFileName = "SimpleC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'='", "'+'", "';'" ]

    symbolicNames = [ "<INVALID>", "TIPO", "ATRIBUICAO", "SOMA", "PONTO_VIRGULA", 
                      "ID", "NUMERO", "ESPACO" ]

    RULE_programa = 0
    RULE_declaracao = 1
    RULE_expressao = 2

    ruleNames =  [ "programa", "declaracao", "expressao" ]

    EOF = Token.EOF
    TIPO=1
    ATRIBUICAO=2
    SOMA=3
    PONTO_VIRGULA=4
    ID=5
    NUMERO=6
    ESPACO=7

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

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(SimpleCParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return SimpleCParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = SimpleCParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.declaracao()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 11
            self.match(SimpleCParser.EOF)
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

        def TIPO(self):
            return self.getToken(SimpleCParser.TIPO, 0)

        def ID(self):
            return self.getToken(SimpleCParser.ID, 0)

        def ATRIBUICAO(self):
            return self.getToken(SimpleCParser.ATRIBUICAO, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpleCParser.ExpressaoContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(SimpleCParser.PONTO_VIRGULA, 0)

        def getRuleIndex(self):
            return SimpleCParser.RULE_declaracao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = SimpleCParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(SimpleCParser.TIPO)
            self.state = 14
            self.match(SimpleCParser.ID)
            self.state = 15
            self.match(SimpleCParser.ATRIBUICAO)
            self.state = 16
            self.expressao()
            self.state = 17
            self.match(SimpleCParser.PONTO_VIRGULA)
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

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.NUMERO)
            else:
                return self.getToken(SimpleCParser.NUMERO, i)

        def SOMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCParser.SOMA)
            else:
                return self.getToken(SimpleCParser.SOMA, i)

        def getRuleIndex(self):
            return SimpleCParser.RULE_expressao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = SimpleCParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expressao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(SimpleCParser.NUMERO)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 20
                self.match(SimpleCParser.SOMA)
                self.state = 21
                self.match(SimpleCParser.NUMERO)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





