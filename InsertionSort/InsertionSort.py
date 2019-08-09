from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

Comparacoes_ale = []
Comparacoes_pior = []

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def geraListaInvertida(tam):
    lista = []
    for i in range(tam, 0, -1):
      lista.append(i)
    return lista

def insertionSort(lista, pior_caso=False):
    comparacoes = 0

    for i in range(1, len(lista)):
        ind = i
        while(ind > 0 and lista[ind] < lista[ind-1]):
            lista[ind], lista[ind-1] = lista[ind-1], lista[ind]

            comparacoes += 1
            ind -= 1

    if(pior_caso):
        Comparacoes_pior.append(comparacoes)
    else:
        Comparacoes_ale.append(comparacoes)
    print(lista)
    
  
mpl.use('Agg')
  
def desenhaGrafico(x,y,y2,fileName,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Lista Aleatória")
    ax.plot(x,y2, label = "Pior Caso (Lista Invertida)")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(fileName)

x = [10000, 20000, 50000, 100000]
time_ale = []
time_pior = []

for i in x:
    setupTI = '''
from __main__ import insertionSort
from __main__ import geraLista
from __main__ import geraListaInvertida
'''
    time_ale.append(timeit.timeit("insertionSort(lista)", setup=setupTI+"lista=geraLista({})".format(i), number=1))
    time_pior.append(timeit.timeit("insertionSort(lista, True)", setup=setupTI+"lista=geraListaInvertida({})".format(i), number=1))

  
desenhaGrafico(x, time_ale, time_pior, "tempoXnumeros", "Tamanho da Lista", "Tempo de Ordenação")
desenhaGrafico(x, Comparacoes_ale, Comparacoes_pior, "comparacoesXnumeros", "Tamanho da Lista", "Número de Trocas")