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

Ver todas as opções:

```bash
python compilador.py --ajuda
```

## Etapas do Compilador

- `cmaismenos.g4`: gramática da linguagem.
- `cmaismenosLexer.py`: analisador léxico gerado pelo ANTLR.
- `cmaismenosParser.py`: analisador sintático gerado pelo ANTLR.
- `cmaismenosVisitor.py`: visitante gerado pelo ANTLR.
- `semantica.py`: analisador semântico escrito manualmente.
- `interpretador.py`: execução dos comandos da linguagem.
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

## Documentação da Análise Semântica

A explicação completa da implementação está em `analise_semantica.md`.

• A interface do compilador é o arquivo compilador.py:1.

  No projeto, ela é o “ponto de entrada” do compilador. Em vez de você chamar manualmente cada parte, ela organiza tudo em ordem:

  1. lê um arquivo .cmm;
  2. faz análise léxica;
  3. faz análise sintática;
  4. faz análise semântica;
  5. gera log;
  6. gera a árvore sintática em .dot;
  7. executa o programa se não houver erro.

  Usos principais

  Rodar o programa padrão entrada.cmm:

  python compilador.py

  Rodar outro arquivo .cmm:

  python compilador.py teste_compilador.cmm

  Fazer apenas as análises, sem executar:

  python compilador.py teste_erros_semanticos.cmm --somente-analisar

  Mostrar a árvore sintática no terminal:

  python compilador.py entrada.cmm --mostrar-arvore

  Não gerar o arquivo arvore.dot:

  python compilador.py entrada.cmm --sem-arvore-dot

  Escolher o nome do arquivo .dot:

  python compilador.py entrada.cmm --arvore-dot minha_arvore.dot

  Escolher o nome do log:

  python compilador.py entrada.cmm --log meu_log.log

  Ver todas as opções:

  python compilador.py --ajuda

  Rodar um .cmm diretamente, se ele tiver a primeira linha especial e permissão de execução:

  ./teste_compilador.cmm

  No fundo, a interface serve para transformar o projeto em uma ferramenta mais parecida com um compilador real: você passa um arquivo fonte e ela controla todo
  o fluxo.
