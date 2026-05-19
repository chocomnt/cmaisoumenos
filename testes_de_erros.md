# Testes de Erros do Compilador

## Como Rodar

Use o compilador passando o arquivo de teste:

```bash
python compilador.py teste_erros_semanticos.cmm --somente-analisar
python compilador.py teste_erro_sintatico.cmm --somente-analisar
python compilador.py teste_erro_lexico.cmm --somente-analisar
```

Ou rode diretamente:

```bash
./teste_erros_semanticos.cmm --somente-analisar
./teste_erro_sintatico.cmm --somente-analisar
./teste_erro_lexico.cmm --somente-analisar
```

## Ordem das Análises

O compilador interpreta os erros nesta ordem:

1. análise léxica;
2. análise sintática;
3. análise semântica.

Se houver erro léxico ou sintático, o compilador para antes da análise semântica.

## Erro Léxico

Arquivo:

```bash
teste_erro_lexico.cmm
```

Exemplo:

```c
pt(@);
```

Interpretação:

O caractere `@` não pertence à linguagem. O analisador léxico não consegue transformar esse caractere em token.

Erro esperado:

```text
ERRO LÉXICO [Linha 7, Coluna 3] Lexema: '' | Mensagem: Token não reconhecido pelo analisador léxico: '@'.
```

## Erro Sintático

Arquivo:

```bash
teste_erro_sintatico.cmm
```

Exemplo:

```c
i x = 10
pt(x);
```

Interpretação:

A declaração de variável precisa terminar com `;`. O analisador sintático entende os tokens, mas eles estão em uma ordem inválida para a gramática.

Erro esperado:

```text
ERRO SINTÁTICO [Linha 7, Coluna 0] Lexema: 'pt' | Mensagem: faltando ';' at 'pt'
```

## Erros Semânticos

Arquivo:

```bash
teste_erros_semanticos.cmm
```

Esse arquivo tem sintaxe válida, mas o significado do código está errado.

### SEM-001: variável não declarada

Exemplo:

```c
pt(y);
```

Interpretação:

`y` é um identificador válido, mas não foi declarado antes de ser usado.

### SEM-002: variável redeclarada

Exemplo:

```c
i x = 10;
i x = 20;
```

Interpretação:

`x` foi declarado duas vezes no mesmo escopo.

### SEM-003: tipo incompatível

Exemplo:

```c
i x = 10;
s nome = "ana";
x = nome;
```

Interpretação:

`x` é inteiro, mas recebeu uma variável de texto.

### SEM-005: operação aritmética inválida

Exemplo:

```c
pt(nome + 2);
```

Interpretação:

O operador `+` só pode ser usado com inteiros. `nome` é texto.

### SEM-006: comparação inválida

Exemplo:

```c
if x == nome {
    pt(x);
}
```

Interpretação:

`x` é inteiro e `nome` é texto. A comparação `==` exige valores do mesmo tipo.

## Onde Ver os Detalhes

Todos os erros aparecem no terminal e também ficam registrados em:

```bash
compilador.log
```
