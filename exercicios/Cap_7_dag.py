"""
Algoritmo para encontrar, partindo do vértice s, o caminho de menor peso para cada vértice v do grafo.
O algoritmo processa os vértices em ordem topológica, relaxando as arestas que saem de cada um.
Esse algoritmo exige grafos acícilicos e direcionados, para que a ordenação topológica seja possível.
"""

import matplotlib.pyplot as plt
from Cap_7_bellman_ford import relax, Initialize_Single_Source
from auxiliares import mostraGrafoDirecionadoPeso, mostraGrafoDirecionadoPesoD, peso_aresta, florestaDeProfundidade
from Cap_4_ordenacao_topologica import Vertice
import Cap_4_ordenacao_topologica as dfs

# Algoritmo
def dag_shortest_path(G, w, s, adj):

  # Ordena topológicamente
  dfs.pilha = []
  dfs.DFS(G, adj)
  pilha = dfs.pilha[::-1]
  print([v.nome for v in pilha])

  # Reinicia vértices
  Initialize_Single_Source(G, s)

  # Relaxa cada vértice que sai de cada elemento da pilha
  for u in pilha:
    for v in adj[u]:
      relax(u, v, w)

def main():
  
  # Vértices
  r = Vertice('r')
  s = Vertice('s')
  t = Vertice('t')
  x = Vertice('x')
  y = Vertice('y')
  z = Vertice('z')

  V = (r, s, t, x, y, z)
  E = ((r, s), (r, t), (s, t), (s, x), (t, x), (t, y), (t, z), (x, y), (x, z), (y, z ))
  G = (V, E)

  w = {
    (r, s): 5,
    (r, t): 3,
    (s, t): 2,
    (s, x): 6,
    (t, x): 7,
    (t, y): 4,
    (t, z): 2,
    (x, y): -1,
    (x, z): 1,
    (y, z): -2
  }

  adj = {
    r: [s, t],
    s: [t, x],
    t: [x, y, z],
    x: [y, z],
    y: [z],
    z: []
  }

  dag_shortest_path(G, w, s, adj)
  c = florestaDeProfundidade(G)

  mostraGrafoDirecionadoPeso(G, "Grafo Original", w)
  mostraGrafoDirecionadoPesoD(c, "Caminho mínimo", w)
  plt.show()

if __name__ == '__main__':
  main()
