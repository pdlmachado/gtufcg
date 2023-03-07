import unittest

#class ParametrizedTestCase(unittest.TestCase):
#    """ TestCase classes that want to be parametrized should
#        inherit from this class.
#    """
#    def __init__(self, methodName='runTest', param=None):
#        super(ParametrizedTestCase, self).__init__(methodName)
#        self.param = param

#    @staticmethod
#    def parametrize(testcase_klass, param=None):
#        """ Create a suite containing all tests taken from the given
#            subclass, passing them the parameter 'param'.
#        """
#        testloader = unittest.TestLoader()
#        testnames = testloader.getTestCaseNames(testcase_klass)
#        suite = unittest.TestSuite()
#        for name in testnames:
#            suite.addTest(testcase_klass(name, param=param))
#        return suite

import networkx as nx
import src.Q01 as Q01
from parameterized import parameterized

class Test_astronautas(unittest.TestCase):

  @parameterized.expand([
     ['Trivial',[('a','b','c')],0],
     ['One Country',[('a1','b1','c'),('a2','b2','c'),('a3','b3','c')],0],
     ['All Diff Country',[('a1','b1','c1'),('a2','b2','c2'),('a3','b3','c3')],3],
     ['Manual Test', [('Kurtis','Shepstone','Italy'),
                      ('Rafferty','Stoak','Canada'),
                      ('Libbey','Anselm','Canada'),
                      ('Odelinda','Thireau','Italy'),
                      ('Rick','Caset','Canada'),
                      ('Matthew','Fearnyough','Canada'),
                      ('Madonna','Brazener','Canada'),
                      ('Laure','Drohane','Canada'),
                      ('Eleanore','Pollett','USA'),
                      ('Town','Duddell','Canada')],23],
     ['Empty',[],0] 
  ])
  def test_base00 (self, name, alist, nedges):
    G = Q01.associate_astronauts(alist)
    self.assertEqual(G.number_of_nodes(),len(alist))
    self.assertEqual(G.number_of_edges(),nedges)
    self.assertTrue(all(G.nodes[e[1]]['country'] != G.nodes[e[0]]['country'] for e in G.edges))
    self.assertTrue(all(any(G.nodes[i]['last_name']==l and G.nodes[i]['first_name']==f and G.nodes[i]['country']==c for i in G.nodes) for f,l,c in alist))

  def test_edge00 (self):
     self.assertTrue(Q01.associate_astronauts(None) is None)

if __name__ == '__main__':
    unittest.main(verbosity=2)