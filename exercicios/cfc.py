"""
Algoritmo que encontra as componentes fortementes conexas de um grafo direcionado.
Cria uma floresta na qual cada árvore é uma CFC (Componente fortemente conexa)
"""

from dfs import Vertice, mostraGrafo, DFS as DFS_sem_pilha, florestaDeProfundidade
import matplotlib.pyplot as plt

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
  u.cor = "black"
  for v in adj[u]:
    if v.cor == 'white':
      v.pai = u
      DFSvisit(G, v, adj)    
  tempo += 1
  u.f = tempo
  pilha.append(u)

# Calcula o grafo transposto de G (inverte arestas):
def tranposto(G, adj):
  Vt = pilha[::-1]  # Ordena os vértices por ordem decrescente de f
  At = []
  A = G[1]

  # Inverte arestas
  for (u, v) in A:
    At.append((v, u))

  Gt = (Vt, At) # Grafo transposto

  # Cria adj de Gt
  adjt = {}
  for vertice, lista in adj.items():
    for v in lista:
      if v in adjt:
        adjt[v].append(vertice)
      else:
        adjt[v] = [vertice]

  return Gt, adjt
    
def main():

  a = Vertice('a')
  b = Vertice('b')
  c = Vertice('c')
  d = Vertice('d')
  e = Vertice('e')
  f = Vertice('f')
  g = Vertice('g')
  h = Vertice('h')

  V = (a, b, c, d, e, f, g, h) # Vértices
  E = ((a, b), (b, a), (g, a), (g, e), (e, f), (f, g), (g, c), (c, d), (d, c), (d, h), (b, h)) # Arestas
  G = (V, E) # Grafo

  # Lista de adjacência
  adj = {
    a: [b],
    b: [a, h],
    c: [d],
    d: [c, h],
    e: [f],
    f: [g],
    g: [a, c, e],
    h: []
  }

  global pilha
  pilha= []

  # Primeiro DFS, cria pilha
  DFS(G, adj)

  Gt, adjt = tranposto(G, adj)

  # Reseta vertices
  for v in Gt[0]:
    v.cor = "white"
    v.pai = None

  # Segundo DFS, segue com base nos vértices da pilha
  DFS_sem_pilha(Gt, adjt)

  # Cria a floresta, cada árvore é uma componente fortemente conexa
  componentes = florestaDeProfundidade(Gt)
  mostraGrafo(G, 'Grafo inicial')
  mostraGrafo(componentes, "Componentes Fortemente Conexas")
  plt.show()

if __name__== '__main__':
  main()
