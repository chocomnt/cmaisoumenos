# Generated from SimpleC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete generic visitor for a parse tree produced by SimpleCParser.

class SimpleCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleCParser#programa.
    def visitPrograma(self, ctx:SimpleCParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#declaracao.
    def visitDeclaracao(self, ctx:SimpleCParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCParser#expressao.
    def visitExpressao(self, ctx:SimpleCParser.ExpressaoContext):
        return self.visitChildren(ctx)



del SimpleCParser