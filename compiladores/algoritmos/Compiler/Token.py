
# -*- coding: utf-8 -*-

class Token():
    def __init__(self):
        self.type = ''
        self.table_id = ''
        self.linha = ''
        self.coluna = ''

    def __repr__(self):
        return f'[{self.type}, {self.table_id}, ({self.linha}, {self.coluna})]'

