"""
Implementação do algoritmo de busca em profundidade (DFS) em um grafo direcionado
"""

import matplotlib.pyplot as plt
from auxiliares import mostraGrafo, florestaDeProfundidade

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
  