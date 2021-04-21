
# -*- coding: utf-8 -*-

from sys import argv, exc_info

from utils.logger import logger
from SyntaxAnalisys import SyntaxAnalisys
from LexicalAnalysis import LexicalAnalysis

log = logger('Compiler')

class Compiler():
    file_path = ''
    file_content = ''

    def main(self, file):
        self.file_path = file_path
        self.read_file()
        self.lexical_analysis()

    def lexical_analysis(self):
        log.info('inicio da analise lexica')
        lexical_analysis = LexicalAnalysis().parser(self.file_content)

    def syntax_analisys(self):
        syntax_analisys = SyntaxAnalisys().main()

    def semantic_analysis(self):
        pass

    def read_file(self):
        file_r = open(self.file_path , "r")
        self.file_content = file_r.read()
        file_r.close()

if (__name__ == '__main__'):
    file_path = None
    try:
        file_path = argv[1]
    except IndexError:
        log.error('Informe o nome do arquivo a ser compilado')
        log.error('Exemplo: ')
        log.error('python3 Compiler.py simple.txt')
        exit(1)
    Compiler().main(file_path)
