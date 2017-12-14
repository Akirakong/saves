# coding:utf-8
import unittest
import saves

TESTTABLE = 'test'

class Testsaves(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        cls.s = saves.Saves(TESTTABLE)

    def setUp(self):
        print('setup')
        self.s.clean()

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        cls.s.drop(TESTTABLE)

    def test_save(self):
        self.s.save('s', 'string')
        self.s.save('n', 9999)
        self.s.save('l', [1, 2, 3, 4])
        self.s.save('d', {'key': 123, 'key2': 456})
        self.s.save('t', (123, 456, 789))

        lst = self.s.keys()
        self.assertEqual(len(lst),5)

    def test_load(self):
        self.s.save('s','string')
        self.s.save('n',9999)
        self.s.save('l',[1,2,3,4])
        self.s.save('d',{'key':123,'key2':456})
        self.s.save('t',(123,456,789))

        s = self.s.load('s')
        self.assertTrue(isinstance(s,str))

        n = self.s.load('n')
        self.assertTrue(isinstance(n, int))

        l = self.s.load('l')
        self.assertTrue(isinstance(l, list))

        d = self.s.load('d')
        self.assertTrue(isinstance(d, dict))

        t = self.s.load('t')
        self.assertTrue(isinstance(t, tuple))

    def test_clean(self):
        self.s.clean()
        r = self.s.load('hoge')
        self.assertEqual(len(r),0)

    def test_keys(self):
        self.s.save('s', 'string')
        self.s.save('n', 9999)
        self.s.save('l', [1, 2, 3, 4])
        self.s.save('d', {'key': 123, 'key2': 456})
        self.s.save('t', (123, 456, 789))

        l = self.s.keys()
        self.assertEqual(len(l),5)

