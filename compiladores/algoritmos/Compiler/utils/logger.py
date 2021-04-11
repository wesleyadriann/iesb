
# -*- coding: utf-8 -*-

import logging

def logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    s_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('logs.txt')
    formatter = logging.Formatter('[%(levelname)s][%(name)s]:: %(message)s')
    s_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    logger.addHandler(f_handler)

    return logger
