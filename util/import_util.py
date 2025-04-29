import networkx as nx

"""# Import"""

"""## read_multiple_csv

Importa um grafo a partir de tabelas com os conjuntos de vértices e arestas.

Parâmetros:
-   g - instância do grafo
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

def read_multiple_CSV(g,
                      vfilename='', vid='',
                      efilename='', esourceid='', etargetid='', weightid='',
                      delimiter=',', multiple_edges=True, self_loops=True,
                      toInt=[], toFloat=[],
                      node_label=None, edge_label=None):
    # Vertices
    listcsvV = []
    with open(vfilename, newline='') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            listcsvV.append(row)
    f.close()
    read_vertices(g, listcsvV, vid, node_label)
    # Arestas
    if efilename != '':
        listcsvE = []
        with open(efilename, newline='') as f:
            reader = csv.reader(f, delimiter=delimiter)
            for row in reader:
                listcsvE.append(row)
        f.close()
        read_edges(g, listcsvE, esourceid, etargetid, weightid, 
                   self_loops, multiple_edges, edge_label)
    for u,v in g.edges:
        for attr in toInt:
            g[u][v][attr] = int(G[u][v][attr])
    for u,v in g.edges:
        for attr in toFloat:
            g[u][v][attr] = float(G[u][v][attr])  


def read_vertices(g, listcsv, vid, node_label):
    headers = listcsv[0]
    vertex_index = headers.index(vid)
    for l in range(1, len(listcsv)):
        node = listcsv[l][vertex_index]
        g.add_node(node)
        for h in range(len(headers)):
            g.nodes[node][headers[h]] = listcsv[l][h]
            if node_label == headers[h]:
              g.nodes[node]['label'] = g.nodes[node][node_label]


def read_edges(g, listcsv, esourceid, etargetid, weightid, 
               self_loops, multiple_edges, edge_label):
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
            if type(g) is nx.classes.multigraph.MultiGraph:
                key = g.number_of_edges(source, target)
                g.add_edge(source, target, key)
                for h in range(len(headers)):
                    g[source][target][key][headers[h]] = listcsv[l][h]
                    if edge_label == headers[h]:
                        g[source][target][key]['label'] = g[source][target][key][edge_label]
                if weight_index != -1:
                    g[source][target][key]['weight'] = listcsv[l][weight_index]
            else:
                g.add_edge(source, target)
                for h in range(len(headers)):
                    g[source][target][headers[h]] = listcsv[l][h]
                    if edge_label == headers[h]:
                      g[source][target]['label'] = g[source][target][edge_label]
                if weight_index != -1:
                    g[source][target]['weight'] = listcsv[l][weight_index]
