
# -*- coding: utf-8 -*-

from models.Token import Token
from models.TokenList import TokenList
from models.Symbolslist import Symbolslist

class LexicalAnalysis:
    def ___init__(self, file_content):
        self.file_content = file_content
        self.token_list = TokenList()

    def __repr__(self):
        return f'[{self.type}, {self.table_id}, ({self.line}, {self.column})]'

    def main(self):
        for line, content in enumerate(self.file_content):
            for column, item in enumerate(content.split(' ')):
                token = Token()
