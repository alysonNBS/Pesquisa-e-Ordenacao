from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

def geraListaInvertida(tam):
    return list(range(tam, 0, -1))

def quickSort(lista):
  if(len(lista) == 0):
    return []
  
  pivo = lista[len(lista)//2]

  list_esq = []
  list_dir = []

  for x in lista:
    if(x < pivo):
      list_esq.append(x)
    elif(x > pivo):
      list_dir.append(x)
  
  return quickSort(list_esq) + [pivo] + quickSort(list_dir)

mpl.use('Agg')
  
def desenhaGrafico(x,y,fileName,xl = "Entradas", yl = "SaÃ­das"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Lista Invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(fileName)

x = [100000, 200000, 400000, 500000, 1000000, 2000000]
time = []

for i in x:
    setupTI = '''
from __main__ import geraListaInvertida
from __main__ import quickSort
'''
    time.append(timeit.timeit("quickSort(lista)", setup=setupTI+"lista=geraListaInvertida({})".format(i), number=1))

  
desenhaGrafico(x, time, "tempoXnumeros", "Tamanho da Lista", "Tempo de Ordenação")
