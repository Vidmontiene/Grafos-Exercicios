"""
Algoritmo de ordenação topológica. Deve ser utilizado num grafo acícilico e direcionado. Ordena todos os vértices tal que se (u, v) é uma aresta, então u aparece antes de v na ordenação.
"""

from dfs import Vertice, mostraGrafo, florestaDeProfundidade
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

def main():

  # Vértices
  meia = Vertice('meia')
  cueca = Vertice('cueca')
  calca = Vertice ('calça')
  sapato = Vertice('sapato')
  relogio = Vertice('relogio')
  camisa = Vertice('camisa')
  cinto = Vertice('cinto')
  gravata = Vertice('gravata')
  paleto = Vertice('paletó')

  V = (meia, cueca, calca, sapato, camisa, cinto, gravata, paleto, relogio)  # Vértices
  E = ( # Arestas
    (camisa, gravata), 
    (camisa, cinto), 
    (gravata, paleto), 
    (cueca, calca), 
    (cueca, sapato), 
    (calca, cinto), 
    (calca, sapato), 
    (meia, sapato)
  )  
  G = (V, E)  # Grafo

  # Lista de adjacência
  adj = {
    camisa: [gravata, sapato],
    gravata: [paleto],
    cueca: [calca, sapato],
    calca: [cinto, sapato],
    meia: [sapato],
    sapato: [],
    cinto: [],
    paleto: [],
    relogio: []
  }

  # Cria pilha
  global pilha
  pilha = []

  DFS(G, adj)

  # Printa a pilha ordenada
  for peca in pilha[::-1]:
    print(peca.nome)

  # Mostra grafos
  floresta = florestaDeProfundidade(G)
  mostraGrafo(G, "Grafo inicial")
  mostraGrafo(floresta, "Floresta de Profundidade")
  
  plt.show()

if __name__ == '__main__':
  main()
