# Regras:

## Organização de letras:
- Variáveis: 1 letra (String: s, int: i)
- Entrada/Saida: 2 letras (print: pt, read: rd)
- Controles: 2 letras (if: if, else: el, else if: ei, do: do, while: wl)

## Operações:
- (+, -, =, ==, /, *, and, or, !)

## Comentários:
- Agora é possível comentar no código usando "#" para comentários em linha e "###" para comentários em bloco.

# Ativação: 
 - Ative o ambiente virtual com o presente na pasta "antlr/bin/activate"

# Compilação:
 - depois de qualquer mudança grande na lógica, compile novamente com o comando: java -jar antlr-4.x.x-complete.jar -Dlanguage=Python3 -visitor cmaismenos.g4
 - Todos os tokens gerados são guardados dentro de 

# Rodando:
- Rode o código com o comando "python parse.py", ou simplesmente execute o parse.py, os comandos devem ser colocados no arquivo entrada.cmm, ou qualquer arquivo com a extensão ".cmm"

- Toda a gramática do compilador está presente no arquivo cmaismenos.g4
- Todo o analisador léxico está presente no cmaismenosLexer, ele quem faz a análise léxica indentificando tipos e nomes e gerando tokens.
- Toda a analise sintática é feita no cmaismenosParser.py, ele pega os tokens gerados e verifica se estão na ordem correta, montando a árvore sintática.
- O cmaismenosVisitor.py é um arquivo gerado pelo python que percorre a árvore gerada pelo parser e calcula resultados, variáveis e coisas desse tipo.
- As lógicas e execuções estão todas presentes no arquivo interpretador.py
- O arquivo parse.py serve básicamente pra gerar os logs caso algum erro aconteça.