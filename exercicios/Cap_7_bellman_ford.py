"""
Algoritmo de Bellman-Ford para encontrar, partindo do vértice s,
o caminho de menor peso para cada vértice v do grafo.

Esse algoritmo admite arestas com pesos negativos e detecta
a existência de ciclos de peso negativo.
"""

import matplotlib.pyplot as plt
from auxiliares import mostraGrafoDirecionadoPeso, mostraGrafoDirecionadoPesoD, peso_aresta, florestaDeProfundidade

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

# Inicia todos os vértices
def Initialize_Single_Source(G, s):
  for v in G[0]:
    v.d = float('inf')
    v.pai = None
  s.d = 0

# Verifica numa aresta (u, v), se o menor caminho por essa aresta é menor que o caminho que v guarda atualmente
# Se sim, (u, v) passa a ser o novo caminho e u vira pai de v
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
  