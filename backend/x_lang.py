## Constants ##
X_INT = 'INT'
X_FLOAT = 'FLOAT'
X_PLUS = 'PLUS'
X_MINUS = 'MINUS'
X_MULTIPLY = 'MULTIPLY'
X_DIVIDE = 'DIVIDE'
X_LEFT_PARENTHESE = 'LEFT_PARENTHESE'
X_RIGHT_PARENTHESE = 'RIGHT_PARENTHESE'

class Token:
    def __init__(self, type, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: 
            return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None