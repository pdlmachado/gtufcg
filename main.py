# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import networkx as nx
from src.Q01 import associate_astronauts
from util.networkx_util import read_multiple_CSV, draw_graph

def manual_test_Q1():
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
    # G = nx.Graph()
    # Criando os vértices do grafo a partir do arquivo CSV
    # read_multiple_CSV(G, filename, vid="last_name")
    # Invocando a função
    G = associate_astronauts(a_list)
    print([G.nodes[n]['last_name'] for n in G.nodes])
    # Saída esperada: (não necessariamente na mesma ordem)
    # ['Shepstone', 'Stoak', 'Anselm', 'Thireau', 'Caset', 'Fearnyough', 'Brazener', 'Drohane', 'Pollett', 'Duddell']
    print([(G.nodes[s]['last_name'],G.nodes[t]['last_name']) for (s,t) in G.edges])
    # Saída esperada: (não necessariamente na mesma ordem)
    # [('Shepstone', 'Stoak'), ('Shepstone', 'Anselm'), ('Shepstone', 'Caset'), ('Shepstone', 'Fearnyough'), ('Shepstone', 'Brazener'), ('Shepstone', 'Drohane'), ('Shepstone', 'Pollett'), ('Shepstone', 'Duddell'), ('Stoak', 'Thireau'), ('Stoak', 'Pollett'), ('Anselm', 'Thireau'), ('Anselm', 'Pollett'), ('Thireau', 'Caset'), ('Thireau', 'Fearnyough'), ('Thireau', 'Brazener'), ('Thireau', 'Drohane'), ('Thireau', 'Pollett'), ('Thireau', 'Duddell'), ('Caset', 'Pollett'), ('Fearnyough', 'Pollett'), ('Brazener', 'Pollett'), ('Drohane', 'Pollett'), ('Pollett', 'Duddell')]
    draw_graph(G, nx.circular_layout(G),node_labels=nx.get_node_attributes(G,'last_name'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manual_test_Q1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
