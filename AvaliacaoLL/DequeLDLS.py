class No:
    def __init__(self, dado = None, anterior = None, proximo = None):
        self.dado       = dado
        self.anterior   = anterior
        self.proximo    = proximo

class Deque:
    def __init__(self) -> None:
        self.cabeca     = No()
        self.cauda      = No()
        self.cabeca.proximo = self.cauda
        self.cauda.anterior = self.cabeca
        self.tamanho = 0

    def isEmpty(self):
        return self.tamanho == 0
    
    def getSize(self):
        return self.tamanho
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Deque vazio!")
        
        return self.cabeca.proximo.dado
    
    def top(self):
        if self.isEmpty():
            raise Exception("deque vazio!")
        
        return self.cauda.anterior.dado
    
    def addFirst(self, dado):
        no_temp = No(dado)

        primeiro = self.cabeca.proximo

        no_temp.proximo = primeiro
        no_temp.anterior = self.cabeca

        self.cabeca.proximo = no_temp
        primeiro.anterior = no_temp

        self.tamanho += 1

    def addLast(self, dado):
        no_temp = No(dado)

        ultimo = self.cauda.anterior
        no_temp.proximo = self.cauda
        no_temp.anterior = ultimo

        self.cauda.anterior = no_temp
        ultimo.proximo = no_temp
        self.tamanho += 1

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("Deque vazio!")
        
        primeiro = self.cabeca.proximo
        self.cabeca.proximo = primeiro.proximo
        primeiro.proximo.anterior = self.cabeca
        self.tamanho -= 1

        return primeiro.dado
    
    def deleteLast(self):
        if self.isEmpty():
            raise Exception("Deque vazio")

        ultimo = self.cauda.anterior
        self.cauda.anterior = ultimo.anterior
        ultimo.anterior.proximo = self.cauda
        self.tamanho -= 1

        return ultimo.dado
    
    def __str__(self):
        atual = self.cabeca.proximo
        resultado = ""

        while atual != self.cauda:
            resultado += str(atual.dado) + " "
            atual = atual.proximo

        return resultado.strip()