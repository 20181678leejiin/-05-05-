import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('happy')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ ')
        self.g1.guess('h')
        self.assertEqual(self.g1.displayCurrent(), 'h _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), 'h a _ _ _ ')
        self.g1.guess('p')
        self.assertEqual(self.g1.displayCurrent(), 'h a p p _ ')
        self.g1.guess('z')
        self.assertEqual(self.g1.displayCurrent(), 'h a p p _ ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), '')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), 'a ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), 'a t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), 'a t u ')

if __name__ == '__main__':
    unittest.main()