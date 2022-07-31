import matplotlib.pyplot as plt
import networkx as nx
import math

class Graph:
  def __init__(self):
    pass

  def visualize_graph(self, temp_edges=list):

    new_edges = [(u, v, {"label": l}) for u, v, l in temp_edges]

    G = nx.Graph()

    G.add_edges_from(new_edges)

    pos = nx.spring_layout(G, seed=8)

    plt.figure(figsize=(G.number_of_nodes(), G.number_of_nodes()))

    nx.draw_networkx_nodes(G, pos,node_size=700)

    edges = [e for e in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=edges, style="dashed", connectionstyle="arc3, rad=0.5")

    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    # fig, ax = plt.subplots(figsize=(8,10))
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout(pad=0.01)
    plt.show()


  def graceful_square_bistar(self, n: int):
    edges = [
             (4*n+1, 0, 4*n+1),
    ]

    for i in range(1, n+1):
      edges.append((4*n+1, n+i, 3*n+1-i))
      edges.append((0, i, i))
      edges.append((4*n+1, i, 4*n+1-i))
      edges.append((0, n+i, n+i))
    
    return edges

  def graceful_splitting_bistar(self, n: int):
    if n % 2 == 0:
      edges = [
              (2*n-1, 0, 2*n-1),  # uv
              (2*n-1, 1, 2*n-2),  # uv'
              (2*n, 0, 2*n)       # u'v
      ]

      for i in range(1, n+1):
        # uu_i
        if i <= n/2-1:
          edges.append((2*n-1, 1+2*i, 2*(n-1-i)))
        elif i <= n:
          edges.append((2*n-1, 6*n-2*i+2, 4*n-2*i+3))

        # vv_i
        if i == 1:
          edges.append((0, 5*n+3, 5*n+3))
        else:
          edges.append((0, 5*n+5-2*i, 5*n+5-2*i))

        # uu'_i
        if i == 1:
          edges.append((2*n-1, 4*n, 2*n+1))
        else:
          edges.append((2*n-1, n-2+i, n+1-i))
        
        # u'u_i
        if i <= n/2-1:
          edges.append((2*n, 1+2*i, 2*n-1-2*i))
        else:
          edges.append((2*n, 6*n-2*i+2, 4*n+2-2*i))

        # vv'_i
        edges.append((0, 6*n+4-i, 6*n+4-i))

        # v'v_i
        if i == 1:
          edges.append((1, 5*n+3, 5*n+2))
        else:
          edges.append((1, 5*n+5-2*i, 5*n+4-2*i))
      
      return edges
    else:
      edges = [
              (2*n-1, 0, 2*n-1),  # uv
              (2*n-1, 1, 2*n-2),  # uv'
              (2*n, 0, 2*n)       # u'v
      ]

      for i in range(1, n+1):
        # uu_i
        if i <= (n-1)/2-1:
          edges.append((2*n-1, 2+2*i, 2*n-2*i-3))
        elif i <= n:
          edges.append((2*n-1, 6*n-2*i+1, 4*n-2*i+2))

        # vv_i
        if i == 1:
          edges.append((0, 5*n+3, 5*n+3))
        else:
          edges.append((0, 5*n+5-2*i, 5*n+5-2*i))

        # uu'_i
        if i == 1:
          edges.append((2*n-1, 2, 2*n-3))
        else:
          edges.append((2*n-1, n-2+i, n+1-i))
        
        # u'u_i
        if i <= (n-1)/2-1:
          edges.append((2*n, 2+2*i, 2*n-2-2*i))
        else:
          edges.append((2*n, 6*n-2*i+1, 4*n-2*i+1))

        # vv'_i
        edges.append((0, 6*n+4-i, 6*n+4-i))

        # v'v_i
        if i == 1:
          edges.append((1, 5*n+3, 5*n+2))
        else:
          edges.append((1, 5*n+5-2*i, 5*n+4-2*i))
      
      return edges

  def graceful_splitting_complete_bipartite(self, n: int):
    edges = []

    for i in range(1, n+1):
      edges.append((0, 2*i, 2*i))
      edges.append((0, 2*n+i, 2*n+i))
      edges.append((1, 2*i, 2*i-1))
    
    return edges


  def odd_graceful_splitting_bistar(self, n: int):
    edges = [
             (0, 3, 3),
             (0, 5, 5),
             (2, 3, 1)
    ]

    for i in range(1, n+1):
      edges.append((0, 5+4*i, 5+4*i))
      edges.append((0, 12*n+7-2*i, 12*n+7-2*i))
      edges.append((2, 5+4*i, 3+4*i))
      if i==1:
        edges.append((3, 10*n+8, 10*n+5))
      else:
        edges.append((3, 10*n+8-2*i+2, 10*n+7-2*i))

      if i==1:
        edges.append((3, 8*n+8, 8*n+5))
      else:
        edges.append((3, 8*n+8-4*i+4, 8*n+9-4*i))
      
      if i==1:
        edges.append((5, 8*n+8, 8*n+3))
      else:
        edges.append((5, 8*n+8-4*i+4, 8*n+7-4*i))
    
    return edges


  def odd_graceful_shadow_bistar(self, n: int):
    edges = [
             (2, 7, 5),   # uv
             (0, 3, 3),   # u'v'
             (2, 3, 1),   # uv'
             (0, 7, 7),   # u'v
    ]

    for i in range(0, n):
      # uu_i
      edges.append((2, 16*n+11-4*(i+1), 16*n+9-4*(i+1)))

      # vv_i
      if i <= math.ceil(n/2) - 1:
        edges.append((7, 16+8*i, 9+8*i))
      if i <= math.floor(n/2) - 1:
        edges.append((7, 18+8*i, 11+8*i))

      # u'u'_i
      edges.append((0, 12*n+11-4*(i+1), 12*n+11-4*(i+1)))

      # v'v'_i
      if n % 2 == 0:
        if i <= math.ceil(n/2) - 1:
          edges.append((3, 16+4*n+8*i, 13+4*n+8*i))
        if i <= math.floor(n/2) - 1:
          edges.append((3, 18+4*n+8*i, 15+4*n+8*i))
      elif n % 2 == 1:
        if i <= math.ceil(n/2) - 1:
          edges.append((3, 14+4*n+8*i, 11+4*n+8*i))
        if i <= math.floor(n/2) - 1:
          edges.append((3, 20+4*n+8*i, 17+4*n+8*i))

      # uu'_i
      edges.append((2, 12*n+11-4*(i+1), 12*n+9-4*(i+1)))

      # vv'_i
      if n % 2 == 0:
        if i <= math.ceil(n/2) - 1:
          edges.append((7, 16+4*n+8*i, 9+4*n+8*i))
        if i <= math.floor(n/2) - 1:
          edges.append((7, 18+4*n+8*i, 11+4*n+8*i))
      elif n % 2 == 1:
        if i <= math.ceil(n/2) - 1:
          edges.append((7, 14+4*n+8*i, 7+4*n+8*i))
        if i <= math.floor(n/2) - 1:
          edges.append((7, 20+4*n+8*i, 13+4*n+8*i))

      # u'u_i
      edges.append((0, 16*n+11-4*(i+1), 16*n+11-4*(i+1)))

      # v'v_i
      if i <= math.ceil(n/2) - 1:
        edges.append((3, 16+8*i, 13+8*i))
      if i <= math.floor(n/2) - 1:
        edges.append((3, 18+8*i, 15+8*i))
    
    return edges
graph = Graph()
edges = graph.odd_graceful_shadow_bistar(2)
graph.visualize_graph(edges)
