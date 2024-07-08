## EM CONSTRUÇÃO

import matplotlib.pyplot as plt
import networkx as nx
from util.networkx_util import draw_graph
size = 8
CGraph = nx.complete_graph(size)
draw_graph(CGraph, layoutid='spring_layout', title="K3",
           eset=[[(0,1)],[(0,2),(1,2)]], esetcolor=["red","green","yellow"], esetlabel=['l1','l2','other'])

