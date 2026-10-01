"""
Algoritmo de Johnson para encontrar o caminho mais curto entre
qualquer par de vértices, dado a lista de pesos.

O algoritmo retorna a matriz D, onde o elemento D[i][j] representa 
a distância de menor peso partindo do vértice i até o vértice j, ou informa se o grafo contém um ciclo negativo.

O algoritmo é recomendado para grafos esparsos (com poucas arestas em relação ao número máximo possível de arestas).
"""

import matplotlib.pyplot as plt
from auxiliares import peso_aresta, mostraGrafoDirecionadoPeso, mostraGrafoDirecionadoPesoD
from tabulate import tabulate
from Cap_7_bellman_ford import Bellman_Ford
from Cap_7_dijkstra import Dijkstra

# Define um vértice
class Vertice:

  # Construtor
  def __init__(self, nome):
    self.nome = nome
    self.pai = None
    self.d = float('inf')

  # toString
  def __str__(self):
    if self.pai == None:
      pai = "Nenhum"
    else:
      pai = self.pai.nome

    return f"""--------------------------------
    Nome do vértice: {self.nome}
    Vértice pai: {pai}
    d: {self.d}"""

# Algoritmo de Johnson
def Johnson(G, w, adj):

  # Cria novo vértice s
  s = Vertice('s')

  # Cria o grafo Gl, que contém todos os vértices de G, + s
  # Todas as arestas de G, + (s, v) para cada vértice v em G
  # O peso das novas arestas criadas é zero
  Gl = ([], [(u, v) for (u, v) in G[1]])
  for v in G[0]:
    Gl[0].append(v)
    Gl[1].append((s, v))
    w[(s, v)] = 0
  Gl[0].append(s)

  # Procura ciclo negativo
  if Bellman_Ford(Gl, w, s) == False:
    print("O grafo contém um ciclo de peso negativo.")
    return False, False

  # Para visualizar a o gráfico Gl após o Bellman_Ford:
  mostraGrafoDirecionadoPesoD(Gl, "Grafo G' após Bellman_Ford", w)

  # Associa cada vértice ao seu índice na matriz 
  # Essa seção não é necessária no algoritmo original, mas necessária para acessar a matriz corretamente
  indices = {}
  for i, v in enumerate(G[0]):
    indices[v] = i

  h = {}
  wc = {}

  # Guarda o menor peso possível de um caminho de s até v para cada v no Grafo Gl
  for v in Gl[0]:
    h[v] = v.d

  # Repondera as arestas para que seus pesos sejam não negativos
  for (u, v) in Gl[1]:
    wc[(u, v)] = peso_aresta(u, v, w) + h[u] - h[v]

  n = len(G[0]) # Número de vértices
  D = [[None for _ in range(n)] for _ in range(n)]  # Matriz n X n

  # Executa Dijkstra a partir de cada vértice e converte as distâncias reponderadas de volta para os pesos originais
  for u in G[0]:
    Dijkstra(G, wc, u, adj)
    for v in G[0]:
      i = indices[u]
      j = indices[v]
      D[i][j] = v.d + h[v] - h[u] # Converte de volta

  return D, wc # Só precisa retornar D, wc é para visualização

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

  # Adjuntos
  adj = {
    zero: [um, dois, quatro],
    um: [tres, quatro],
    dois: [um],
    tres: [zero, dois],
    quatro: [tres]
  }

  D, wc = Johnson(G, w, adj) 

  if not D:
    return
  
  print("Menor peso entre i e j:")
  print(tabulate(D, tablefmt="fancy_grid"))

  mostraGrafoDirecionadoPeso(G, "Grafo inical", w)
  mostraGrafoDirecionadoPeso(G, "Grafo G com pesos wc", wc)
  plt.show()

if __name__ == '__main__':
  main()
