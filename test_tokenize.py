import unittest
import shunting_yard as sy
import math

class TokenizeTest(unittest.TestCase):
    def test_single_operator(self):
        tokens = list(sy.tokenize('1+2'))
        self.assertListEqual(tokens, ['1', '+', '2'])
    def test_Multiple_operator(self):
        tokens = list(sy.tokenize('1/2*3'))
        self.assertListEqual(tokens, ['1', '/', '2', '*', '3'])
    def test_huge_number(self):
        tokens = list(sy.tokenize('10000000000000000000000000000000000000000000000000000000000000000000000000000000*2'))
        self.assertListEqual(tokens, ['10000000000000000000000000000000000000000000000000000000000000000000000000000000', '*', '2'])
    def test_isDigit(self):
        tokens = sy.isDigit('3')
        self.assertEqual(tokens, True)
        tokens = sy.isDigit('f')
        self.assertEqual(tokens, False)
    def test_isNumber(self):
        #decimal digit
        tokens = sy.isNumber('450.5')
        self.assertEqual(tokens, True)
        #non decimal digit
        tokens = sy.isNumber('450')
        self.assertEqual(tokens, True)
        tokens = sy.isNumber('fs')
        self.assertEqual(tokens, False)
    def test_isLeftBracket(self):
        token = sy.isLeftBracket('[')
        self.assertEqual(token, True)
        token = sy.isLeftBracket('(')
        self.assertEqual(token, True)
        token = sy.isLeftBracket(' ')
        self.assertEqual(token, False)
    def test_isRightBracket(self):
        token = sy.isRightBracket(']')
        self.assertEqual(token, True)
        token = sy.isRightBracket(')')
        self.assertEqual(token, True)
        token = sy.isRightBracket(' ')
        self.assertEqual(token, False)
    def test_appendToOutput(self):
        token = sy.appendToOutput('10','+')
        self.assertEqual(token, '10 +')
    def test_Precedence(self):
        token = sy.comparePrecedence('*', '+')
        self.assertEqual(token, 1)
        token = sy.comparePrecedence('-', '/')
        self.assertEqual(token, -1)
    def test_infixToPostfix(self):
        token = sy.infixToPostfix('1 * (2 + 3 * 4) + 5')
        self.assertEqual(token, '1 2 3 4 * + * 5 +')
