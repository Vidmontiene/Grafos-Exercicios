"""
Encontra quantas componentes conexas um grafo tem, bem como quais vértices pertencem a cada componente
"""

from Cap_5_ciclo import mostraGrafoNaoDirecionado
import matplotlib.pyplot as plt

# Define um vértice
class Vertice:

  # Construtor
  def __init__(self, nome):
    self.nome = nome
    self.cor = "white"
    self.pai = None
    self.cc = 0

  # toString
  def __str__(self):

    if self.pai == None:
      pai = "Nenhum"
    else:
      pai = self.pai.nome

    return f"""--------------------------------
    Nome do vértice: {self.nome}
    Cor: {self.cor}
    Pai: {pai}
    Componente: {self.cc}"""

def ComponentesConexas(G, adj):
  k = 0

  for u in G[0]:
    if u.cor == 'white':
      k += 1
      VisitaCC(G, u, adj, k)
  return k

def VisitaCC(G, u, adj, k):
  u.cor = "gray"
  u.cc = k
  for v in adj[u]:
    if v.cor == 'white':
      v.pai = u
      VisitaCC(G, v, adj, k)
  u.cor = "black"

def main():
  a = Vertice('a')
  b = Vertice('b')
  c = Vertice('c')
  d = Vertice('d')
  e = Vertice('e')
  f = Vertice('f')
  g = Vertice('g')
  h = Vertice('h')

  V = (a, b, c, d, e, f, g, h)
  E = ((a,b), (b,c), (c,a), (c,d), (d,e), (e,f), (f, d), (g,h))
  G = (V, E)

  # Lista de adjacência
  adj = {
    a: [b, c],
    b: [a, c],
    c: [a, b, d],
    d: [c, e, f],
    e: [d, f],
    f: [d, e],
    g: [h],
    h: [g]
  }

  componentes_conexas = ComponentesConexas(G, adj)

  # Printa as informações dos vertices
  print(f"O grafo tem {componentes_conexas} componentes conexas")
  for vertice in G[0]:
    print(vertice)
  print("--------------------------------")

  mostraGrafoNaoDirecionado(G, "Grafo")
  plt.show()

if __name__ == '__main__':
  main()