# -*- coding: utf-8 -*-

# Importando pacotes
import networkx as nx
import matplotlib.pyplot as plt

"""# Draw """ 

def draw_graph(G,pos,node_labels=None,edge_labels=None,
                     node_color="cyan", node_size=500, nmap=None,
                     edge_color="gray", emap=None,
                     width=8, height=5,
                     nset=[], nsetcolor=[], nsetlabel=[],
                     eset=[], esetcolor=[], esetlabel=[]):
  if nset == []:
    nodes = nx.draw_networkx_nodes(G, pos, node_color=node_color, cmap=nmap, node_size=node_size)
  else:
    for i in range(len(nset)):
      nx.draw_networkx_nodes(G, pos, nodelist=nset[i], node_color=nsetcolor[i], label=nsetlabel[i], node_size=node_size)
  if node_labels is None:
    nx.draw_networkx_labels(G, pos)
  else:
    nx.draw_networkx_labels(G,pos,labels=node_labels)
  ax = plt.gca()
  v = list(G.nodes)
  elist = [] # Arestas paralelas
  notelist = [] # Links
  for i in range(len(G.nodes)):
    for j in range(i,len(G.nodes)):
      elistb = [e for e in G.edges if (e[0]==v[i] and e[1]==v[j]) or (e[0]==v[j] and e[1]==v[i])]
      if len(elistb) > 1:
        for k in range(len(elistb)):
          elist.append((elistb[k][0],elistb[k][1],k))
      elif len(elistb) == 1:
        notelist.append(elistb[0])
  # Desenhando arestas paralelas
  for e in elist:
    if nx.is_directed(G): # Grafos Direcionados
      ax.annotate("",
                xy=pos[e[0]], xycoords='data',
                xytext=pos[e[1]], textcoords='data',
                arrowprops=dict(arrowstyle="-|>", color=edge_color,
                                shrinkA=11, shrinkB=11,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])),
                                ),
      )
    else: # Grafos Não-Direcionados
      ax.annotate("",
                xy=pos[e[0]], xycoords='data',
                xytext=pos[e[1]], textcoords='data',
                arrowprops=dict(arrowstyle="-", color=edge_color,
                                shrinkA=11, shrinkB=11,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])),
                                ),
      )
  # Desenhando loops simples e links
  nx.draw_networkx_edges(G,pos,arrows=True, edge_color=edge_color,
                         edgelist=[e for e in G.edges if e in notelist])
  # Desenhando edge_labels
  if edge_labels is None:
    pass
  else:
    if elist == []:
      nx.draw_networkx_edge_labels(G,pos,font_color=edge_color,
                                   edge_labels=edge_labels)
  plt.axis(False)
  plt.rcParams['figure.figsize'] = [width,height]
  plt.show()

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
"""
import csv
def read_multiple_CSV(G,
                      vfilename='',vid='',
                      efilename='',esourceid='',etargetid='',weightid='',
                      delimiter=','):
  # Vertices
  listcsvV = []
  with open(vfilename, newline='') as f:
      reader = csv.reader(f,delimiter=delimiter)    
      for row in reader:
        listcsvV.append(row)
  f.close()
  viddict = {}
  read_vertices(G,listcsvV,vid)
  # Arestas
  if efilename != '':
    listcsvE = []
    with open(efilename, newline='') as f:
      reader = csv.reader(f,delimiter=delimiter)    
      for row in reader:
        listcsvE.append(row)
    f.close()
    read_edges(G,listcsvE,esourceid,etargetid,weightid)

def read_vertices(G,listcsv,vid):  
  headers = listcsv[0]
  vertex_index = headers.index(vid)
  for l in range(1,len(listcsv)):
    node = listcsv[l][vertex_index]
    G.add_node(node)
    for h in range(len(headers)):
      G.nodes[node][headers[h]] = listcsv[l][h]

def read_edges (G,listcsv,esourceid,etargetid,weightid):
  headers = listcsv[0]
  source_index = headers.index(esourceid)
  target_index = headers.index(etargetid)
  if weightid != '':
    weight_index = headers.index(weightid)
  else:
    weight_index = -1
  for l in range(1,len(listcsv)):
    source = listcsv[l][source_index]
    target = listcsv[l][target_index]
    if type (G) is nx.classes.multigraph.MultiGraph:
      key = G.number_of_edges(source,target)
      G.add_edge(source,target,key)
      for h in range(len(headers)):
        G[source][target][key][headers[h]] = listcsv[l][h]
      if weight_index != -1:
        G[source][target][key]['weight'] = listcsv[l][weight_index]
    else:
      G.add_edge(source,target)
      for h in range(len(headers)):
        G[source][target][headers[h]] = listcsv[l][h]
      if weight_index != -1:
        G[source][target]['weight'] = listcsv[l][weight_index]