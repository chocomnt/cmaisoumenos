from cmaismenosVisitor import cmaismenosVisitor
from cmaismenosParser import cmaismenosParser

class Interpretador(cmaismenosVisitor):
    def __init__(self):
        self.memoria = {}

    def visitPrograma(self, ctx: cmaismenosParser.ProgramaContext):
        for comando in ctx.comando():
            self.visit(comando)

    def visitDeclaracaoInt(self, ctx: cmaismenosParser.DeclaracaoIntContext):
        nome = ctx.ID().getText()
        valor = self.visit(ctx.expressao())
        self.memoria[nome] = int(valor)

    def visitDeclaracaoStr(self, ctx: cmaismenosParser.DeclaracaoStrContext):
        nome = ctx.ID().getText()
        valor = ctx.STRING().getText()[1:-1] # Remove aspas
        self.memoria[nome] = str(valor)

    def visitAtribuicao(self, ctx: cmaismenosParser.AtribuicaoContext):
        nome = ctx.ID().getText()
        if nome not in self.memoria:
            raise Exception(f"Variável '{nome}' não declarada!")
        
        valor = self.visit(ctx.expressao())
        
        if isinstance(self.memoria[nome], int):
            self.memoria[nome] = int(valor)
        else:
            self.memoria[nome] = str(valor)

    def visitEntrada(self, ctx: cmaismenosParser.EntradaContext):
        nome = ctx.ID().getText()
        if nome not in self.memoria:
            raise Exception(f"Variável '{nome}' não declarada!")
            
        valor = input(f"{nome} > ")
        if isinstance(self.memoria[nome], int):
            self.memoria[nome] = int(valor)
        else:
            self.memoria[nome] = str(valor)

    def visitSaida(self, ctx: cmaismenosParser.SaidaContext):
        if ctx.STRING():
            print(ctx.STRING().getText()[1:-1])
        else:
            valor = self.visit(ctx.expressao())
            print(valor)

    def visitExpressao(self, ctx: cmaismenosParser.ExpressaoContext):
        esquerda = self.visit(ctx.termo(0))
        for i in range(1, len(ctx.termo())):
            op = ctx.getChild(2 * i - 1).getText()
            direita = self.visit(ctx.termo(i))
            if op == '+':
                esquerda = esquerda + direita
            elif op == '-':
                esquerda = esquerda - direita
        return esquerda

    def visitTermo(self, ctx: cmaismenosParser.TermoContext):
        esquerda = self.visit(ctx.fator(0))
        for i in range(1, len(ctx.fator())):
            op = ctx.getChild(2 * i - 1).getText()
            direita = self.visit(ctx.fator(i))
            if op == '*':
                esquerda = esquerda * direita
            elif op == '/':
                esquerda = esquerda // direita
        return esquerda

    def visitFator(self, ctx: cmaismenosParser.FatorContext):
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.ID():
            nome = ctx.ID().getText()
            if nome in self.memoria:
                return self.memoria[nome]
            raise Exception(f"Variável '{nome}' não identificada!")
        elif ctx.expressao():
            return self.visit(ctx.expressao())

    def visitExpressaoLogica(self, ctx: cmaismenosParser.ExpressaoLogicaContext):
        esquerda = self.visit(ctx.termoLogico(0))
        for i in range(1, len(ctx.termoLogico())):
            op = ctx.getChild(2 * i - 1).getText()
            direita = self.visit(ctx.termoLogico(i))
            if op == 'and':
                esquerda = esquerda and direita
            elif op == 'or':
                esquerda = esquerda or direita
        return esquerda

    def visitTermoLogico(self, ctx: cmaismenosParser.TermoLogicoContext):
        resultado = None
        if ctx.comparacao():
            resultado = self.visit(ctx.comparacao())
        else:
            resultado = self.visit(ctx.expressaoLogica())
            
        return not resultado if ctx.NOT() else resultado

    def visitComparacao(self, ctx: cmaismenosParser.ComparacaoContext):
        esquerda = self.visit(ctx.expressao(0))
        direita = self.visit(ctx.expressao(1))
        op = ctx.getChild(1).getText()
        if op == '==': return esquerda == direita
        if op == '<': return esquerda < direita
        if op == '>': return esquerda > direita

    def visitCondicional(self, ctx: cmaismenosParser.CondicionalContext):
        condicao_atendida = False
        
        # Avalia a primeira condição lógica ligada ao IF (índice 0)
        if self.visit(ctx.expressaoLogica(0)):
            self.visit(ctx.bloco(0))
            condicao_atendida = True
            
        # Avalia os ELSE IF (EI) em caso de não atendimento
        if not condicao_atendida:
            for i in range(len(ctx.children)):
                child = ctx.children[i]
                if child.getText() == 'ei':
                    # O próximo filho lógico é a expressaoLogica e o seguinte é o bloco
                    if self.visit(ctx.children[i+1]):
                        self.visit(ctx.children[i+2])
                        condicao_atendida = True
                        break
                        
        # Avalia o ELSE (EL) como fallback
        if not condicao_atendida and ctx.EL():
            for i in range(len(ctx.children)):
                if ctx.children[i].getText() == 'el':
                    self.visit(ctx.children[i+1])
                    break

    def visitRepeticao(self, ctx: cmaismenosParser.RepeticaoContext):
        while self.visit(ctx.expressaoLogica()):
            self.visit(ctx.bloco())

    def visitBloco(self, ctx: cmaismenosParser.BlocoContext):
        for comando in ctx.comando():
            self.visit(comando)
