# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import networkx as nx
from src.Q01 import associate_astronauts, example_Q1
from src.Q02 import insep_blocks, example_Q2
from util.networkx_util import read_multiple_CSV, draw_graph


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Questão 01
    # example_Q1()
    # Questão 02
    # example_Q2()
    nexample="les_miserables_graph"
    layout = "spring_layout"
    BCGraph = nx.complete_multipartite_graph(3, 4)
    X, Y = nx.bipartite.sets(BCGraph)
    draw_graph(BCGraph, nx.bipartite_layout(BCGraph, X),
               nset=[X, Y], nsetcolor=["blue", "green"])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
