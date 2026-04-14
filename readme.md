# Regras:

## Organização de letras:
- Variáveis: 1 letra (String: s, int: i)
- Entrada/Saida: 2 letras (print: pt, read: rd)
- Controles: 2 letras (if: if, else: el, else if: ei, do: do, while: wl)

## Operações:
- (+, -, =, ==, /, *, and, or, !)

# Ativação: 
 - Ative o ambiente virtual com o presente na pasta "antlr/bin/activate"

# Rodando:
- Rode o código com o comando "python parse.py", ou simplesmente execute o parse.py, os comandos devem ser colocados no arquivo entrada.cmm, ou qualquer arquivo com a extensão ".cmm"
- Toda a gramática do compilador está presente no arquivo simpleC.g4
- Todo o analisador léxico está presente no SimpleCLexer, ele quem faz a análise léxica indentificando tipos e nomes e gerando tokens.
- Toda a analise sintática é feita no SimpleCParser.py, ele pega os tokens gerados e verifica se estão na ordem correta, montando a árvore sintática.
- O simpleCVisitor.py é um arquivo gerado pelo python que percorre a árvore gerada pelo parser e calcula resultados, variáveis e coisas desse tipo.
