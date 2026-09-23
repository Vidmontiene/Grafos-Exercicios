"""
Algoritmo de Dijkstra para encontrar, partindo do vértice s,
o caminho de menor peso para cada vértice v do grafo.

Esse algoritmo exige pesos não negativos, ou seja, não pode conter arestas de peso < 0
"""

import matplotlib.pyplot as plt
from auxiliares import mostraGrafoDirecionadoPeso, mostraGrafoDirecionadoPesoD, peso_aresta, florestaDeProfundidade
from Cap_7_bellman_ford import relax, Initialize_Single_Source

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

# Algoritmo de Dijkstra
def Dijkstra(G, w, s, adj):
  Initialize_Single_Source(G, s)
  S = []
  Q = list(G[0]) # Idealmente, aqui seria uma heap

  while Q != []:
    u = min(Q, key=lambda v: v.d) # Pega o vértice de menor .d
    Q.remove(u)
    S.append(u)
    for v in adj[u]:
      if relax(u, v, w):  # Relaxa todas as arestas que saem de u
        None # Aqui atualizaria a heap

def main():
  # Declaração dos vértices
  s = Vertice('s')
  t = Vertice('t')
  x = Vertice('x')
  y = Vertice('y')
  z = Vertice('z')

  V = (s, t, x, y, z)
  E = ((s, t), (s, y), (t, y), (y, t), (t, x), (y, x), (y, z), (z, x), (x, z), (z, s))
  G = (V, E)

  w = {
    (s, t): 10,
    (s, y): 5,
    (t, y): 2,
    (y, t): 3,
    (t, x): 1,
    (y, x): 9,
    (y, z): 2,
    (z, x): 4,
    (x, z): 6,
    (z, s): 7
  }

  adj = {
    s: [t, y],
    t: [y, x],
    x: [z],
    y: [t, x, z],
    z: [x, s]
  }

  mostraGrafoDirecionadoPeso(G, "Grafo Original", w)
  Dijkstra(G, w, s, adj)
  c = florestaDeProfundidade(G)
  mostraGrafoDirecionadoPesoD(c, "Caminho mínimo", w)
  plt.show()

if __name__ == '__main__':
  main()
