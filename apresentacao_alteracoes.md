# Apresentação das Alterações

## 1. Objetivo

O objetivo das alterações foi deixar o compilador mais organizado, com nomes em português, uma interface de uso mais clara e uma etapa de análise semântica antes da execução.

## 2. Arquivos Criados ou Renomeados

- `compilador.py`: nova interface principal do compilador.
- `semantica.py`: camada de análise semântica.
- `analise_semantica.md`: explicação técnica da análise semântica.
- `compilador.log`: arquivo de log gerado durante a execução.
- `arvore.dot`: arquivo DOT da árvore sintática.

## 3. Interface do Compilador

Antes, o projeto era executado pelo `parse.py`.

Agora, a execução principal é feita por:

```bash
python compilador.py
```

Também foram adicionadas opções:

```bash
python compilador.py --somente-analisar
python compilador.py --mostrar-arvore
python compilador.py --sem-arvore-dot
python compilador.py --ajuda
```

Isso torna o compilador mais fácil de testar e apresentar.

## 4. Análise Semântica

A análise semântica foi implementada em `semantica.py`.

Ela verifica erros que a análise sintática não consegue identificar, como:

- variável usada antes de ser declarada;
- variável declarada duas vezes no mesmo escopo;
- atribuição com tipo incompatível;
- uso errado de operadores aritméticos;
- comparação entre tipos incompatíveis.

## 5. Tratamento de Erros

Os erros agora são exibidos com mais detalhes:

```text
ERRO SEMÂNTICO: SEM-001 [Linha 2, Coluna 3] Lexema: 'y' | Contexto: uso de variável | Mensagem: Variável 'y' usada antes de ser declarada. | Sugestão: Declare 'y' antes de usar esse identificador em uma expressão.
```

Cada erro mostra:

- tipo do erro;
- linha;
- coluna;
- lexema;
- contexto;
- mensagem;
- sugestão de correção.

## 6. Como Demonstrar

Primeiro, mostre a interface:

```bash
python compilador.py --ajuda
```

Depois, rode um programa correto:

```bash
python compilador.py
```

Em seguida, coloque um erro em `entrada.cmm`:

```c
i x = 1;
pt(y);
```

E rode:

```bash
python compilador.py --somente-analisar
```

O compilador deve parar na análise semântica e mostrar o erro detalhado.

## 7. Conclusão

As alterações deixam o compilador mais próximo de uma estrutura real:

1. análise léxica;
2. análise sintática;
3. análise semântica;
4. execução.

Com isso, o interpretador só roda quando o código passa por todas as validações.
