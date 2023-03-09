import unittest
import networkx as nx
import src.Q02 as Q02
from parameterized import parameterized
from collections import Counter

## TEST DATA
# .graphs\s-u-w-cy-dis-p-01.graphml
S1 = ["n0 n1 2", "n0 n2 3", "n1 n2 1", "n3 n4 4"]
G1 = nx.parse_edgelist(S1,data=(("weight",int),))
# .grapns\s-u-w-cy-dis-p-02.graphml
S2 = ['n0 n1 1', 'n0 n3 5', 'n1 n3 2', 'n1 n6 4', 'n1 n4 6', 'n2 n5 3']
G2 = nx.parse_edgelist(S2,data=(("weight",int),))
# .graphs\s-u-w-cy-sc-p-03.graphml
S3 = ['n0 n1 4', 'n0 n2 7', 'n1 n3 3', 'n1 n2 2', 'n1 n4 9', 'n2 n4 8', 'n3 n5 3', 'n3 n4 7', 'n4 n6 3', 'n4 n5 2', 'n5 n7 9', 'n5 n6 7', 'n6 n7 3']
G3 = nx.parse_edgelist(S3,data=(("weight",int),))
# .graphs/s-u-w-cy-sc-p-01.graphml
S4 = ['n0 n1 120', 'n0 n6 300', 'n0 n5 250', 'n1 n2 80', 'n1 n6 250', 'n2 n3 150', 'n2 n7 280', 'n3 n4 100', 'n3 n8 250', 'n4 n9 250', 'n5 n6 120', 'n5 n10 150', 'n6 n11 150', 'n6 n7 150', 'n7 n12 260', 'n7 n8 80', 'n8 n9 100', 'n9 n12 180', 'n10 n11 120']
G4 = nx.parse_edgelist(S4,data=(("weight",int),))

class Test_insep_blocks(unittest.TestCase):

  @parameterized.expand([
    ['Empty',nx.Graph(),0,[]],
    ['G1',G1,10,[['n1', 'n2', 'n0']]],
    ['G1_0',G1,0,[]],
    ['G2',G2,10,[['n0', 'n1', 'n3']]],
    ['G2_2',G2,2,[]],
    ['G3_7',G3,7,[['n4', 'n5', 'n6'], ['n4', 'n3', 'n5'], ['n0', 'n2', 'n1']]],
    ['G3_9',G3,9,[['n5', 'n7', 'n6'], ['n4', 'n5', 'n6'], ['n4', 'n3', 'n5'], 
['n4', 'n1', 'n3'], ['n0', 'n2', 'n1'], ['n4', 'n2', 'n1']]],
    ["G4_250",G4,250,[]],
    ["G4_300",G4,300,[['n0', 'n5', 'n6'], ['n0', 'n1', 'n6']]]  
  ])
  def test_base00 (self, name, G, limiar, expected_result):
    result = Q02.insep_blocks(G,limiar)
    self.assertEqual(len(result),len(expected_result))
    self.assertTrue(all(any(Counter(r)==Counter(e) for r in result) for e in expected_result))
    self.assertTrue(all(any(Counter(r)==Counter(e) for e in expected_result) for r in result))

  def test_edge00 (self):
     self.assertTrue(Q02.insep_blocks(None,10) is None)

  def test_edge01 (self):
     self.assertTrue(Q02.insep_blocks(nx.Graph(),None) is None)

  def test_edge02 (self):
     self.assertTrue(Q02.insep_blocks(nx.Graph(),-1) is None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
