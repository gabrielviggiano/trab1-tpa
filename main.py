from HashTable import *
from functools import lru_cache

#Neste trabalho usamos a distancia de levenshtein para encontrarmos palavras similares á palavras denominadas erradas, de acordo com o dicionario utilizado
#Este código foi baseado no seguinte artigo: https://towardsdatascience.com/text-similarity-w-levenshtein-distance-in-python-2f7478986e75
def levenshtein_distance(x, y):
  @lru_cache(None)
  def min_distance(letra1, letra2):
    if (letra1 == len(x)) or (letra2 == len(y)):
      return (len(x) - letra1) + (len(y) - letra2)
  
    if x[letra1] == y[letra2]:
      return min_distance(letra1 + 1, letra2 + 1)
    
    return 1 + min( min_distance(letra1, letra2 + 1), min_distance(letra1 + 1, letra2), min_distance(letra1 + 1, letra2 + 1) )
  
  return (min_distance(0,0))


#função para abrir arquivo do dicionario
def open_arq():
  arq = open("pt.dic", "r", encoding="utf8", errors="ignore")
  palavras = []
  print("Carregando Dicionário...\n")
  for linha in arq:
    linha = linha.strip().replace('\x00', '')
    palavras.append(linha)
  
  
  return palavras

#criando tabela hash com as palavras do dicionario
def cria_dicionario():
  hash = HashTable()
 
  palavras = open_arq()
  
  cont = 1
  for i in palavras:
    hash[cont] = i
    cont += 1
  
  return hash

#funcao que verifica se a palavra existe no dicionario
def corretor(palavra, dicionario):
  flag = False
  for palavra_dic in dicionario:
    if(palavra == palavra_dic):
      flag = True
  return flag

#funcao que procura palavras proximas à palavra digitada errada, e informa ao usuário as opções
def corrige(palavra, dicionario):
  for i in dicionario:
    corrigida = levenshtein_distance(palavra, i)
    if(corrigida == 1):
      print("A palavra", palavra, "não foi encontrada. Você quis dizer:", i, "?\n")

def main():
       
    dicionario = cria_dicionario()
    print("Dicionário carregado...\n")
    frase = list(input('Digite a frase: ').split())
    for palavra in frase:
      corret = corretor(palavra, dicionario.dados)
      if(corret == False):
        corrige(palavra, dicionario.dados)
    
if __name__ == "__main__":
    main()
