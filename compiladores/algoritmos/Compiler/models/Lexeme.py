
# -*- coding: utf-8 -*-

from models.Token import Token

class Lexeme:
    def __init__(self, line, column, char, type_symbol):
        self.line = line
        self.column = column
        self.term = char
        self.type = type_symbol

    def __repr__(self):
        return f"'{self.term}' ({self.line}, {self.column})"

    def append(self, char, type_symbol):
        self.term = self.term + char
        self.type = type_symbol

    def token(self, table_id = ''):
        return Token(self.line, self.column, self.type, table_id)
