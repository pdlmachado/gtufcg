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

