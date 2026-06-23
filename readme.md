# Linguagem cmaismenos

## Regras

### Organização de letras

- Variáveis: tipo `i` para inteiro e tipo `s` para texto.
- Entrada e saída: `rd` para leitura e `pt` para impressão.
- Controle de fluxo: `if`, `el`, `ei`, `do` e `wl`.

### Operações

- Atribuição: `=`
- Comparação: `==`, `<`, `>`
- Aritmética: `+`, `-`, `/`, `*`
- Lógica: `and`, `or`, `!`

### Comentários

- Comentário em linha: `# comentário`
- Comentário em bloco: `### comentário ###`

## Ativação

Ative o ambiente virtual:

```bash
source ../antlr/bin/activate
```

Também é possível chamar o Python do ambiente diretamente:

```bash
../antlr/bin/python compilador.py
```

## Geração dos Arquivos ANTLR

Depois de uma mudança grande na gramática, gere novamente os arquivos do ANTLR:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor cmaismenos.g4
```

Os arquivos `cmaismenosLexer.py`, `cmaismenosParser.py`, `cmaismenosVisitor.py` e `cmaismenosListener.py` são gerados automaticamente pelo ANTLR.

## Interface do Compilador

A interface principal está no arquivo `compilador.py`.

Execução padrão:

```bash
python compilador.py
```

Por padrão, o compilador usa `entrada.cmm`, gera `compilador.log`, gera `arvore.dot` e executa o programa se as análises passarem.

Executar outro arquivo:

```bash
python compilador.py caminho/do/programa.cmm
```

Executar apenas as análises, sem rodar o interpretador:

```bash
python compilador.py --somente-analisar
```

Mostrar a árvore sintática textual:

```bash
python compilador.py --mostrar-arvore
```

Não gerar o arquivo DOT da árvore:

```bash
python compilador.py --sem-arvore-dot
```

Definir nomes de saída:

```bash
python compilador.py entrada.cmm --log compilador.log --arvore-dot arvore.dot
```

Gerar código Python equivalente ao programa .cmm:

```bash
python compilador.py --gerar
```

Gerar código Python com nome de saída personalizado:

```bash
python compilador.py entrada.cmm --gerar --saida programa.py
```

Executar o código Python gerado:

```bash
python saida.py
```

Ver todas as opções:

```bash
python compilador.py --ajuda
```

Rodar um .cmm diretamente, se ele tiver a primeira linha especial e permissão de execução:

```bash
./teste_compilador.cmm
```

## Etapas do Compilador

- `cmaismenos.g4`: gramática da linguagem.
- `cmaismenosLexer.py`: analisador léxico gerado pelo ANTLR.
- `cmaismenosParser.py`: analisador sintático gerado pelo ANTLR.
- `cmaismenosVisitor.py`: visitante gerado pelo ANTLR.
- `semantica.py`: analisador semântico escrito manualmente.
- `interpretador.py`: execução dos comandos da linguagem.
- `gerador.py`: geração de código Python equivalente ao programa .cmm.
- `compilador.py`: interface principal do compilador.

## Tratamento de Erros

Os erros são apresentados no terminal e registrados em `compilador.log`.

Cada erro informa:

- tipo do erro;
- linha;
- coluna;
- lexema;
- mensagem em português.

Exemplo de erro léxico ou sintático:

```text
ERRO SINTÁTICO [Linha 3, Coluna 5] Lexema: 'x' | Mensagem: entrada incompatível 'x' esperado {'i', 's', '}', 'rd', 'pt', 'if', 'wl'}
```

Exemplo de erro semântico:

```text
ERRO SEMÂNTICO: SEM-001 [Linha 2, Coluna 3] Lexema: 'y' | Contexto: uso de variável | Mensagem: Variável 'y' usada antes de ser declarada. | Sugestão: Declare 'y' antes de usar esse identificador em uma expressão.
```

## Geração de Código Python

O compilador pode gerar código Python equivalente ao programa `.cmm`. A tradução mantém a semântica da linguagem original usando construções nativas do Python:

| cmaismenos | Python |
|------------|--------|
| `i x = 10;` | `x = 10` |
| `s nome = "texto";` | `nome = "texto"` |
| `x = 5;` | `x = 5` |
| `rd(x);` | `x = int(input())` ou `x = input()` |
| `pt(x);` | `print(x)` |
| `if ... { } el { }` | `if ...: ... else: ...` |
| `ei ... { }` | `elif ...: ...` |
| `wl ... do { }` | `while ...: ...` |
| `a / b` | `a // b` |
| `and`, `or`, `!` | `and`, `or`, `not` |

O fluxo de geração de código é:

1. lê um arquivo .cmm;
2. faz análise léxica;
3. faz análise sintática;
4. faz análise semântica;
5. gera código Python equivalente;
6. salva no arquivo de saída (padrão: `saida.py`).

Se houver erros em qualquer etapa, o código não é gerado.

## Opções da Interface

```
argumentos:
  arquivo               arquivo fonte .cmm que será analisado e executado; padrão: entrada.cmm

opções:
  -h, --ajuda           mostra esta mensagem de ajuda e encerra
  --somente-analisar    executa as análises léxica, sintática e semântica sem rodar o interpretador
  --mostrar-arvore      mostra a árvore sintática textual no terminal
  --sem-arvore-dot      não gera o arquivo DOT da árvore sintática
  --arvore-dot ARVORE_DOT
                        nome do arquivo DOT gerado; padrão: arvore.dot
  --log LOG             nome do arquivo de log; padrão: compilador.log
  --gerar               gera código Python equivalente ao programa .cmm
  --saida SAIDA         nome do arquivo Python gerado; padrão: saida.py
```
