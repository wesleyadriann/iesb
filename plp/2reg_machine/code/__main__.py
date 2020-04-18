
# -*- coding: utf-8 -*-

import os, sys
from App import App

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    path = ''
    try:
        path = argv[1]
    except:
        path = '2r_program.txt'
    app = App(path)
    
    main = App(path) 
    main.initSyntax()