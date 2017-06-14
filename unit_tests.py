import unittest

from chart_abstract import *
from observer import *
from data import *
from chart import * #will remove in future


class Downloader():
    '''secondary class'''
    def update(self,arg):
        self.information=arg

    def print_chart(self):
        self.runned=True


class TestObservableClass(unittest.TestCase):
    '''Test for base class, exist and exceptions'''
    def setUp(self):
        self.chart=Chart()

    def test_exc_update(self):
        self.assertRaises(NotImplementedError,self.chart.update)

    def test_exc_print(self):
        self.assertRaises(NotImplementedError, self.chart.print_chart)


class TestObserverClass(unittest.TestCase):
    '''Tests for observer'''
    def setUp(self):
        self.observer=Observer()

    def test_list_atr(self):
        self.assertTrue(hasattr(self.observer,'observers'))

    def test_add_observer(self):
        one,two,three=0,1,2
        self.observer.add_observer(one)
        self.observer.add_observer(two)
        self.observer.add_observer(three)
        self.assertEqual(3, len(self.observer.observers))

    def test_attributs(self):
        self.assertTrue(hasattr(self.observer,'add_observer'))
        self.assertTrue(hasattr(self.observer,'remove_observer'))
        self.assertTrue(hasattr(self.observer,'send_information'))
        self.assertTrue(hasattr(self.observer,'send_finnally_information'))

    def test_add_unically_observer(self):
        one,two,three,four=0,1,0,1
        self.observer.add_observer(one)
        self.observer.add_observer(two)
        self.observer.add_observer(three)
        self.observer.add_observer(four)
        self.assertEqual(2, len(self.observer.observers))

    def test_remove(self):
        self.observer.add_observer(1)
        self.observer.remove_observer(1)
        self.assertEqual(0, len(self.observer.observers))

    def test_remove_if_exist(self):
        self.observer.add_observer(1)
        self.observer.remove_observer(0)
        self.assertEqual(1, len(self.observer.observers))

    def test_sending_inf(self):
        information='some information'
        downloader=Downloader()
        self.observer.add_observer(downloader)
        self.observer.send_information(information)
        self.assertEqual(information, downloader.information)
        self.observer.send_finnally_information()
        self.assertTrue(downloader.runned)


class TestDataClass(unittest.TestCase):
    '''Tests for Data class'''
    def test_wrong_initialization(self):
        self.assertRaises(SyntaxError,Data)

    def test_initialization(self):
        observer=Observer()
        data=Data(observer)
        self.assertEqual(observer, data.observer)

    def test_read_data_implement(self):
        observer=Observer()
        data=Data(observer)
        self.assertTrue(hasattr(data,'read_data'))
        '''functionality of this method will be checked later'''


class TestInheritance(unittest.TestCase):
    '''Good inheritance = Exception if functions arent definined'''
    def test_First(self):
        self.assertTrue(
            issubclass(First, Chart)
            )

if __name__=="__main__":
    unittest.main()
