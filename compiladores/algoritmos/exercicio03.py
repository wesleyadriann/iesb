
# -*- coding: utf-8 -*-

class Compiler():
    token_index = 0
    tokens = ''
    current_token = ''
    called_states = []

    def next_token(self, state):
        print(f'q{state} `{self.tokens[self.token_index]}` - ', end='')
        self.token_index = self.token_index + 1
        self.current_token = self.tokens[self.token_index]
        print(f'`{self.tokens[self.token_index:]}`')

    def remove_spaces(self, tokens):
        if(' ' in tokens):
            return ''.join(tokens.split(' '))
        return tokens

    def add_in_called_state(self, state):
        self.called_states.append(f'<q{state} `{self.tokens[self.token_index]}`>')

    def qA(self):
        self.add_in_called_state('A')
        return self.qB() and self.qD()

    def qB(self):
        self.add_in_called_state('B')
        return self.qC() and self.qE()

    def qC(self):
        self.add_in_called_state('C')
        if('x' == self.current_token):
            self.next_token('C')
            return True

        if('~' == self.current_token):
            self.next_token('C')
            return self.qC()

        if('(' == self.current_token):
            self.next_token('C')
            if(self.qA()):
                if(')' == self.current_token):
                    self.next_token('C')
                    return True
                return False
            return False
        return False

    def qD(self):
        self.add_in_called_state('D')
        if('v' == self.current_token):
            self.next_token('D')
            return self.qB() and self.qD()
        return (')' == self.current_token
                or '$' == self.current_token)

    def qE(self):
        self.add_in_called_state('E')
        if('&' == self.current_token):
            self.next_token('E')
            return self.qC() and self.qE()

        return (')' == self.current_token
                or 'v' == self.current_token
                or '$' == self.current_token)

    def parse(self, tokens):
        tokens = self.remove_spaces(tokens)
        self.tokens = f'{tokens}$'
        self.current_token = tokens[0]
        self.result(self.qA() and self.current_token == '$')

    def result(self, is_valid):
        print(f'Estados chamados: {" | ".join(self.called_states)}')
        if(is_valid):
            return print('Análise concluída com sucesso!')
        print('Análise concluída com erro!')


if(__name__ == '__main__'):
    Compiler().parse('x & x v (x & ~x)')
