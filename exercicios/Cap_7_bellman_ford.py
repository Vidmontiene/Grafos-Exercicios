"""
Algoritmo de Bellman-Ford para encontrar, partindo do vértice s,
o caminho de menor peso para cada vértice v do grafo.

Esse algoritmo admite arestas com pesos negativos e detecta
a existência de ciclos de peso negativo.
"""

from Cap_6_kruskal import peso_aresta
from Cap_3_dfs import florestaDeProfundidade
import matplotlib.pyplot as plt
import networkx as nx

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

# Mostra grafo e os pesos
def mostraGrafoDirecionadoPeso(G, nome, w):

  plt.figure()
  G_grafo = nx.DiGraph()

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
    node_color="lightgreen",
    arrows = True
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

# Mostra grafo direcionado, pesos e d dos vértices
def mostraGrafoDirecionadoPesoD(G, nome, w):

  plt.figure()

  G_grafo = nx.DiGraph()

  G_grafo.add_nodes_from(
    [v.nome for v in G[0]]
  )

  G_grafo.add_edges_from(
    [(u.nome, v.nome) for (u, v) in G[1]]
  )

  pos = nx.kamada_kawai_layout(G_grafo)

  # Desenha os vértices e as arestas
  nx.draw(
    G_grafo,
    pos,
    with_labels=False,
    node_size=1000,
    node_color="lightgreen",
    arrows=True
  )

  # Nome e valor de d dos vértices
  labels_vertices = {
    v.nome: f"{v.nome}\n(d={v.d})"
    for v in G[0]
  }

  nx.draw_networkx_labels(
    G_grafo,
    pos,
    labels=labels_vertices
  )

  # Pesos das arestas
  labels_arestas = {
    (u.nome, v.nome): peso_aresta(u, v, w)
    for (u, v) in G[1]
  }

  nx.draw_networkx_edge_labels(
    G_grafo,
    pos,
    edge_labels=labels_arestas
  )

  plt.get_current_fig_manager().set_window_title(nome)

  plt.show()

# Inicia todos os vértices
def Initialize_Single_Source(G, s):
  for v in G[0]:
    v.d = float('inf')
    v.pai = None
  s.d = 0

# Verifica numa aresta (u, v), se o menor caminho por essa aresta é menor que o caminho que v guarda atualmente
# Se sim, (u, v) passa a ser o novo caminho
def relax(u, v, w):
  if v.d > (novo := u.d + peso_aresta(u, v, w)):
    v.d = novo
    v.pai = u
    return True
  return False

# Algoritmo de Bellman-Ford. Retorna false se existe um ciclo de peso negativo alcançável a partir da fonte; caso contrário, retorna true e produz os caminhos mínimos e seus pesos
def Bellman_Ford(G, w, s):
  Initialize_Single_Source(G, s)

  for i in range(1, len(G[0])):
    for (u, v) in G[1]:
      relax(u, v, w)

  # Aqui, o número máximo de relaxamentos foi feito, se houver algum outro, há um ciclo negativo
  for (u, v) in G[1]:
    if v.d > u.d + peso_aresta(u, v, w):
      return False
  return True

def main():
  # Vértices
  s = Vertice('s')
  t = Vertice('t')
  x = Vertice('x')
  y = Vertice('y')
  z = Vertice('z')

  V = (s, t, x, y, z)

  # Arestas
  E = ((t, x),(t, y),(t, z),(x,t),(y, x),(y, z),(z, x),(z,s),(s,t),(s, y))

  # Grafo
  G = (V, E)

  # Lista de pesos
  w = {
    (s, t): 6,
    (s, y): 7,
    (t, x): 5,
    (x, t): -2,
    (t, y): 8,
    (t, z): -4,
    (x, y): -3,
    (y, z): 9,
    (z, x): 7,
    (z, s): 2
  }

  mostraGrafoDirecionadoPeso(G, "Grafo original", w)
  if Bellman_Ford(G, w, s):
    caminho = florestaDeProfundidade(G)
    mostraGrafoDirecionadoPesoD(caminho, "Caminho mínimo", w)

  plt.show()

if __name__ == '__main__':
  main()
  