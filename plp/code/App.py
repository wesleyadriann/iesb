
# -*- coding: utf-8 -*-

from fileReader import fileReader
from config import strings

class App():
    def __init__(self, path):
        self.filePath = path
        self.file = ''
        self.loadFile()
        self.errors = []

    def loadFile(self):
        self.file = fileReader(self.filePath)

    def initSyntax(self):
        print("--------------------------------")
        print("Validating syntax")
        print("--------------------------------")
        for i, line in enumerate(self.file):
            print(f"Validating line: \n - {line}")
            code = line.split(': ')
            validLabel = self.validLabel(code[0])
            if(not validLabel):
                self.errors.append(f'Error in line {i + 1} on \n - {code[0]} invalid label')
            validInstruction = self.validInstruction(code[1]) 
            if (validInstruction):
                print(validInstruction)
                self.errors.append(f'Error in line {i + 1} on \n{validInstruction}')
                # self.errors.append(validInstruction)

        print("--------------------------------")
        if(self.errors):
            print('\n'.join(self.errors))
        else:
            print('The Program Syntax is Valid')
        print("--------------------------------")

    def validLabel(self, label):
        print(f'method: validLabel, param: {label}')
        if label[0] != 'R':
            return False
        for i in range(1, len(label)):
            if(label[1] == "x"):
                print(f"        paramn: {label} is valid")
                return True
            if(not label[i].isnumeric()):
                return False
        print(f"        paramn: {label} is valid")
        return True

    def validInstruction(self, instruction):
        texts = instruction.split(' ')
        lineErros = []
        try:
            if(texts[0] == strings["do"]):
                validSubAOrAddB = self.validSubAOrAddB(texts[1])
                validSubAOrAddB = self.validSubAOrAddB(texts[1])
                validGoto = self.validGoto(texts[2])
                validLabel = self.validLabel(texts[-1][0:-1])
                validSemicolon = self.validSemicolon(texts[-1][-1])

                if(validSubAOrAddB):
                    lineErros.append(validSubAOrAddB)
                if(validGoto):
                    lineErros.append(validGoto)
                if(not validLabel):
                    lineErros.append(f" - {texts[-1][0:-1]} is invalid to label")
                if(validSemicolon):
                    lineErros.append(validSemicolon)

            if(texts[0] == strings["if"]):
                validVerifyA = self.validVerifyA(texts[1])
                validThen = self.validThen(texts[2])
                valid1Goto = self.validGoto(texts[3])
                valid1Label = self.validLabel(texts[4])
                validElse = self.validElse(texts[5])
                valid2Goto = self.validGoto(texts[6])
                valid2Label = self.validLabel(texts[-1][0:-1])
                validSemicolon = self.validSemicolon(texts[-1][-1])

                if(validVerifyA):
                    lineErros.append(validVerifyA)
                if(validThen):
                    lineErros.append(validThen)
                if(valid1Goto):
                    lineErros.append(valid1Goto)
                if(validElse):
                    lineErros.append(validElse)
                if(not valid1Label):
                    lineErros.append(f" - {texts[4]} is invalid to label")
                if(valid2Goto):
                    lineErros.append(valid2Goto)
                if(not valid2Label):
                    lineErros.append(f" - {texts[-1][0:-1]} is invalid to label")
                if(validSemicolon):
                    lineErros.append(validSemicolon)
                
        except:
            lineErros.append(f'\n - Error to valitated instruction \n  - {instruction}')
        
        return '\n'.join(lineErros)

    def validSubAOrAddB(self, string):
        print(f'method: validSubAOrAddB, param: {string}',)
        if(string != strings["sub_a"] and string != strings["add_b"]):
            return f" - {string} is invalid, subA or addB is missing"
        print(f"        paramn: {string} is valid")

    def validGoto(self, string):
        print(f'method: validGoto, param: {string}',)
        if(string != strings["goto"]):
            return f" - {string} is invalid, goto is missing"
        print(f"        paramn: {string} is valid")

    def validSemicolon(self, string):
        print(f'method: validSemicolon, param: {string}',)
        if(string != strings["semicolon"]):
            return f" - {string} is invalid, semicolon is missing"
        print(f"        paramn: {string} is valid")

    def validVerifyA(self, string):
        print(f'method: validVerifyA, param: {string}')
        if(string != strings["zero_a"]):
            return f" - {string} is invalid, zero_a comparation is missing"
        print(f"        paramn: {string} is valid")

    def validThen(self, string):
        print(f"method: validThen, param: {string}")
        if(string != strings["then"]):
            return f" - {string} is invalid, then is missing"
        print(f"        paramn: {string} is valid")

    def validElse(self, string):
        print(f"method: validElse, param: {string}")
        if(string != strings["else"]):
            return f" - {string} is invalid, else is missing"
        print(f"        paramn: {string} is valid")

