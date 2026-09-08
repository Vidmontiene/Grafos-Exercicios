"""
Implementação do algoritmo de busca em largura (BFS), que encontra o menor caminho entre dois vértices de um grafo ordenado, além de retornar uma árvore para melhor visualização
"""

import networkx as nx
import matplotlib.pyplot as plt

# Define um vértice
class Vertice:

  # Construtor
  def __init__(self, nome):
    self.nome = nome
    self.pai = None
    self.d = float('inf')
    self.cor = "white"

  # toString
  def __str__(self):
    if self.pai == None:
      pai = "Nenhum"
    else:
      pai = self.pai.nome

    return f"""--------------------------------
Nome do vértice: {self.nome}
Vértice pai: {pai}
Distância da raiz: {self.d}
Cor: {self.cor}"""

# Busca em Largura, retorna o grafo da árvore
def BFS (G, s, adj):

  # Define as configurações do primeiro vértice
  s.cor = "gray"
  s.d = 0

  vertices = G[0]
  
  fila = [s]
  arvore = ([s], [])

  while fila != []:
    u = fila.pop(0)
    for v in adj[u]:
      if v.cor == "white":
        fila.append(v)
        arvore[0].append(v)
        arvore[1].append((u, v))
        v.cor = "gray"
        v.pai = u
        v.d = u.d + 1

  return arvore

# Main
def main():
  a = Vertice("a")
  b = Vertice("b")
  c = Vertice("c")
  d = Vertice("d")
  e = Vertice("e")

  V = (a, b, c, d, e) # Vértices
  E = ((a, b), (a, c), (c, d), (c, e))  # Arestas
  G = (V, E) # Grafo

  adj = {
    a: [b, c],
    b: [],
    c: [d, e],
    d: [],
    e: []
  }

  arvore = BFS(G, a, adj) # Chama a função

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

  # Usa networkx e matplotlib para mostrar a árvore
  G_arvore = nx.DiGraph()
  G_arvore.add_edges_from(
    [(u.nome, v.nome) for (u, v) in arvore[1]]
  )
  pos = nx.spring_layout(G_arvore)

  nx.draw(
    G_arvore,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="lightgreen",
    arrows=True
  )
  plt.show()

if __name__ == '__main__':
  main()
