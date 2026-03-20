"""
Implementação do algoritmo de busca em profundidade (DFS) em um grafo direcionado
"""

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
  
def DFS(G):
  global tempo
  tempo = 0
  for v in G[0]:
    if v.cor == "white":
      DFSvisit(G, v)

def DFSvisit(G, u):
  global tempo
  tempo += 1
  u.d = tempo
  u.cor = "black"
  for v in adj[u]:
    if v.cor == 'white':
      v.pai = u
      DFSvisit(G, v)    
  tempo += 1
  u.f = tempo

# Cria a floresta do grafo
def florestaDeProfundidade(G):
  arvore = (G[0], [])
  for v in G[0]:
    if v.pai:
      arvore[1].append((v.pai, v))
  return arvore

# Main
def main(): 
  u = Vertice('u')
  v = Vertice('v')
  w = Vertice ('w')
  x = Vertice('x')
  y = Vertice('y')
  z = Vertice('z')

  V = (u, v, w, x, y, z)  # Vertices
  E = ((u,v), (u,x), (v,y), (w,y), (w,z), (x,v), (y,x), (z,z))  # Arestas
  G = (V, E)  # Grafo

  # Lista de adjacência
  global adj
  adj = {
    u: [v, x],
    v: [y],
    w: [y, z],
    x: [v],
    y: [x],
    z: [z]
  }

  DFS(G)
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

if __name__ == '__main__':
  main()