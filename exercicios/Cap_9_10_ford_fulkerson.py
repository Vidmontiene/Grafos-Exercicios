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
from auxiliares import mostraGrafoFluxo, encontrar_aresta, cria_capacidade_residual, cria_grafo_residual, encontra_caminho
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

# Ford Fulkerson - Utiliza DFS
def ford_fulkerson(G, s, t):

  # Inicia arestas
  for aresta in G[1]:
    aresta.f = 0

  while True:

    # Encontra um caminho de s até t na rede residual
    cf = cria_capacidade_residual(G)
    Gf, adj_residual = cria_grafo_residual(G, cf)
    DFS(Gf, adj_residual)
    caminho = encontra_caminho(s, t)

    if caminho is None:
      break # Não há caminho aumentante

    # Pega o menor fluxo que pode ser enviado no caminho
    menor_cf = min(cf[(u, v)] for (u, v) in caminho)
    
    for (u, v) in caminho:

      # Se (u, v) é uma aresta do grafo...
      aresta = encontrar_aresta(G, u, v)
      if aresta is not None:
        aresta.f += menor_cf
      else:
        aresta = encontrar_aresta(G, v, u)
        aresta.f -= menor_cf
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
  mostraGrafoFluxo(G, f"Fluxo máximo {fluxo_maximo}")

  plt.show()

if __name__ == "__main__":
  main()
  