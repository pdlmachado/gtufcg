import networkx as nx
from util.networkx_util import read_multiple_CSV, draw_graph

G = nx.DiGraph()
read_multiple_CSV(G,vfilename="datasets/person-100.csv",
                  vid='SSN',
                  efilename="datasets/person T person.csv", esourceid="person_id1", etargetid="person_id2",
                  multiple_edges=False, self_loops=False)
S = G.subgraph(nodes=list(G.nodes)[0:20])
draw_graph(S,layoutid="kamada_kawai_layout",node_labels=nx.get_node_attributes(S,'last_name'))