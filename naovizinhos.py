
import networkx as nx
import matplotlib as plt
from util.networkx_util import draw_graph

def naovizinhos (G,v):
    return [u for u in G.nodes if not u in G.neighbors(v) ]

G1 = nx.read_graphml('graphs/m-u-cy-sc-p-01.graphml')
print(G1.nodes)
print(naovizinhos(G1,'n0'))
draw_graph(G1,nx.spring_layout(G1))

