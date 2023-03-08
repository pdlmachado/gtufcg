# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import networkx as nx
from src.Q01 import associate_astronauts
#from src.Q02 import insep_blocks
from util.networkx_util import read_multiple_CSV, draw_graph

def example_Q1():
    a_list = [
        ('Kurtis','Shepstone','Italy'),
        ('Rafferty','Stoak','Canada'),
        ('Libbey','Anselm','Canada'),
        ('Odelinda','Thireau','Italy'),
        ('Rick','Caset','Canada'),
        ('Matthew','Fearnyough','Canada'),
        ('Madonna','Brazener','Canada'),
        ('Laure','Drohane','Canada'),
        ('Eleanore','Pollett','USA'),
        ('Town','Duddell','Canada')
    ]
    # Invocando a função
    G = associate_astronauts(a_list)
    print([G.nodes[n]['last_name'] for n in G.nodes])
    # Saída esperada: (não necessariamente na mesma ordem)
    # ['Shepstone', 'Stoak', 'Anselm', 'Thireau', 'Caset', 'Fearnyough', 'Brazener', 'Drohane', 'Pollett', 'Duddell']
    print([(G.nodes[s]['last_name'],G.nodes[t]['last_name']) for (s,t) in G.edges])
    # Saída esperada: (não necessariamente na mesma ordem)
    # [('Shepstone', 'Stoak'), ('Shepstone', 'Anselm'), ('Shepstone', 'Caset'), ('Shepstone', 'Fearnyough'), ('Shepstone', 'Brazener'), ('Shepstone', 'Drohane'), ('Shepstone', 'Pollett'), ('Shepstone', 'Duddell'), ('Stoak', 'Thireau'), ('Stoak', 'Pollett'), ('Anselm', 'Thireau'), ('Anselm', 'Pollett'), ('Thireau', 'Caset'), ('Thireau', 'Fearnyough'), ('Thireau', 'Brazener'), ('Thireau', 'Drohane'), ('Thireau', 'Pollett'), ('Thireau', 'Duddell'), ('Caset', 'Pollett'), ('Fearnyough', 'Pollett'), ('Brazener', 'Pollett'), ('Drohane', 'Pollett'), ('Pollett', 'Duddell')]
    draw_graph(G, nx.circular_layout(G),node_labels=nx.get_node_attributes(G,'last_name'))

def insep_blocks (G,limiar):
    list_cycles = []
    for c in filter(lambda c : len(c) == 3, nx.cycle_basis(G)):
        insep = True
        for i in range(3):
            for j in range(i+1,3):
                if G[c[i]][c[j]]['weight'] > limiar:
                    insep = False
        if insep:
            list_cycles.append(c)
    return list_cycles

def example_Q2(): 
    # Importando o grafo, pesos são labels das arestas
    G = nx.read_graphml('graphs\s-u-w-cy-sc-p-03.graphml')
    for s,t in G.edges:
        G[s][t]['weight'] = int(G[s][t]['label'])
    # Invocando a função
    iblocks = insep_blocks(G,7)
    print(f"Blocos Inseparáveis com limiar 7: {iblocks}")
    # Saída Esperada: [['n3', 'n5', 'n4'], ['n6', 'n5', 'n4'], ['n1', 'n0', 'n2']]
    iblocks = insep_blocks(G,9)
    print(f"Blocos Inseparáveis com limiar 9: {iblocks}")
    # Saída Esperada: [['n5', 'n6', 'n7'], ['n5', 'n4', 'n6'], ['n1', 'n3', 'n4'], ['n5', 'n3', 'n4'], ['n1', 'n2', 'n4'], ['n1', 'n0', 'n2']]
    draw_graph(G,nx.spring_layout(G),edge_labels=nx.get_edge_attributes(G,'weight'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #example_Q1()
    example_Q2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
