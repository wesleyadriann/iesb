
class Symbol():
    code = dict({
        'LF': 10,
        'ETX': 3,
        '=': 11,
        '+': 21,
        '-': 22,
        '*': 23,
        '/': 24,
        '%': 25,
        '==': 31,
        '!=': 32,
        '>': 33,
        '<': 34,
        '>=': 35,
        '<=': 36,
        'var': 41,
        'int': 51,
        'rem': 61,
        'input': 62,
        'let': 63,
        'print': 64,
        'goto': 65,
        'if': 66,
        'end': 67,
        'error': 99
    })

    def __init__(self, uid):
        self.uid = uid
