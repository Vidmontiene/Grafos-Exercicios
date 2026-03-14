"""
Implementação do algoritmo de busca em largura (BFS), que encontra o menor caminho entre dois vértices de um grafo, além de retornar uma árvore para melhor visualização
"""

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

# Indica se dois vértices formam uma aresta em um grafo
def isAresta(G, v1, v2):
  return ((v1, v2) in G[1] or (v2, v1) in G[1])

# Busca em Largura, retorna o grafo da árvore
def BFS (G, s):

  # Define as configurações do primeiro vértice
  s.cor = "gray"
  s.d = 0

  vertices = G[0]
  
  fila = [s]
  arvore = ([s], [])

  while fila != []:
    u = fila.pop()
    for v in vertices:
      if isAresta(G, v, u) and v.cor == "white":
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
  E = ((a, b), (a, c), (c, d), (c, e))  #Arestas
  G = (V, E) #Grafo

  arvore = BFS(G, a) # Chama a função

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