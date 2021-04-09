
# -*- coding: utf-8 -*-

class SymbolsList():
    symbols_list = []

    def add(self, symbol):
        index = 0
        try:
            index = symbols_list.index(symbol)
        except ValueError:
            index = len(symbols_list)
            self.symbols_list.append(symbol)
        return index
