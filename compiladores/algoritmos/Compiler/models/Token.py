
# -*- coding: utf-8 -*-

class Token():
    tokens_codes = dict({
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
    })

    def __init__(self, line, column, value, table_id = ''):
        self.type = tokens_codes[value]
        self.table_id = table_id
        self.line = line
        self.column = column


    def __repr__(self):
        return f'[{self.type}, {self.table_id}, ({self.line}, {self.column})]'

    def define_type(self, value):
        try:
            self.type = tokens_codes[value]
        except KeyError:
            numeric = int(value)
            self.type = tokens_codes['const']
        except ValueError:
            self.type = tokens_codes['var']



