class HashTable:
    #Inicializando as células da tabela hash
    def __init__(self):
        self.tamanho = 980931 #tamanho do dicionario utilizado no trab
        self.ids = [None] * self.tamanho #ids da tabela
        self.dados = [None] * self.tamanho #dados da tabela

    #função principal de hash
    def hashtable(self, k, dado):
      valor = self.H1(k, len(self.ids))
      
      if (self.ids[valor] == None):
        self.ids[valor] = k
        self.dados[valor] = dado
      else:
        if(self.ids[valor] == k):
          self.dados[valor] = dado
        else:
          proximo = self.H2(valor, len(self.ids))
          
          while ((self.ids[proximo] != None) and (self.ids[proximo] != k)):
            proximo = self.H2(proximo, len(self.ids))
          
          if(self.ids[proximo] == None):
            self.ids[proximo] = k
            self.dados[proximo] = dado
          else:
            self.dados[proximo] = dado

    def H1(self, k, tamanho):
      return k % tamanho
    
    def H2(self, anterior, tamanho):
      return (anterior + 1) % tamanho
    
    #operação para popular a hashtable, usando a funcao principal
    def __setitem__(self, k, dado):
      self.hashtable(k, dado)
