# Análise Semântica da Linguagem cmaismenos

## Objetivo

A análise semântica foi adicionada como uma terceira etapa do compilador, executada depois da análise léxica e da análise sintática do ANTLR.

Fluxo atual:

1. O analisador léxico transforma `entrada.cmm` em tokens.
2. O analisador sintático valida a ordem dos tokens e monta a árvore sintática.
3. O analisador semântico percorre a árvore e valida o significado do programa.
4. O interpretador só executa quando não existem erros léxicos, sintáticos ou semânticos.

## Arquivos Implementados

### `semantica.py`

Esse arquivo concentra a nova camada semântica.

Ele define:

- `AnalisadorSemantico`: visitante responsável por percorrer a árvore gerada pelo ANTLR.
- `SimboloSemantico`: representa uma variável declarada na tabela de símbolos.
- `ErroSemantico`: representa um erro semântico detalhado.

O analisador herda de `cmaismenosVisitor`, o mesmo padrão usado pelo interpretador. Assim, ele visita os nós da árvore sintática sem alterar os arquivos gerados pelo ANTLR.

### `compilador.py`

O arquivo principal foi atualizado para chamar a análise semântica depois do analisador sintático:

```python
analisador_semantico = AnalisadorSemantico()
erros_semanticos = analisador_semantico.analisar(arvore)
```

Se houver erro semântico, a execução para antes do interpretador:

```python
if erros_semanticos:
    sys.exit(1)
```

## Tabela de Símbolos

A tabela de símbolos guarda as variáveis declaradas no programa.

Cada símbolo possui:

- nome da variável;
- tipo da variável;
- linha da declaração;
- coluna da declaração.

Exemplo conceitual:

```text
x -> tipo inteiro, linha 1, coluna 2
nome -> tipo string, linha 7, coluna 2
```

## Escopos

O analisador usa uma pilha de escopos.

O escopo global é criado no início da análise. Sempre que um bloco `{ ... }` é visitado, um novo escopo é aberto. Ao sair do bloco, esse escopo é removido.

Isso permite:

- acessar variáveis declaradas fora do bloco;
- impedir declaração duplicada dentro do mesmo bloco;
- permitir nomes iguais em blocos diferentes.

## Regras Semânticas Implementadas

### 1. Uso de variável não declarada

Código inválido:

```c
pt(x);
```

Se `x` não foi declarada antes, o analisador gera `SEM-001`.

Motivo: o analisador sintático só sabe que `x` é um identificador válido, mas não sabe se ele existe na memória do programa.

### 2. Redeclaração no mesmo escopo

Código inválido:

```c
i x = 1;
i x = 2;
```

O analisador gera `SEM-002`.

Motivo: duas variáveis com o mesmo nome no mesmo escopo causam ambiguidade na tabela de símbolos.

### 3. Incompatibilidade de tipos

Código inválido:

```c
i x = 1;
s nome = "ana";
x = nome;
```

O analisador gera `SEM-003`.

Motivo: `x` foi declarado como inteiro, mas recebeu uma expressão do tipo string.

### 4. Condições precisam ser booleanas

As condições de `if` e `wl` precisam ser comparações ou expressões lógicas.

Exemplo válido:

```c
wl x < 10 do {
    x = x + 1;
}
```

O tipo booleano é usado internamente pelo analisador para representar o resultado de comparações como `x < 10`, `x > 3` e `x == y`.

### 5. Operações aritméticas apenas com inteiros

Código inválido:

```c
s nome = "ana";
pt(nome + 1);
```

O analisador gera `SEM-005`.

Motivo: operadores como `+`, `-`, `*` e `/` só podem operar com números inteiros.

### 6. Comparações com tipos compatíveis

Código inválido:

```c
i x = 1;
s nome = "ana";
if x == nome {
    pt(x);
}
```

O analisador gera `SEM-006`.

Motivo: a comparação `==` exige valores do mesmo tipo. Já `<` e `>` só podem ser usados com inteiros.

## Log de Erros Detalhado

Cada erro semântico inclui:

- código do erro;
- linha;
- coluna;
- lexema;
- contexto;
- mensagem;
- sugestão de correção.

Formato:

```text
SEM-001 [Linha 2, Coluna 3] Lexema: 'y' | Contexto: uso de variável | Mensagem: Variável 'y' usada antes de ser declarada. | Sugestão: Declare 'y' antes de usar esse identificador em uma expressão.
```

Os erros aparecem no terminal e também são registrados em `compilador.log`.

## Códigos de Erro

| Código | Significado |
| --- | --- |
| `SEM-001` | Variável usada antes da declaração |
| `SEM-002` | Variável redeclarada no mesmo escopo |
| `SEM-003` | Incompatibilidade de tipos em declaração ou atribuição |
| `SEM-004` | Uso inválido de expressão lógica ou condição |
| `SEM-005` | Operação aritmética com tipo inválido |
| `SEM-006` | Comparação com tipos incompatíveis |

## Exemplo de Falhas Encontradas

Entrada:

```c
i x = 1;
pt(y);
s nome = "ana";
x = nome;
nome = x + 1;
i x = 2;
```

Saída semântica:

```text
ERRO SEMÂNTICO: SEM-001 [Linha 2, Coluna 3] Lexema: 'y' | Contexto: uso de variável | Mensagem: Variável 'y' usada antes de ser declarada. | Sugestão: Declare 'y' antes de usar esse identificador em uma expressão.
ERRO SEMÂNTICO: SEM-003 [Linha 4, Coluna 0] Lexema: 'x' | Contexto: atribuição | Mensagem: Variável 'x' é do tipo inteiro, mas recebeu expressão do tipo string. | Sugestão: Atribua um valor compatível com o tipo declarado da variável.
ERRO SEMÂNTICO: SEM-003 [Linha 5, Coluna 0] Lexema: 'nome' | Contexto: atribuição | Mensagem: Variável 'nome' é do tipo string, mas recebeu expressão do tipo inteiro. | Sugestão: Atribua um valor compatível com o tipo declarado da variável.
ERRO SEMÂNTICO: SEM-002 [Linha 6, Coluna 2] Lexema: 'x' | Contexto: declaração de variável | Mensagem: Variável 'x' já foi declarada neste escopo. | Sugestão: Use outro nome ou remova a declaração duplicada. A declaração anterior está na linha 1, coluna 2.
```

## Como Apresentar

A implementação pode ser apresentada em três partes:

1. A gramática ANTLR garante que o código tem forma correta.
2. O `AnalisadorSemantico` garante que os identificadores e tipos fazem sentido.
3. O interpretador só roda quando as etapas anteriores não encontram falhas.

Essa separação deixa o compilador mais organizado porque cada fase tem uma responsabilidade clara.
