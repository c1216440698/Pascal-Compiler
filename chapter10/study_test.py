from spi import Token
import unittest
from study_spi import Lexer

class LexerTestCase(unittest.TestCase):
    def makeLexer(self, text):
        lexer = Lexer(text)
        return lexer

    def test_tokens(self):
        from study_spi import (
            INTEGER_CONST, REAL_CONST, MUL, INTEGER_DIV, FLOAT_DIV, PLUS, MINUS, LPAREN, RPAREN,
            ASSIGN, DOT, ID, SEMI, BEGIN, END
        )
        records = (
            ('234', INTEGER_CONST, 234),
            ('3.14', REAL_CONST, 3.14),
            ('*', MUL, '*'),
            ('DIV', INTEGER_DIV, 'DIV'),
            ('/', FLOAT_DIV, '/'),
            ('+', PLUS, '+'),
            ('-', MINUS, '-'),
            ('(', LPAREN, '('),
            (')', RPAREN, ')'),
            (':=', ASSIGN, ':='),
            ('.', DOT, '.'),
            ('number', ID, 'number'),
            (';', SEMI, ';'),
            ('BEGIN', BEGIN, 'BEGIN'),
            ('END', END, 'END'),
        )
        for text, tok_type, tok_val in records:
            lexer = self.makeLexer(text)
            token = lexer.get_next_token()
            self.assertEqual(token.type, tok_type)
            self.assertEqual(token.value, tok_val)

from study_spi import EOF
def main():
    import sys
    text = open(sys.argv[1], 'r').read()

    lexer = Lexer(text)
    token = lexer.get_next_token()
    while token.type != EOF:
        print(repr(token))
        token = lexer.get_next_token()
    print(repr(token))

if __name__ == '__main__':
    main()        



