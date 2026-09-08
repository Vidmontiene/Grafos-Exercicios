"""
Algoritmo de Prim para achar a árvore geradora mínima (AGM) de um grafo.

Uma árvore geradora de um grafo G contém todos os vértices de G e um subconjunto de suas arestas que mantém o grafo conexo e sem ciclos. Essa árvore tem necessariamente |V| - 1 arestas

Para essa árvore ser mínima, ela deve ainda ter a menor soma possível dos pesos de suas arestas.
"""

from Cap_6_kruskal import mostraGrafoNaoDirecionadoPeso
import matplotlib.pyplot as plt

# Define um vértice
class Vertice:

  # Construtor
  def __init__(self, nome):
    self.nome = nome
    self.pai = None
    self.key = float('inf')

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

# Pega o peso de uma aresta. Essa função não é necessária no pseudocódigo
def peso_aresta(u, v, w):
  if (u, v) in w:
    return w[(u, v)]
  return w[(v, u)]

def AGM_Prim(G, adj, w, r):
  r.key = 0

  Q = [u for u in G[0]]  # Idealmente, aqui seria usada uma heap, mas python não permite atualizar heaps, então vamos usar listas

  while Q != []:
    u = min(Q, key=lambda v: v.key) # Pega o vértice de menor key
    Q.remove(u)
    for v in adj[u]:
      if v in Q and peso_aresta(u, v, w) < v.key:
        v.pai = u
        v.key = peso_aresta(u, v, w)
        # Aqui atualizaria a heap -> Decrease-Key(Q, v, w(u,v))

# Cria a AGM e também retorna o peso
def cria_AGM(G, w):
  A = (G[0], [])
  peso = 0

  for u in G[0]:
    if u.pai:
      A[1].append((u.pai, u))
      peso += peso_aresta(u.pai, u, w)

  return A, peso

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

  # Lista de adjacência
  adj = {
    a: [b, h],
    b: [a, c, h],
    c: [b, d, f, i],
    d: [c, e],
    e: [d, f],
    f: [c, e, g],
    g: [f, h, i],
    h: [a, b, g, i],
    i: [c, g, h]
  }

  AGM_Prim(G, adj, w, a)
  agm, peso = cria_AGM(G, w)

  mostraGrafoNaoDirecionadoPeso(G, "Grafo", w)
  mostraGrafoNaoDirecionadoPeso(agm, f"AGM do grafo - Peso total = {peso}", w)
  plt.show()

if __name__ == '__main__':
  main()
  