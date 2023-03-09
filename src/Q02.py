"""
A administração de um município necessita agrupar os quarteirões de 
uma cidade em distritos para facilitar sua gestão. Para tal, possui 
um grafo onde os vértices representam quarteirões e arestas as 
vizinhanças entre os quarteirões.
Existem duas condições básicas a serem atendidas na divisão: 
1) os quarteirões de um distrito têm que ser vizinhos; 
2) Um grupo de 3 vizinhos mutuamente adjacentes não pode ser 
separado em distritos diferentes, a não ser que a distância entre 
dois deles seja maior que um limite de tolerância. 

Considerando o exemplo do grafo abaixo, os quarteirões I,J,D não 
podem ser separados se o limite de tolerância para a distância 
for maior que 300. A distância entre dois quarteirões está 
representada no peso da aresta.

Construa uma função, **inseparable**, que recebe um grafo como 
o apresentado no exemplo, um limite para tolerância de distância 
entre quarteirões e retorna uma lista com os grupos de 3 
quarteirões que não podem ser separados. 

Dica: Use o conceito de incorporação do subgrafo K3 para 
identificar os candidatos.
"""

import networkx as nx
from util.networkx_util import draw_graph

def insep_blocks (G,limiar):
    if G is None or limiar is None or limiar < 0:
        return None
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