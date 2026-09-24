"""
Algoritmo de Floyd-Warshall para encontrar o caminho mais curto entre
qualquer par de vértices, dada a matriz de pesos.

O algoritmo retorna a matriz D, onde o elemento D[i][j] representa
a distância de menor peso partindo do vértice i até o vértice j.

Também retorna a matriz P, onde o elemento P[i][j] representa o
predecessor do vértice j no caminho de menor peso partindo do vértice
i até j.
"""

import matplotlib.pyplot as plt
from auxiliares import caminho_mais_curto, mostraGrafoDirecionadoPeso
from tabulate import tabulate

class Vertice:
  # Construtor
  def __init__(self, nome):
    self.nome = nome

  # toString
  def __str__(self):
    return f"Número {self.nome}"

# Inicializa a matriz P
# A diagonal e as arestas que não existem são nulas
# O restante é i 
def inicia_P(n, W):
  P = [[None for _ in range(5)] for _ in range(5)]
  for i in range(n):
    for j in range(n):
      if i == j or W[i][j] == float('inf'): 
        P[i][j] = None
      elif i != j:
        P[i][j] = i

  return P

# Algoritmo de Floyd-Warshall
def floyd_warshall(W, n):
  D = W
  P = inicia_P(n, W)
  for k in range(n):
    for i in range(n):
      for j in range(n):

        # Se não fosse necessário saber a matriz P, bastava adicionar:
        # D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        # E ignorar os condicionais a seguir:

        # O caminho por k é menor do que o caminho que tenho atualmente?
        if D[i][j] > (soma_k := D[i][k] + D[k][j]): 
          D[i][j] = soma_k
          P[i][j] = P[k][j]
        else: # essa parte não é necessária, mas deixa claro
          D[i][j] = D[i][j]
          P[i][j] = P[i][j]

  # Detecta se há ciclo negativo
  for i in range(n):
    if D[i][i] < 0:
      return False, False
  return D, P

def main():
  # Vértices
  zero = Vertice(0)
  um = Vertice(1)
  dois = Vertice(2)
  tres = Vertice(3)
  quatro = Vertice(4)

  V = (zero, um, dois, tres, quatro)

  # Arestas
  E = ( (zero, um), (zero, dois), (zero, quatro), (um, tres), (um, quatro), (dois, um), (tres, zero), (tres, dois), (quatro, tres))

  G = (V, E)

  # Pesos
  w = {
    (zero, um): 3,
    (zero, dois): 8,
    (zero, quatro): -4,
    (um, tres): 1,
    (um, quatro): 7,
    (dois, um): 4,
    (tres, zero): 2,
    (tres, dois): -5,
    (quatro, tres): 6
  }

  # Matriz de pesos
  # Cada elemento wij dessa matriz é o peso da aresta (i, j)
  # Caso essa aresta não exista, o peso é infinito
  W = [
    [           0,            3,            8, float('inf'),           -4],
    [float('inf'),            0, float('inf'),            1,            7],
    [float('inf'),            4,            0, float('inf'), float('inf')],
    [           2, float('inf'),           -5,            0, float('inf')],
    [float('inf'), float('inf'), float('inf'),            6,            0]
  ]

  D, P = floyd_warshall(W, 5)

  if D == False:
    print('Há um ciclo negativo no grafo. Não foi possível aplicar o algoritmo.')
    return

  mostraGrafoDirecionadoPeso(G, "Grafo", w)
  plt.show(block=False)

  # Printa tabelas
  print("Menor peso entre i e j:")
  print(tabulate(D, tablefmt="fancy_grid"))
  print('-=' * 50)
  print("Pai de j no caminho até i: ")
  print(tabulate(P, tablefmt="fancy_grid", headers="Teste"))

  # Perguntas de menor caminho
  while True: 
    r = input("Deseja saber caminho entre algum vértice? [S/N] ").strip()
    if r.lower() == 'n':
      break
    l = input("Partindo de _ e chegando em _ (Separe com espaço) ").split()
    inicio, fim = int(l[0]), int(l[1])
    caminho_mais_curto(P, inicio, fim)
    
if __name__ == "__main__":
  main()
