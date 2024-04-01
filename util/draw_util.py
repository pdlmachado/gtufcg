# -*- coding: utf-8 -*-

# Importando pacotes
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.cm import ScalarMappable
from matplotlib import colors
from util.get_util import get_node_classes

"""# Graph Draw """

"""## draw_graph """


# Desenha um grafo de tipo qualquer
# Parâmetros:
#   G, pos, title, layoutid - grafo, layout, título, id de um layout (caso deseje que o objeto layout seja criado internamente)
#   node_labels, node_edges - dicionários com os labels de cada vértice e aresta respectivamente
#   node_color, node_size, nmap, node_order - cor, tamanho, mapa e ordem de cores para vértices (Ex: nmap = plt.cm.YlGn)
#        Se nmap não for None, node_color tem que ser um array de números inteiros que indexam o map para cada vértice
#   vmin, vmax - valor máximo e mínimo para representar no colorbar. 
#        Se vmin,vmax = None ou nmax = None, não será criado um colorbar.
#   edge_color, arrow_size, emap - cor, tamanho da seta e mapa de cores para arestas
#               (Ex: emap = plt.cm.YlGn) (emap apenas para links e loops)
#        Se emap não for None, edge_color tem que ser um array de números inteiros que indexam o map para cada arestas
#   font_size, font_color - tamanho e cor da fonte utilizada para os vértices
#   nset, nsetcolor, nsetlabel - definem grupos de vértices que terão cores diferentes
#      nset - lista de lista de vértices (listas disjuntas; se um ou mais vértices não foram incluídos,
#                                         a função adiciona um grupo complementar com estes vértices)
#      nsetcolor (obrigatório, quando usando nset) -
#         lista de cores, uma para cada grupo definido em nset (adicione uma cor a mais para o grupo complementar, se existir)
#      nsetlabel (opcional quando usando nset e nsetcolor) -
#          lista de labels, um para cada grupo definido em nset (adicione um label a mais para o grupo complementar, se existir)
#   eset, esetcolor, esetlabel - definem grupos de arestas que terão cores diferentes (apenas para links e loops)
#      eset - lista de lista de arestas (listas disjuntas; se arestas não foram incluídos, a função adiciona uma lista com o complemento)
#      esetcolor (obrigatório quando usando eset) -
#        lista de cores, uma para cada grupo definido em nset (adicione uma cor a mais para o grupo complementar, se existir)
#      esetlabel (opcional quando usando eset e esetcolor) -
#        lista de labels, um para cada grupo definido em nset (adicione um label a mais para o grupo complementar, se existir)
# Referências:
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
# https://matplotlib.org/stable/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py


