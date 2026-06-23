# Apresentação: Geração de Código Python

## O que foi implementado

Implementação da etapa final do compilador: **geração de código em alto nível (Python)**.

## Nova funcionalidade

O compilador agora pode traduzir programas `.cmm` para código Python equivalente, mantendo a semântica original da linguagem.

## Arquivos modificados

- **gerador.py** (novo) - Visitor que percorre a AST e gera código Python
- **compilador.py** - Integrado com opções `--gerar` e `--saida`
- **readme.md** - Documentação atualizada

## Opções da interface do compilador

### Argumentos posicionais

| Opção | Descrição |
|-------|-----------|
| `arquivo` | Arquivo fonte `.cmm` que será processado. Padrão: `entrada.cmm` |

### Opções de análise

| Opção | Descrição |
|-------|-----------|
| `--somente-analisar` | Executa apenas análises léxica, sintática e semântica, sem executar o programa |
| `--mostrar-arvore` | Exibe a árvore sintática (parse tree) no terminal em formato textual |
| `--sem-arvore-dot` | Desabilita a geração do arquivo DOT da árvore sintática |
| `--arvore-dot ARVORE_DOT` | Define o nome do arquivo DOT gerado. Padrão: `arvore.dot` |
| `--log LOG` | Define o nome do arquivo de log. Padrão: `compilador.log` |

### Opções de geração de código (NOVO)

| Opção | Descrição |
|-------|-----------|
| `--gerar` | Gera código Python equivalente ao programa `.cmm` em vez de executar o interpretador |
| `--saida SAIDA` | Define o nome do arquivo Python gerado. Padrão: `saida.py` |

## Como funciona

```
Programa .cmm → Análise Léxica → Análise Sintática → Análise Semântica → Geração de Código Python
```

O gerador usa o padrão Visitor (mesmo padrão do interpretador) para percorrer a árvore sintática e emitir código Python equivalente.

## Detalhes técnicos da implementação

### Classe GeradorPython

```python
class GeradorPython(cmaismenosVisitor):
    def __init__(self):
        self.linhas = []        # Lista de linhas de código geradas
        self.indentacao = 0     # Controle de indentação para blocos
        self.tipos = {}         # Mapeamento de variáveis para seus tipos
```

### Métodos principais

Cada método `visit*` corresponde a uma regra da gramática e gera o código Python equivalente:

| Método | Regra da gramática | O que gera |
|--------|-------------------|------------|
| `visitPrograma()` | `programa` | Itera sobre todos os comandos |
| `visitDeclaracaoInt()` | `declaracaoInt` | Atribuição simples: `x = 10` |
| `visitDeclaracaoStr()` | `declaracaoStr` | Atribuição de string: `nome = "texto"` |
| `visitAtribuicao()` | `atribuicao` | Atribuição: `x = expr` |
| `visitEntrada()` | `entrada` | `x = int(input())` ou `x = input()` |
| `visitSaida()` | `saida` | `print(expr)` |
| `visitCondicional()` | `condicional` | `if`/`elif`/`else` |
| `visitRepeticao()` | `repeticao` | `while condicao:` |
| `visitExpressao()` | `expressao` | Expressões aritméticas com `+`, `-` |
| `visitTermo()` | `termo` | Multiplicação/divisão (`/` vira `//`) |
| `visitFator()` | `fator` | Literais, variáveis, parênteses |
| `visitExpressaoLogica()` | `expressaoLogica` | Operadores `and`, `or` |
| `visitTermoLogico()` | `termoLogico` | Negação com `not` |
| `visitComparacao()` | `comparacao` | Comparações `==`, `<`, `>` |

### Controle de indentação

```python
def _emitir(self, linha):
    self.linhas.append("    " * self.indentacao + linha)
```

- `self.indentacao` é incrementado ao entrar em blocos (`if`, `while`)
- Decrementado ao sair dos blocos
- Garante que o código Python gerado tenha indentação correta

### Tratamento de condicionais

A gramática permite: `if ... { } el { } (ei ... { })*`

```python
def visitCondicional(self, ctx):
    # 1. Emite o if principal
    self._emitir(f"if {condicao}:")
    
    # 2. Verifica se tem else (el)
    if proximo_token == 'el':
        self._emitir("else:")
    
    # 3. Processa elifs (ei) em loop
    while houver_ei:
        self._emitir(f"elif {condicao}:")
```

### Divisão inteira

Na linguagem cmaismenos, `/` faz divisão inteira (como em C++).
No Python 3, `/` faz divisão float e `//` faz divisão inteira.

```python
def visitTermo(self, ctx):
    if op == "/":
        resultado = f"{esquerda} // {direita}"  # Traduz para //
    else:
        resultado = f"{esquerda} {op} {direita}"
```

### Entrada de dados com tipo

O gerador verifica o tipo da variável para gerar `int(input())` ou `input()`:

```python
def visitEntrada(self, ctx):
    nome = ctx.ID().getText()
    if self.tipos.get(nome) == "int":
        self._emitir(f"{nome} = int(input())")
    else:
        self._emitir(f"{nome} = input()")
```

## Mapeamento das construções

| cmaismenos | Python |
|------------|--------|
| `i x = 10;` | `x = 10` |
| `s nome = "texto";` | `nome = "texto"` |
| `rd(x);` | `x = int(input())` ou `x = input()` |
| `pt(x);` | `print(x)` |
| `if ... { } el { }` | `if ...: ... else: ...` |
| `ei ... { }` | `elif ...: ...` |
| `wl ... do { }` | `while ...: ...` |
| `a / b` | `a // b` |
| `and`, `or`, `!` | `and`, `or`, `not` |

## Exemplo completo

**entrada.cmm:**
```
i x = 10;
i y = 5;

if x > y {
    pt("x é maior");
} el {
    pt("y é maior");
}

wl x > 0 do {
    pt(x);
    x = x - 1;
}
```

**Comando:**
```bash
python compilador.py entrada.cmm --gerar --saida programa.py
```

**programa.py gerado:**
```python
x = 10
y = 5
if x > y:
    print("x é maior")
else:
    print("y é maior")
while x > 0:
    print(x)
    x = x - 1
```

## Fluxo completo do compilador

1. **Análise Léxica** - Tokenização do código fonte (ANTLR Lexer)
2. **Análise Sintática** - Construção da árvore sintática (ANTLR Parser)
3. **Análise Semântica** - Verificação de tipos e escopos (`semantica.py`)
4. **Geração de Código** - Tradução para Python (`gerador.py`) ← NOVO
5. **Execução** - Interpretador (`interpretador.py`) OU código Python gerado

## Destaques da implementação

- **Reutilização de infraestrutura** - Aproveita todas as análises existentes
- **Padrão Visitor** - Mesmo padrão do interpretador, facilitando manutenção
- **Código legível** - Python gerado é formatado e indentado corretamente
- **Tratamento de erros** - Só gera código se todas as análises passarem
- **Suporte completo** - Todas as construções da linguagem são traduzidas
