
# -*- coding: utf-8 -*-

import re

from models import Lexeme, Symbol
from utils import logger

log = logger.logger(__name__)
Lexeme = Lexeme.Lexeme
Symbol = Symbol.Symbol

class LexicalAnalysis:
    token_list = []
    symbols_table = dict()
    has_error = False
    line = 1
    column = 0
    source = ''
    lexeme = None

    def ___init__(self, file_content):
        self.file_content = file_content

    def __repr__(self):
        return f'[{self.type}, {self.table_id}, ({self.line}, {self.column})]'

    def add_symbols_table(self, lexeme):
        if(lexeme not in self.symbols_table):
            self.symbols_table["lexeme"] = len(self.symbols_table)
        return self.symbols_table.get(lexeme)

    def add_token_list():
        if(lexeme.type != 'error'):
            # if(lexeme.type)
            self.token_list.append(
                lexeme.token(lexeme.type)
            )
        else:
            print(f'token não reconhecido: {lexeme}')
            return False

    def next_char(self):
        char = 0
        if(self.source != None):
            char = self.source[0:1]
            self.source = self.source[1:]

        if(char):
            self.column += 1
            return char
        else:
            self.source = None

        return 0

    def parser(self, source):
        self.source = source
        while(self.source != None):
            self.q0()
        return self


    def q0(self):
        log.info('q0')
        char = self.next_char()
        symbol_type = None
        next_state = None
        if(char == 0): next_state = self.q4
        if(char == '\n'): next_state = self.q3
        if(re.findall('\d', f'{char}')):
            symbol_type = Symbol.code['int']
            next_state = self.q1
        if(re.findall('[a,b,c,d,f,h,j,k,m,n,o,q,s,t,u,v,w,x,y,z]', f'{char}')):
            symbol_type = Symbol.code['var']
            next_state = self.q2
        if(char == 'r'):
            symbol_type = Symbol.code['var']
            # next_state = self.q14
        if(char == 'i'):
            symbol_type = Symbol.code['var']
            # next_state = self.q16
        if(char == 'l'):
            symbol_type = Symbol.code['var']
            # next_state = self.q20
        if(char == 'p'):
            symbol_type = Symbol.code['var']
            # next_state = self.q22
        if(char == 'g'):
            symbol_type = Symbol.code['var']
            # next_state = self.q26
        if(char == 'e'):
            symbol_type = Symbol.code['var']
            # next_state = self.q29
        if(re.findall('[+,-,*,/,%]', f'{char}')):
            symbol_type = Symbol.code[char]
            next_state = self.q05
        if(char == '='):
            symbol_type = Symbol.code['=']
            # next_state = self.q06
        if(char == '<'):
            symbol_type = Symbol.code['<']
            # next_state = self.q07
        if(char == '>'):
            symbol_type = Symbol.code['>']
            # next_state = self.q08
        if(char == '!'):
            symbol_type = Symbol.code['error']
            # next_state = self.q13
        if(char != ' ' and not symbol_type and not next_state):
            symbol_type = symbol_type = Symbol.code['error']
            next_state = self.q99

        if(char != ' '):
            self.lexeme = Lexeme(self.line, self.column, char, symbol_type)
            next_state()

    def q1(self):

        pass

    def q2(self):
        pass

    def q3(self):
        pass

    def q4(self):
        pass
