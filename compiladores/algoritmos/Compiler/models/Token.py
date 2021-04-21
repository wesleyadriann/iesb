
# -*- coding: utf-8 -*-

class Token():
    def __init__(self, line, column, type_symbol, table_id):
        self.type = type_symbol
        self.table_id = table_id
        self.line = line
        self.column = column

    def __repr__(self):
        return f'[{self.type}, {self.table_id}, ({self.line}, {self.column})]'

