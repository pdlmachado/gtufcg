"""
A associação espacial internacional precisa enviar 2 astronautas de nacionalidades 
diferentes para uma missão a Lua.

Construa uma função, duplas_astronauta, que recebe um arquivo CSV entrada com informações sobre
astronautas, incluindo sua nacionalidade, e retorna um grafo onde os vértices representam 
astronautas e as arestas associam todos os astronautas de nacionalidades diferentes. 
Um exemplo de arquivo CSV que pode ser usado como entrada segue abaixo:

first_name,last_name,country
Kurtis,Shepstone,Canada
Rafferty,Stoak,Canada
Libbey,Anselm,Croatia
Odelinda,Thireau,Canada
Rick,Caset,Canada
Matthew,Fearnyough,Croatia
Madonna,Brazener,Canada
Laure,Drohane,Canada
Eleanore,Pollett,Canada
Town,Duddell,Canada

Para o exemplo abaixo, as seguintes duplas podem realizar a viagem:

('Shepstone', 'Anselm')
('Shepstone', 'Fearnyough')
('Stoak', 'Anselm')
('Stoak', 'Fearnyough')
('Anselm', 'Thireau')
('Anselm', 'Caset')
('Anselm', 'Brazener')
('Anselm', 'Drohane')
('Anselm', 'Pollett')
('Anselm', 'Duddell')
('Thireau', 'Fearnyough')
('Caset', 'Fearnyough')
('Fearnyough', 'Brazener')
('Fearnyough', 'Drohane')
('Fearnyough', 'Pollett')
('Fearnyough', 'Duddell')
"""

import networkx as nx
from util.networkx_util import draw_graph

def associate_astronauts (list_a):
    # Escreva aqui o seu código
    if list_a is None:
        return None
    G = nx.Graph()
    for i in range(len(list_a)):
        f,l,c = list_a[i]
        G.add_node(i,first_name=f,last_name=l,country=c)
    for v in G.nodes:
        for u in G.nodes:
            if (G.nodes[v]['country'] != G.nodes[u]['country']):
                if not G.has_edge(u,v):
                    G.add_edge(u,v)
    return G

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

