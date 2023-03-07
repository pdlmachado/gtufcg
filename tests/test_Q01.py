import unittest

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite

import src.Q01 as Q01

class Test_astronautas(ParametrizedTestCase):

  def test_valid01 (self):
    l=self.param
    #print(f"OIIIII {l}")
    G = Q01.associate_astronauts(l)
    #print(G)
    self.assertTrue(G.number_of_nodes()==len(l))

params = [[
        ('Kurtis','Shepstone','Italy'),
        ('Rafferty','Stoak','Canada'),
        ('Libbey','Anselm','Canada'),
        ('Odelinda','Thireau','Italy'),
        ('Rick','Caset','Canada'),
        ('Matthew','Fearnyough','Canada'),
        ('Madonna','Brazener','Canada'),
        ('Laure','Drohane','Canada'),
        ('Eleanore','Pollett','USA'),
        ('Town','Duddell','Canada')
    ]]
Test_ast_cases = [ParametrizedTestCase.parametrize(Test_astronautas, param=params[i]) for i in range(len(params))]
print("PASSEI")
suite = unittest.TestSuite()
for tc in Test_ast_cases:
    suite.addTest(tc)    
unittest.TextTestRunner(verbosity=2).run(suite)

#if __name__ == '__main__':
    #unittest.main()
#    pass