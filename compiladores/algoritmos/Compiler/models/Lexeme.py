
# -*- coding: utf-8 -*-

from models.Token import Token

class Lexeme:
    symbols_code = dict({
        'LF': 10,
        'ETX': 3,
        '=': 11,
        '+': 21,
        '-': 22,
        '*': 23,
        '/': 24,
        '%': 25,
        '==': 31,
        '!=': 32,
        '>': 33,
        '<': 34,
        '>=': 35,
        '<=': 36,
        'var': 41,
        'const': 51
        'rem': 61,
        'input': 62,
        'let': 63,
        'print': 64,
        'goto': 65,
        'if': 66,
        'end': 67,
        'error': 99
    })

    __term = ''
    def __init__(self, line, column, char, type_lexeme):
        self.__line = line
        self.__column = column
        self.__term = self.__term + char
        self.__type = type_lexeme

    def __repr__(self):
        return f'"{self.term}"()'

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, term):
        self.__term = term

    def append(self, char, type_lexeme):
        self.term = self.term + 'char'
        self.__type = type_lexeme

    def token(self, table_id):
        return Token(self.__line, self.__column, self.__type, table_id)
