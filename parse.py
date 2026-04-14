import logging
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree import Trees
from SimpleCLexer import SimpleCLexer
from SimpleCParser import SimpleCParser

# Configurar logging
logging.basicConfig(filename='parser.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Distinguir entre erro léxico e sintático
        if 'token recognition error' in msg or 'extraneous input' in msg:
            error_type = "ERRO LÉXICO"
        else:
            error_type = "ERRO SINTÁTICO"
        error_msg = f"{error_type} [Linha {line}, Coluna {column}]: {msg}"
        print(error_msg)
        logging.error(error_msg)

def generate_dot(tree, parser, filename='ast.dot'):
    """Gera arquivo DOT para visualização da AST"""
    def get_node_text(node):
        if hasattr(node, 'getText'):
            return node.getText()
        return str(node)

    def traverse_tree(node, parent_id, node_id_counter):
        node_id = f"node{node_id_counter[0]}"
        node_id_counter[0] += 1
        label = get_node_text(node)
        dot_lines.append(f'  {node_id} [label="{label}"];')
        if parent_id:
            dot_lines.append(f'  {parent_id} -> {node_id};')
        
        if hasattr(node, 'children') and node.children:
            for child in node.children:
                traverse_tree(child, node_id, node_id_counter)
        return node_id

    dot_lines = ['digraph AST {', '  node [shape=box];']
    node_id_counter = [0]
    traverse_tree(tree, None, node_id_counter)
    dot_lines.append('}')
    
    with open(filename, 'w') as f:
        f.write('\n'.join(dot_lines))
    print(f"AST gerada em {filename}")

# Processar arquivo-fonte
stream = FileStream("entrada.cmm", encoding="utf-8")
lexer = SimpleCLexer(stream)

# Adicionar listener de erro customizado
lexer.removeErrorListeners()
lexer.addErrorListener(CustomErrorListener())

# Gerar tokens no formato: <Tipo do Token, Lexema, Linha, Coluna>
tokens = CommonTokenStream(lexer)
tokens.fill()

print("Tokens gerados:")
for token in tokens.tokens:
    if token.type != Token.EOF:
        token_type = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else str(token.type)
        print(f"<{token_type}, '{token.text}', {token.line}, {token.column}>")
        logging.info(f"Token: <{token_type}, '{token.text}', {token.line}, {token.column}>")

# Parsing
parser = SimpleCParser(tokens)
parser.removeErrorListeners()
parser.addErrorListener(CustomErrorListener())

logging.info("Iniciando parsing...")
tree = parser.programa()
logging.info("Parsing concluído.")

print("\nÁrvore de sintaxe textual:")
print(tree.toStringTree(recog=parser))

# Gerar AST em DOT
generate_dot(tree, parser)