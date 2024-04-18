import networkx as nx

"""# get_node_ids """
# Retorna uma lista com os identificadores de nodes cujo valor do atributo "attr" é "value"
def get_node_ids (g, attr, value):
   return [i for i in g.nodes if g.nodes[i][attr]==value]

"""# has_parallel_edges """

def has_parallel_edges (G):
  for u in G.nodes:
    for v in G.nodes:
      if G.number_of_edges(u,v) > 1:
        return True
  return False


"""# get_edge """

# Retorna uma tupla para uma aresta existente entre dois vértices na ordem que foi considerada
# para os vértices na criação da aresta
# O grafo g deve ser simples
def get_edge(g, u, v):
  if type(g) is nx.classes.multigraph.MultiGraph:
    for x,y,k in g.edges:
        if x == u and y == v or x == v and y == u:
            return k
  else:
    for x,y in g.edges:
        if x == u and y == v or x == v and y == u:
            return (x,y)
          
"""# get_path_edges """

# Retorna um path qualquer a partir de uma lista de vértices
# Apenas para multigrafos
def get_path_edges(g,path):
  edges = [(path[i],path[i+1],get_edge(g,path[i],path[i+1])) for i in range(len(path)-1)]
  out = []
  for i in range(len(path)-1):
    u,v,k = edges[i]
    out.append((u,v,k))
  return out

"""## get_node_classes """
# Função que agrupa valores de um dicionário de vértices em n faixas
# Retorna uma lista de listas com os vértices de cada faixa
# d - dicionário
# r - quantidade de faixas
from math import trunc


def get_node_classes(d, r):
    node_class = [[] for i in range(r)]
    minimo = min(d.values())
    máximo = max(d.values())
    step = (máximo - minimo) / (r)
    for n in d.keys():
        if d[n] == máximo:
            node_class[r - 1].append(n)
        else:
            index = trunc((d[n] - minimo) / step)
            node_class[index].append(n)
    return minimo, step, node_class
