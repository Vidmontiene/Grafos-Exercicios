"""
Algoritmo de Ford-Fulkerson para encontrar o fluxo máximo
em uma rede direcionada com capacidades nas arestas.

O algoritmo começa inicializando o fluxo de todas as arestas com zero e,
em seguida, procura caminhos da fonte até o destino na rede residual,
utilizando uma busca em profundidade (DFS).

Para cada caminho encontrado, calcula a capacidade residual mínima entre
suas arestas, que determina a quantidade máxima de fluxo que pode ser
enviada por esse caminho. Depois, atualiza os fluxos das arestas percorridas.

A rede residual considera tanto as arestas originais, cuja capacidade
residual corresponde à capacidade menos o fluxo atual, quanto as arestas
reversas, que permitem cancelar parte do fluxo enviado anteriormente.

O processo se repete até que não exista mais um caminho da fonte ao destino
na rede residual. Ao final, os fluxos armazenados nas arestas representam
um fluxo máximo da rede.
"""

from Cap_3_dfs import DFS
from auxiliares import mostraGrafoFluxo
import matplotlib.pyplot as plt

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

# Define uma aresta
class Aresta:

  # Construtor
  def __init__(self, v1, v2, capacidade):
    self.aresta = (v1, v2)
    self.capacidade = capacidade
    self.f = 0

# Verifica se uma aresta está no grafo
def encontrar_aresta(G, u, v):

  for aresta in G[1]:
    v1, v2 = aresta.aresta
    if v1 == u and v2 == v:
      return aresta
    
  return None

# Indica o quanto de fluxo ainda pode ser enviado por uma aresta 
def capacidade_residual(G, u, v):

  # Verifica se é uma aresta original
  aresta = encontrar_aresta(G, u, v)

  if aresta is not None:
    return aresta.capacidade - aresta.f

  # Caso contrário, é uma aresta reversa
  aresta = encontrar_aresta(G, v, u)

  if aresta is not None:
    return aresta.f

  return 0

# Encontra um caminho da fonte até o destino na rede residual usando DFS
def encontrar_caminho_residual(G, s, t):

  # Cria a lista de adjacência da rede residual
  adj_residual = {v: [] for v in G[0]}

  for aresta in G[1]:
    u, v = aresta.aresta

    # Aresta original
    if aresta.capacidade - aresta.f > 0:
      adj_residual[u].append(v)

    # Aresta reversa
    if aresta.f > 0:
      adj_residual[v].append(u)

  # Reinicia informações da DFS
  for v in G[0]:
    v.cor = "white"
    v.pai = None

  # Executa a DFS
  DFS(G, adj_residual)

  # Se t não foi alcançado
  if t.cor == "white":
    return None

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

# Algoritmo de ford_fulkerson
def ford_fulkerson(G, s, t):

  # Inicia arestas
  for aresta in G[1]:
    aresta.f = 0

  while True:

    # Encontra um caminho de s até t na rede residual
    caminho = encontrar_caminho_residual(G, s, t)

    if caminho is None:
      break

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

  # Ford-Fulkerson
  ford_fulkerson(G, s, t)

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
  mostraGrafoFluxo(G, "Fluxo máximo")

  plt.show()


if __name__ == "__main__":
  main()