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
from util.networkx_util import read_multiple_CSV, draw_graph

def associate_astronauts (G):
    # Escreva aqui o seu código
    for v in G.nodes:
        for u in G.nodes:
            if (G.nodes[v]['country'] != G.nodes[u]['country']):
                if not G.has_edge(u,v):
                    G.add_edge(u,v)
##
# Ambiente para Testes Manuais
filename = "datasets/astronauta.csv"
G = nx.Graph()
# Criando os vértices do grafo a partir do arquivo CSV
read_multiple_CSV(G,filename,vid="last_name")
# Invocando a função
associate_astronauts(G)
print(G.nodes)
# Saída esperada: (não necessariamente na mesma ordem)
# ['Shepstone', 'Stoak', 'Anselm', 'Thireau', 'Caset', 'Fearnyough', 'Brazener', 'Drohane', 'Pollett', 'Duddell']
print(G.edges)
# Saída esperada: (não necessariamente na mesma ordem)
['Shepstone', 'Stoak', 'Anselm', 'Thireau', 'Caset', 'Fearnyough', 'Brazener', 'Drohane', 'Pollett', 'Duddell']
[('Shepstone', 'Anselm'), ('Shepstone', 'Fearnyough'), ('Stoak', 'Anselm'), ('Stoak', 'Fearnyough'), ('Anselm', 'Thireau'), ('Anselm', 'Caset'), ('Anselm', 'Brazener'), ('Anselm', 'Drohane'), ('Anselm', 'Pollett'), ('Anselm', 'Duddell'), ('Thireau', 'Fearnyough'), ('Caset', 'Fearnyough'), ('Fearnyough', 'Brazener'), ('Fearnyough', 'Drohane'), ('Fearnyough', 'Pollett'), ('Fearnyough', 'Duddell')]
draw_graph(G,nx.spring_layout(G))

