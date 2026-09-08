"""
Detecta as pontes e articulações de um grafo
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
    self.low = float('inf')
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
    Cor: {self.cor}
    Pai: {pai}
    Low: {self.low}
    Tempo de descoberta: {self.d}
    Tempo de término: {self.f}"""

def DFSPonte(G, adj):
  global tempo
  tempo = 0
  for u in G[0]:
    if u.cor == 'white':
      VisitaPonte(G, u, adj)

def VisitaPonte(G, u, adj):
  global tempo
  global pontes_articulacoes
  tempo += 1
  u.d = tempo
  u.cor = 'gray'
  u.low = u.d
  filhos = 0  # Conta quantos vértices u se liga que ainda são brancos

  for v in adj[u]:

    if v.cor == 'white':
      v.pai = u
      filhos += 1
      VisitaPonte(G, v, adj)
      u.low = min(u.low, v.low)

      if v.low > u.d:
        # Se a subárvore de v não consegue alcançar u nem nenhum
        # ancestral de u por outro caminho, remover a aresta (u, v)
        # desconecta o grafo. Portanto, (u, v) é uma ponte.    
        pontes_articulacoes[0].append((u, v))

      if u.pai != None and v.low >= u.d:
        # Se u não é a raiz e a subárvore de v não consegue alcançar
        # nenhum ancestral de u, remover u desconecta essa subárvore.
        # Portanto, u é um ponto de articulação.
        pontes_articulacoes[1].append(u)

    elif v != u.pai: 
      # Encontrou uma aresta (u, v) de retorno
      # O tempo de descoberta de v é menor que o low de u?
      u.low = min(u.low, v.d)

  if u.pai == None and filhos >= 2:
    # Após visitar todos os descendentes de u:
    # Se u é a raiz da árvore DFS e possui pelo menos dois filhos,
    # então cada filho inicia uma subárvore independente na DFS.
    # Portanto, ao remover u, essas subárvores ficam desconectadas,
    # tornando u um ponto de articulação.
    pontes_articulacoes[1].append(u)

  u.cor = 'black'
  tempo += 1
  u.f = tempo

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

  global pontes_articulacoes
  pontes_articulacoes = ([], [])

  DFSPonte(G, adj)
  print(f"Pontes: {[(u.nome, v.nome) for (u, v) in pontes_articulacoes[0]]}")
  print(f"Articulações: {[u.nome for u in pontes_articulacoes[1]]}")

  mostraGrafoNaoDirecionado(G, "Grafo")
  plt.show()

if __name__ == '__main__':
  main()
