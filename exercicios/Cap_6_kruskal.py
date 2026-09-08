"""
Algoritmo de Kruskal (guloso) para achar a árvore geradora mínima (AGM) de um grafo.

Uma árvore geradora de um grafo G contém todos os vértices de G e um subconjunto de suas arestas que mantém o grafo conexo e sem ciclos. Essa árvore tem necessariamente |V| - 1 arestas

Para essa árvore ser mínima, ela deve ainda ter a menor soma possível dos pesos de suas arestas.
"""

import matplotlib.pyplot as plt
import networkx as nx

# Define um vértice
class Vertice:

  # Construtor
  def __init__(self, nome):
    self.nome = nome
    self.pai = None
    self.rank = 0

  # toString
  def __str__(self):
    if self.pai == None:
      pai = "Nenhum"
    else:
      pai = self.pai.nome

    return f"""--------------------------------
    Nome do vértice: {self.nome}
    Vértice pai: {pai}
    Rank: {self.rank}"""

# Define v como raiz de seu componente
def make_set(v):
  v.pai = None
  v.rank = 0

# Devolve a raiz
def find_set(u):
  while u.pai != None:
    u = u.pai
  return u

# Liga uma raiz a outra - Transforma na mesma componente
def union(u, v):
  paiU = find_set(u)
  paiV = find_set(v)

  if paiU == paiV:
    return

  if paiU.rank < paiV.rank:
    paiU.pai = paiV

  elif paiU.rank > paiV.rank:
    paiV.pai = paiU

  else:
    paiV.pai = paiU
    paiU.rank += 1

# Algoritmo de Kruskal - Guloso
def AGM_Kruskal(G, w):
  A = []

  # O pai de todos os vertices vira None e rank vira 0
  for v in G[0]:
    make_set(v)

  # Cria uma lista das arestas
  arestas = [(u, v) for (u, v) in G[1]]

  # Ordena lista por ordem de peso crescente
  arestas = sorted(arestas, key=lambda aresta: w[aresta])

  peso = 0

  for (u, v) in arestas:
    if find_set(u) !=  find_set(v): # Se estão em componentes diferentes...
      A.append((u, v))              # ... pegar essa aresta
      union(u, v)                   # ... Unir na mesma componente
      peso += w[(u, v)]

  return A, peso

# Pega o peso de uma aresta. Essa função não é necessária no pseudocódigo
def peso_aresta(u, v, w):
  if (u, v) in w:
    return w[(u, v)]
  return w[(v, u)]

# Mostra grafo e os pesos
def mostraGrafoNaoDirecionadoPeso(G, nome, w):

  plt.figure()
  G_grafo = nx.Graph()

  G_grafo.add_nodes_from(
    [v.nome for v in G[0]]
  )

  G_grafo.add_edges_from(
    [(u.nome, v.nome) for (u, v) in G[1]]
  )

  pos = nx.kamada_kawai_layout(G_grafo)

  nx.draw(
    G_grafo,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="lightgreen"
  )

  # Pesos das arestas
  labels = {
    (u.nome, v.nome): peso_aresta(u, v, w)
    for (u, v) in G[1]
  }

  nx.draw_networkx_edge_labels(
    G_grafo,
    pos,
    edge_labels=labels
  )

  plt.get_current_fig_manager().set_window_title(nome)

def main():
  a = Vertice('a')
  b = Vertice('b')
  c = Vertice('c')
  d = Vertice('d')
  e = Vertice('e')
  f = Vertice('f')
  g = Vertice('g')
  h = Vertice('h')
  i = Vertice('i')

  V = (a, b, c, d, e, f, g, h, i)
  E = ((a, b), (a, h), (b, h), (b, c), (c, i), (h, i), (g, i), (g, h), (c, f), (c, d), (d, e), (d, f), (e, f), (g, f))
  G = (V, E)

  # Pesos
  w = {
    (a, b): 4,
    (a, h): 8,
    (b, h): 11,
    (b, c): 8,
    (c, i): 2,
    (h, i): 7,
    (g, i): 6,
    (g, h): 1 ,
    (c, f): 4,
    (c, d): 7,
    (d, e): 9,
    (d, f): 14,
    (e, f): 10,
    (g, f): 2
  }

  mostraGrafoNaoDirecionadoPeso(G, "Grafo", w)

  arestas, peso = AGM_Kruskal(G, w)

  mostraGrafoNaoDirecionadoPeso((V, arestas), f"AGM do grafo - Peso total = {peso}", w)
  plt.show()

if __name__ == '__main__':
  main()
  