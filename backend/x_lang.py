## Tokens ##
X_INT = 'INT'
X_FLOAT = 'FLOAT'
X_PLUS = 'PLUS'
X_MINUS = 'MINUS'
X_MULTIPLY = 'MULTIPLY'
X_DIVIDE = 'DIVIDE'
X_LEFT_PARENTHESE = 'LEFT_PARENTHESE'
X_RIGHT_PARENTHESE = 'RIGHT_PARENTHESE'

## Constants ##
digits = '0123456789'

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
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\t':
                self.advance()

            elif self.current_char in digits:
                tokens.append(self.make_number())

            elif self.current_char == "+":
                tokens.append(Token(X_PLUS))
                self.advance()

            elif self.current_char == "-":
                tokens.append(Token(X_MINUS))
                self.advance()

            elif self.current_char == "*":
                tokens.append(Token(X_MULTIPLY))
                self.advance()

            elif self.current_char == "/":
                tokens.append(Token(X_DIVIDE))
                self.advance()

            elif self.current_char == "(":
                tokens.append(Token(X_LEFT_PARENTHESE))
                self.advance()

            elif self.current_char == ")":
                tokens.append(Token(X_RIGHT_PARENTHESE))
                self.advance()
        return tokens

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in digits + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char

        if dot_count == 0:
            return Token(X_INT, int(num_str))
        else:
            return Token(X_FLOAT, float(num_str))