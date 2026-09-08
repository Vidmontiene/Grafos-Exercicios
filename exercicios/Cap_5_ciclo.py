"""
Usa DFS para detectar ciclos em um grafo não direcionado.
"""

from Cap_3_dfs import Vertice
import networkx as nx
import matplotlib.pyplot as plt

def TemCiclo(G, adj):
  for v in G[0]:
    if v.cor == "white":
      if VisitaCiclo(G, v, adj):
        return True
  return False

def VisitaCiclo(G, u, adj):
  u.cor = "gray"
  for v in adj[u]:
    if v.cor == 'white':
      v.pai = u
      if VisitaCiclo(G, v, adj):
        return True
    elif u.pai != v:
      return True 
  u.cor = "black"
  return False

def mostraGrafoNaoDirecionado(G, nome):
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

  plt.get_current_fig_manager().set_window_title(nome)

def main():
  a = Vertice('a')
  b = Vertice('b')
  c = Vertice ('c')
  d = Vertice('d')
  e = Vertice('e')
  f = Vertice('f')

  V = (a, b, c, d, e, f)  # Vertices
  E = ((a,b), (b,c), (c,a), (c,d), (d,f), (d,e), (e,f)) # Arestas
  G = (V, E)  # Grafo

  # Lista de adjacência
  adj = {
    a: [b, c],
    b: [a, c],
    c: [a, b, d],
    d: [c, e, f],
    e: [d, f],
    f: [d, e]
  }

  tem_ciclo = TemCiclo(G, adj)
  mostraGrafoNaoDirecionado(G, f"Esse grafo {"tem" if tem_ciclo else "não tem"} ciclo")
  plt.show()

if __name__ == '__main__':
  main()
  