import unittest

from chart import *
from observer import *
from data import *

class TestObservableClass(unittest.TestCase):
    '''Test for base class, exist and exceptions'''
    def setUp(self):
        self.chart=Chart()

    def test_exc_update(self):
        self.assertRaises(NotImplementedError,self.chart.update)

    def test_exc_print(self):
        self.assertRaises(NotImplementedError, self.chart.print_chart)


class TestInheritance(unittest.TestCase):
    '''Good inheritance = Exception if functions dont definition'''
    def test_First(self):
        self.assertTrue(
            issubclass(First, Chart)
            )

if __name__=="__main__":
    unittest.main()

'''Write tests to observer and data classes'''
