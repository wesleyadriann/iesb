
# -*- coding: utf-8 -*-

from Ordinal import Ordinal
from Romano import Romano
from Arabico import Arabico

class CreateApp():
    def main(self):
        
        romano = Romano(35)
        arabico = Arabico(100)
        ordinal = Ordinal(999)
        
        romano.extenso()
        arabico.extenso()
        ordinal.extenso()
        
        romano.setNumero(330)
        arabico.setNumero(123)
        ordinal.setNumero(2)

        romano.extenso()
        arabico.extenso()
        ordinal.extenso()

if __name__ == '__main__':
    app = CreateApp()
    app.main()