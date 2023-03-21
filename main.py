# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import networkx as nx
    from util.networkx_util import draw_graph
    size = 8
    CGraph = nx.complete_graph(size)
    draw_graph(CGraph, nx.kamada_kawai_layout(CGraph),
               node_color=range(size), nmap=plt.cm.YlGn)

