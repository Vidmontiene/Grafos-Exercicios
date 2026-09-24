# Funções auxiliares nos algoritmos de grafos

import networkx as nx
import matplotlib.pyplot as plt

# Mostrar grafo não direcionado sem pesos
def mostraGrafo(G, nome):
  plt.figure()
  
  G_grafo = nx.DiGraph()

  G_grafo.add_nodes_from(
    [v.nome for v in G[0]]
  )
  
  G_grafo.add_edges_from(
    [(u.nome, v.nome) for (u, v) in G[1]]
  )
  pos = nx.spring_layout(G_grafo, k=0.5)

  nx.draw(
    G_grafo,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="lightgreen",
    arrows=True
  )
  plt.get_current_fig_manager().set_window_title(nome)

# Mostrar grafo direcionado sem pesos
def mostraGrafoNaoDirecionado(G, nome):
  plt.figure()

  G_grafo = nx.Graph()

  G_grafo.add_nodes_from(
    [v.nome for v in G[0]]
  )

  G_grafo.add_edges_from(
    [(u.nome, v.nome) for (u, v) in G[1]]
  )

  pos = nx.kamada_kawai_layout(G_grafo)

  nx.draw(
    G_grafo,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="lightgreen"
  )

  plt.get_current_fig_manager().set_window_title(nome)

# Mostra grafo não direcionado e os pesos
def mostraGrafoNaoDirecionadoPeso(G, nome, w):

  plt.figure()
  G_grafo = nx.Graph()

  G_grafo.add_nodes_from(
    [v.nome for v in G[0]]
  )

  G_grafo.add_edges_from(
    [(u.nome, v.nome) for (u, v) in G[1]]
  )

  pos = nx.kamada_kawai_layout(G_grafo)

  nx.draw(
    G_grafo,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="lightgreen"
  )

  # Pesos das arestas
  labels = {
    (u.nome, v.nome): peso_aresta(u, v, w)
    for (u, v) in G[1]
  }

  nx.draw_networkx_edge_labels(
    G_grafo,
    pos,
    edge_labels=labels
  )

  plt.get_current_fig_manager().set_window_title(nome)

# Mostra grafo direcionado e os pesos
def mostraGrafoDirecionadoPeso(G, nome, w):

  plt.figure()
  G_grafo = nx.DiGraph()

  G_grafo.add_nodes_from(
    [v.nome for v in G[0]]
  )

  G_grafo.add_edges_from(
    [(u.nome, v.nome) for (u, v) in G[1]]
  )

  pos = nx.kamada_kawai_layout(G_grafo)

  nx.draw(
    G_grafo,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="lightgreen",
    arrows = True
  )

  # Pesos das arestas
  labels = {
    (u.nome, v.nome): peso_aresta(u, v, w)
    for (u, v) in G[1]
  }

  nx.draw_networkx_edge_labels(
    G_grafo,
    pos,
    edge_labels=labels
  )

  plt.get_current_fig_manager().set_window_title(nome)

# Mostra grafo direcionado, pesos e atributo .d dos vértices
def mostraGrafoDirecionadoPesoD(G, nome, w):

  plt.figure()

  G_grafo = nx.DiGraph()

  G_grafo.add_nodes_from(
    [v.nome for v in G[0]]
  )

  G_grafo.add_edges_from(
    [(u.nome, v.nome) for (u, v) in G[1]]
  )

  pos = nx.kamada_kawai_layout(G_grafo)

  # Desenha os vértices e as arestas
  nx.draw(
    G_grafo,
    pos,
    with_labels=False,
    node_size=1000,
    node_color="lightgreen",
    arrows=True
  )

  # Nome e valor de d dos vértices
  labels_vertices = {
    v.nome: f"{v.nome}\n(d={v.d})"
    for v in G[0]
  }

  nx.draw_networkx_labels(
    G_grafo,
    pos,
    labels=labels_vertices
  )

  # Pesos das arestas
  labels_arestas = {
    (u.nome, v.nome): peso_aresta(u, v, w)
    for (u, v) in G[1]
  }

  nx.draw_networkx_edge_labels(
    G_grafo,
    pos,
    edge_labels=labels_arestas
  )

  plt.get_current_fig_manager().set_window_title(nome)

  plt.show()

# Cria a floresta do grafo
def florestaDeProfundidade(G):
  arvore = (G[0], [])
  for v in G[0]:
    if v.pai:
      arvore[1].append((v.pai, v))
  return arvore

# Printa o menor caminho entre dois vértices a partir da matriz de predecessores
def caminho_mais_curto(Pai, i, j):
  if i == j:
    print(i)
  elif Pai[i][j] == None:
    print("Não existe caminho")
    return
  else: 
    caminho_mais_curto(Pai, i, Pai[i][j])
    print(j)

# Pega o peso de uma aresta
def peso_aresta(u, v, w):
  if (u, v) in w:
    return w[(u, v)]
  return w[(v, u)]
