from antlr4 import *
from SimpleCLexer import SimpleCLexer
from SimpleCParser import SimpleCParser

stream = FileStream("entrada.cmm", encoding="utf-8")
lexer = SimpleCLexer(stream)
tokens = CommonTokenStream(lexer)
parser = SimpleCParser(tokens)

tree = parser.programa()
print(tree.toStringTree(recog=parser))