"""
Implementação do algoritmo de busca em profundidade (DFS) em um grafo direcionado
"""

import networkx as nx
import matplotlib.pyplot as plt

# Define um vértice
class Vertice:

  # Construtor
  def __init__(self, nome):
    self.nome = nome
    self.pai = None
    self.cor = "white"
    self.d = 0
    self.f = 0

  # toString
  def __str__(self):
    if self.pai == None:
      pai = "Nenhum"
    else:
      pai = self.pai.nome

    return f"""--------------------------------
Nome do vértice: {self.nome}
Vértice pai: {pai}
Cor: {self.cor}
Tempo de descoberta: {self.d}
Tempo de término: {self.f}"""
  
def DFS(G, adj):
  global tempo
  tempo = 0
  for v in G[0]:
    if v.cor == "white":
      DFSvisit(G, v, adj)

def DFSvisit(G, u, adj):
  global tempo
  tempo += 1
  u.d = tempo
  u.cor = "gray"
  for v in adj[u]:
    if v.cor == 'white':
      v.pai = u
      DFSvisit(G, v, adj)    
  tempo += 1
  u.f = tempo
  u.cor = "black"

# Cria a floresta do grafo
def florestaDeProfundidade(G):
  arvore = (G[0], [])
  for v in G[0]:
    if v.pai:
      arvore[1].append((v.pai, v))
  return arvore

# Usa networkx e matplotlib para mostrar a árvore
def mostraGrafo(G, nome):
  plt.figure()
  
  G_grafo = nx.DiGraph()

  G_grafo.add_nodes_from(
    [v.nome for v in G[0]]
  )
  
  G_grafo.add_edges_from(
    [(u.nome, v.nome) for (u, v) in G[1]]
  )
  pos = nx.spring_layout(G_grafo, k=0.5)

  nx.draw(
    G_grafo,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="lightgreen",
    arrows=True
  )
  plt.get_current_fig_manager().set_window_title(nome)

# Main
def main(): 
  a = Vertice('a')
  b = Vertice('b')
  c = Vertice ('c')
  d = Vertice('d')
  e = Vertice('e')
  f = Vertice('f')

  V = (a, b, c, d, e, f)  # Vertices
  E = ((a,b), (a,d), (b,e), (c,e), (c,f), (d,b), (e,d), (f,f))  # Arestas
  G = (V, E)  # Grafo

  # Lista de adjacência
  adj = {
    a: [b, d],
    b: [e],
    c: [e, f],
    d: [b],
    e: [d],
    f: [f]
  }

  DFS(G, adj)
  arvore = florestaDeProfundidade(G)

  # Printa as informações dos vertices
  for vertice in G[0]:
    print(vertice)
  print("--------------------------------")

  # Printa a árvore
  print("Vértices da árvore:")
  print([v.nome for v in arvore[0]])
  print("Arestas da árvore:")
  print([(u.nome, v.nome) for (u,v) in arvore[1]])
  print("--------------------------------")

  mostraGrafo(G, "Grafo Inicial")
  mostraGrafo(arvore, "Floresta de Profundidade - Após DFS")
  plt.show()

if __name__ == '__main__':
  main()
  