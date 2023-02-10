import networkx as nx
from util.networkx_util import draw_graph

def naovizinhos (G,v):
    return [u for u in G.nodes if not u in G.neighbors(v) ]

G = nx.read_graphml('graphs/m-u-cy-sc-p-01.graphml')
print(G)
