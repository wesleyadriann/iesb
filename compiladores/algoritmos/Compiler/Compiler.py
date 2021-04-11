
# -*- coding: utf-8 -*-

from sys import argv

from utils.logger import logger
from SyntaxAnalisys import SyntaxAnalisys
from LexicalAnalysis import LexicalAnalysis

log = logger('Compiler')

class Compiler():
    file_path = ''
    file_content = []

    def main(self, file):
        self.file_path = file_path
        self.read_file()
        self.lexical_analysis()

    def lexical_analysis(self):
        lexical_analysis = LexicalAnalysis().main()

    def syntax_analisys(self):
        syntax_analisys = SyntaxAnalisys().main()

    def semantic_analysis(self):
        pass

    def read_file(self):
        file_r = open(self.file_path , "r")
        file_content = file_r.read()
        file_r.close()
        self.file_content = file_content.split('\n')

if (__name__ == '__main__'):
    file_path = argv[1]
    Compiler().main(file_path)