def draw_graph(G, pos=None, title="", layoutid=None,
               node_labels=None, edge_labels=None,
               node_color="cyan", node_size=500, nmap=None,
               node_order=None, vmin=None, vmax=None,
               font_size=12, font_color="black",
               edge_color="gray", arrow_size=15, emap=None,
               width=8, height=5,
               nset=[], nsetcolor=[], nsetlabel=[],
               eset=[], esetcolor=[], esetlabel=[]):
    ax = plt.gca()
    if pos is None and layoutid is not None:
        if layoutid in ["neato", "dot", "fdp", "sfdp", "circo", "twopi", "osage", "patchwork"]:
            pos = nx.nx_agraph.pygraphviz_layout(G, layoutid)
        elif layoutid in ["circular_layout", "kamada_kawai_layout", "planar_layout", "random_layout", "shell_layout",
                          "spring_layout", "spectral_layout", "spiral_layout", "planar_layout"]:
            pos = eval(f"nx.{layoutid}(G)")
    elif pos is None:
        pos = nx.spring_layout(G)
    if not nset:
        if node_order is None:
            nx.draw_networkx_nodes(G, pos, node_color=node_color, cmap=nmap, node_size=node_size)
        else:
            nx.draw_networkx_nodes(G, pos, nodelist=node_order, node_color=node_color, cmap=nmap, node_size=node_size)
    elif not nset == [] and nsetlabel == []:
        comp_nset = [n for n in G.nodes if n not in sum([list(x) for x in nset], [])]
        if comp_nset:
            nset.append(comp_nset)
        for i in range(len(nset)):
            nx.draw_networkx_nodes(G, pos, nodelist=nset[i], node_color=nsetcolor[i], node_size=node_size)
    else:
        handles = []
        comp_nset = [n for n in G.nodes if n not in sum([list(x) for x in nset], [])]
        if comp_nset:
            nset.append(comp_nset)
        for i in range(len(nset)):
            nx.draw_networkx_nodes(G, pos, nodelist=nset[i], node_color=nsetcolor[i], label=nsetlabel[i],
                                   node_size=node_size)
            handles.append(mpatches.Patch(color=nsetcolor[i], label=nsetlabel[i]))
        ax.legend(handles=handles)
    if node_labels is None:
        nx.draw_networkx_labels(G, pos, font_size=font_size, font_color=font_color)
    else:
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=font_size, font_color=font_color)
    v = list(G.nodes)
    elist = []  # Arestas paralelas
    notelist = []  # Links
    for i in range(len(G.nodes)):
        for j in range(i, len(G.nodes)):
            elistb = [e for e in G.edges if (e[0] == v[i] and e[1] == v[j]) or (e[0] == v[j] and e[1] == v[i])]
            if len(elistb) > 1:
                for k in range(len(elistb)):
                    elist.append((elistb[k][0], elistb[k][1], k))
            elif len(elistb) == 1:
                notelist.append(elistb[0])
    # Desenhando arestas paralelas
    for e in elist:
        if nx.is_directed(G):  # Grafos Direcionados
            ax.annotate("",
                        xy=pos[e[0]], xycoords='data',
                        xytext=pos[e[1]], textcoords='data',
                        arrowprops=dict(arrowstyle="-|>", color=edge_color,
                                        shrinkA=11, shrinkB=11,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=rrr".replace('rrr', str(0.3 * e[2])),
                                        ),
                        )
        else:  # Grafos Não-Direcionados
            ax.annotate("",
                        xy=pos[e[0]], xycoords='data',
                        xytext=pos[e[1]], textcoords='data',
                        arrowprops=dict(arrowstyle="-", color=edge_color,
                                        shrinkA=11, shrinkB=11,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=rrr".replace('rrr', str(0.3 * e[2])),
                                        ),
                        )
    # Desenhando loops simples e links
    if not eset:
        nx.draw_networkx_edges(G, pos,
                               arrows=True, arrowsize=arrow_size,
                               edge_color=edge_color, edge_cmap=emap,
                               edgelist=[e for e in G.edges if e in notelist])
    elif not esetlabel:
        comp_eset = [e for e in G.edges if e not in [get_edge(G, x[0], x[1]) for x in sum([list(x) for x in eset], [])]]
        if comp_eset:
            eset.append(comp_eset)
        for i in range(len(eset)):
            nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=arrow_size,
                                   edge_color=esetcolor[i],
                                   edgelist=eset[i])
    else:
        handles = []
        # print(eset)
        # print([get_edge(G, x[0], x[1]) for x in sum(eset, [])])
        comp_eset = [e for e in G.edges if e not in [get_edge(G, x[0], x[1]) for x in sum([list(x) for x in eset], [])]]
        if comp_eset:
            eset.append(comp_eset)
        for i in range(len(eset)):
            nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=arrow_size,
                                   edge_color=esetcolor[i],
                                   edgelist=eset[i])
            handles.append(mpatches.Patch(color=esetcolor[i], label=esetlabel[i]))
        ax.legend(handles=handles)
    # Desenhando edge_labels
    if edge_labels is None:
        pass
    else:
        if elist == [] and type(G) is not nx.classes.multigraph.MultiGraph and type(
                G) is not nx.classes.multidigraph.MultiDiGraph:
            nx.draw_networkx_edge_labels(G, pos, font_color=edge_color,
                                         font_size=font_size - 2,
                                         edge_labels=edge_labels)
    plt.title(title)
    plt.axis(False)
    plt.rcParams['figure.figsize'] = [width, height]
    if nmap is not None and vmin is not None and vmax is not None:
        cnorm = colors.Normalize(vmin, vmax)
        sm = ScalarMappable(cnorm, nmap)
        plt.colorbar(sm, shrink=0.6)
    plt.show()


    