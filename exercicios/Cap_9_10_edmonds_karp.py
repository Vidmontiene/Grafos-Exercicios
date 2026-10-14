""" 
Implementa o algoritmo de Edmonds-Karp para encontrar o fluxo máximo em uma rede de fluxo. 

O algoritmo utiliza busca em largura (BFS) para encontrar caminhos aumentantes no grafo residual. A cada iteração, calcula a capacidade residual mínima do caminho encontrado e atualiza o fluxo das arestas, aumentando-o nas arestas originais e diminuindo-o quando o caminho utiliza arestas residuais reversas. 

O processo se repete até que não exista mais um caminho aumentante entre a origem e o destino. Ao final, retorna o grafo com os fluxos calculados.
"""

from Cap_2_bfs import BFS
from auxiliares import mostraGrafoFluxo, encontrar_aresta, capacidade_residual
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

# Define uma aresta
class Aresta:

  # Construtor
  def __init__(self, v1, v2, capacidade):
    self.aresta = (v1, v2)
    self.capacidade = capacidade
    self.f = 0

# Cria grafo residual e sua lista de adjacência e reseta vertices
def cria_grafo_residual(G):
  Gf = (G[0], [])

  for v in G[0]:
    v.cor = 'white'
    v.pai = None
    v.d = float('inf')

  # Cria a lista de adjacência da rede residual
  adj_residual = {v: [] for v in G[0]}

  for aresta in G[1]:
    u, v = aresta.aresta

    # Aresta original
    if aresta.capacidade - aresta.f > 0:
      adj_residual[u].append(v)
      Gf[1].append((u, v))

    # Aresta reversa
    if aresta.f > 0:
      adj_residual[v].append(u)
      Gf[1].append((v, u))

  return Gf, adj_residual

# Retorna caminho de s a t
def encontra_caminho(s, t):
  # Reconstrói o caminho
  caminho = []
  atual = t

  while atual != s:

    anterior = atual.pai

    # Evita reconstruir um caminho inválido
    if anterior is None:
      return None

    caminho.append((anterior, atual))
    atual = anterior

  caminho.reverse()
  return caminho

def Edmonds_Karp(G, s, t):
  for aresta in G[1]:
    aresta.f = 0

  Gf, adj_residual = cria_grafo_residual(G)
  BFS(Gf, s, adj_residual)

  while t.pai != None:
    caminho = encontra_caminho(s, t)

    # Pega o menor fluxo que pode ser enviado no caminho
    cf = min(
      capacidade_residual(G, u, v)
      for (u, v) in caminho
    )

    for (u, v) in caminho:

      # Se (u, v) é uma aresta do grafo...
      aresta = encontrar_aresta(G, u, v)
      if aresta is not None:
        aresta.f += cf
      else:
        aresta = encontrar_aresta(G, v, u)
        aresta.f -= cf

    Gf, adj_residual = cria_grafo_residual(G)
    BFS(Gf, s, adj_residual)

  return G

def main():

  # Vértices
  s = Vertice("s")
  v1 = Vertice("v1")
  v2 = Vertice("v2")
  v3 = Vertice("v3")
  v4 = Vertice("v4")
  t = Vertice("t")

  V = [s, v1, v2, v3, v4, t]

  # Arestas
  e1 = Aresta(s, v1, 16)
  e2 = Aresta(s, v2, 13)
  e3 = Aresta(v2, v1, 4)
  e4 = Aresta(v1, v3, 12)
  e5 = Aresta(v3, v2, 9)
  e6 = Aresta(v2, v4, 14)
  e7 = Aresta(v4, v3, 7)
  e8 = Aresta(v3, t, 20)
  e9 = Aresta(v4, t, 4)

  E = [e1, e2, e3, e4, e5, e6, e7, e8, e9]

  # Grafo
  G = [V, E]

  mostraGrafoFluxo(G, "Grafo original")

  # Edmonds Karp
  Edmonds_Karp(G, s, t)

  # Mostra o fluxo encontrado em cada aresta
  for aresta in G[1]:
    u, v = aresta.aresta
    print(f"{u.nome} -> {v.nome}: fluxo = {aresta.f} / capacidade = {aresta.capacidade}")

  # Calcula o fluxo máximo que sai da fonte
  fluxo_maximo = sum(
    aresta.f
    for aresta in G[1]
    if aresta.aresta[0] == s
  )
  print(f"\nFluxo máximo: {fluxo_maximo}")

  # Grafo com os fluxos calculados
  mostraGrafoFluxo(G, f"Fluxo máximo {fluxo_maximo}")

  plt.show()

if __name__ == "__main__":
  main()