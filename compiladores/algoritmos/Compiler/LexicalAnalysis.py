
# -*- coding: utf-8 -*-

from models.Token import Token
from models.SymbolsList import SymbolsList

from utils.logger import logger

log = logger(__name__)

class LexicalAnalysis:
    token_list = []
    symbols_list = SymbolsList()
    has_error = False

    def ___init__(self, file_content):
        self.file_content = file_content
        self.token_list = TokenList()

    def __repr__(self):
        return f'[{self.type}, {self.table_id}, ({self.line}, {self.column})]'

    def q0(self):
        pass

    def parser(self, source):
        pass

    def main(self):
        log.info('start')
        return self
        # print
        # for line, content in enumerate(self.file_content):
        #     for column, item in enumerate(content.split(' ')):
        #         token = Token()
