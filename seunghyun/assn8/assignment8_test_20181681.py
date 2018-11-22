import unittest
from guess import Guess
from word import Word

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.w1 = Word
    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        print('display test ended')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        print('guessed test ended')

    def testfinished(self):
        t1 = Guess('a')
        self.assertEqual(t1.secretWord,'a')
        t2 = Guess('toomuchhomework')
        self.assertEqual(t2.secretWord,'toomuchhomework')
        t3 = Guess('chicken')
        self.assertEqual(t3.secretWord,'chicken')
        print('finished test ended')

    def testguess(self):
        self.assertFalse(self.g1.guess('k'),msg='There is no k')
        self.assertFalse(self.g1.guess('o'),msg='There is no o')
        self.assertFalse(self.g1.guess('p'),msg='There is no p')

        self.assertTrue(self.g1.guess('d'),msg='guess method error')
        self.assertTrue(self.g1.guess('e'),msg='guess method error')

        print('guess method test ended')

    def testInputIsAlpha(self):
        self.assertFalse(self.g1.guess('1'),msg='Please input Alphabet not integer')
        self.assertFalse(self.g1.guess('ㅂ'),msg='Please input Alphabet not korean')
        self.assertFalse(self.g1.guess('*'),msg='Please input Alphabet not symbol')
        print('input test ended')


    

if __name__ == '__main__':
    unittest.main()

