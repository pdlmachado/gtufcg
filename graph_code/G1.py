def G1 ():
    G1 = graphviz.Graph('G1', filename="G1", format='png')
    G1.attr(rankdir='LR', size='8,5')
    G1.attr('node', shape='doublecircle')
    G1.node('a')
    G1.node('b')
    G1.node('c')
    G1.node('d')
    G1.node('e')
    G1.edge('a','b',label='s')
    G1.edge('a','a',label='t')
    G1.edge('b','c',label='u')
    G1.edge('c','d',label='v')
    G1.edge('b','d',label='x')
    G1.edge('c','d',label='w')
    G1.edge('a','d',label='y')
    G1.edge('d','e',label='z')
    G1.view()   
    