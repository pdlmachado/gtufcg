import networkx as nx

"""# Import"""

"""## read_multiple_csv

Importa um grafo a partir de tabelas com os conjuntos de vértices e arestas.

Parâmetros:
-   G - instância do grafo
-   vfilename - arquivo com tabela de vértices no formato CSV
-   vid - atributo que representa vértices na tabela de arestas
-   efilename - arquivo com tabela de arestas no formato CSV
-   esourceid - atributo que representa o vértice origem
-   etargetid - atributo que representa o vértice destino
-   weightid - atributo que representa o peso das arestas (se existir)
-   delimiter - delimitador utilizado nos arquivos CSV - default: ,
-   multiple_edges - se False, o grafo não poderá ter arestas paralelas
-   self_loops - se False, o grafo não poderá ter aresta loop
"""
import csv


def read_multiple_CSV(G,
                      vfilename='', vid='',
                      efilename='', esourceid='', etargetid='', weightid='',
                      delimiter=',', multiple_edges=True, self_loops=True,
                      toInt=[], toFloat=[]):
    # Vertices
    listcsvV = []
    with open(vfilename, newline='') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            listcsvV.append(row)
    f.close()
    read_vertices(G, listcsvV, vid)
    # Arestas
    if efilename != '':
        listcsvE = []
        with open(efilename, newline='') as f:
            reader = csv.reader(f, delimiter=delimiter)
            for row in reader:
                listcsvE.append(row)
        f.close()
        read_edges(G, listcsvE, esourceid, etargetid, weightid, self_loops, multiple_edges)
    for u,v in G.edges:
        for attr in toInt:
            G[u][v][attr] = int(G[u][v][attr])
    for u,v in G.edges:
        for attr in toFloat:
            G[u][v][attr] = float(G[u][v][attr])  


def read_vertices(G, listcsv, vid):
    headers = listcsv[0]
    vertex_index = headers.index(vid)
    for l in range(1, len(listcsv)):
        node = listcsv[l][vertex_index]
        G.add_node(node)
        for h in range(len(headers)):
            G.nodes[node][headers[h]] = listcsv[l][h]


def read_edges(G, listcsv, esourceid, etargetid, weightid, self_loops, multiple_edges):
    headers = listcsv[0]
    source_index = headers.index(esourceid)
    target_index = headers.index(etargetid)
    if weightid != '':
        weight_index = headers.index(weightid)
    else:
        weight_index = -1
    for l in range(1, len(listcsv)):
        source = listcsv[l][source_index]
        target = listcsv[l][target_index]
        if not self_loops and source == target or not multiple_edges and G.has_edge(source, target):
            pass
        else:
            if type(G) is nx.classes.multigraph.MultiGraph:
                key = G.number_of_edges(source, target)
                G.add_edge(source, target, key)
                for h in range(len(headers)):
                    G[source][target][key][headers[h]] = listcsv[l][h]
                if weight_index != -1:
                    G[source][target][key]['weight'] = listcsv[l][weight_index]
            else:
                G.add_edge(source, target)
                for h in range(len(headers)):
                    G[source][target][headers[h]] = listcsv[l][h]
                if weight_index != -1:
                    G[source][target]['weight'] = listcsv[l][weight_index]


