"""
Utiliza o algortimo do fecho transitivo para criar o grafo do fecho transitivo.
Um fecho transitivo de um grafo G = (V, E) será G* = (V, E*), onde
E* = {(i, j) se existe caminho de i a j em G}

A função fecho_transitivo(G, n) retorna a matriz T, onde T[i][j] indica se há ou não (True ou False)
caminho de i até j em G
"""

import matplotlib.pyplot as plt
from auxiliares import mostraGrafo
from tabulate import tabulate

class Vertice:
  # Construtor
  def __init__(self, nome):
    self.nome = nome

  # toString
  def __str__(self):
    return f"Número {self.nome}"

# Inicia a matriz T, onde cada elemento T[i][j] será True se
# i == j ou existir uma aresta direta de i para j; caso contrário, será False.
def inicia_T(G, n):
  T = [[None for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if i == j or (G[0][i], G[0][j]) in G[1]:
        T[i][j] = True
      else:
        T[i][j] = False
  return T

# Algoritmo do fecho transitivo
def fecho_transitivo(G, n):
  T = inicia_T(G, n)
  for k in range(n):
    for i in range(n):
      for j in range(n):

        # Verifica se existe um caminho entre i e j (passando por k ou não)
        T[i][j] = T[i][j] or (T[i][k] and T[k][j])

  return T

# A partir da matriz T cria o grafo do fecho transitivo
def cria_grafo_fecho_transitivo(G, T, n):
  Gfs = (G[0], [])
  for i in range(n):
    for j in range(n):
      if T[i][j]:
        Gfs[1].append((G[0][i], G[0][j]))

  return Gfs

def main():
  # Vértices
  zero = Vertice(0)
  um = Vertice(1)
  dois = Vertice(2)
  tres = Vertice(3)

  V = (zero, um, dois, tres)
  E = ((um, dois), (um, tres), (dois, um), (tres, zero), (tres, dois))
  G = (V, E)

  mostraGrafo(G, "Grafo inicial")

  # n = número de vértices
  T = fecho_transitivo(G, 4)
  Gfs = cria_grafo_fecho_transitivo(G, T, 4)

  mostraGrafo(Gfs, "Grafo do fecho transitivo")

  print("Tabela T:")
  print(tabulate(T, tablefmt="fancy_grid"))

  plt.show()

if __name__ == '__main__':
  main()
