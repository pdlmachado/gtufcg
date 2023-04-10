# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import networkx as nx
    from util.networkx_util import draw_graph
    #size = 8
    #CGraph = nx.complete_graph(size)
    #draw_graph(CGraph,nx.kamada_kawai_layout(CGraph), title="K8",
    #           node_color = range(CGraph.number_of_nodes()),nmap=plt.cm.YlGn,
    #           edge_color = range(CGraph.number_of_edges()),emap=plt.cm.OrRd)
    #draw_graph(CGraph, nx.kamada_kawai_layout(CGraph), title="K8",
    #           nset=[[0,1],[2,3],[4,5],[6,7]],nsetcolor=["blue","orange","red","green"],nsetlabel=['l1','l2','l3','l4'])
    #draw_graph(CGraph, nx.kamada_kawai_layout(CGraph), title="K3",
    #           eset=[[(0,1)],[(0,2),(1,2)]], esetcolor=["red","green"], esetlabel=['l1','l2'])
    from matplotlib import colors
    D1 = nx.read_graphml("graphs/s-d-cy-wc-02.graphml")
    print(D1.nodes)
    n_degrees = {n:D1.in_degree(n)+D1.out_degree(n) for n in D1.nodes}
    print(n_degrees)
    node_list = [ n for (n,k) in sorted(n_degrees.items(), key = lambda x:x[1])]
    print(node_list)
    print(list(colors.TABLEAU_COLORS.keys())[0:D1.number_of_nodes()])
    draw_graph(D1, nx.kamada_kawai_layout(D1), node_order=node_list,
               node_color=range(D1.number_of_nodes()),nmap=plt.cm.Purples,
               font_size=10, font_color="red")

