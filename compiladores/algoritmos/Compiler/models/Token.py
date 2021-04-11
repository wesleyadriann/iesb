
# -*- coding: utf-8 -*-

class Token():

    def __init__(self, line, column, type_token, table_id = ''):
        self.type = type_token
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
