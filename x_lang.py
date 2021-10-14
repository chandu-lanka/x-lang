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

## Errors ##
class Error:
    def __init__(self, errorName, details):
        self.errorName = errorName
        self.details = details

    def printError(self):
        print_error = f'{self.errorName}: {self.details}'
        return print_error

class UndefinedCharacter(Error):
    def __init__(self, details):
        super().__init__('Undefined Character', details)

## X Lang ##
class Token:
    def __init__(self, type_of_token, value=None):
        self.type_of_token = type_of_token
        self.value = value

    def __repr__(self):
        if self.value: 
            return f'{self.type_of_token}:{self.value}'
        return f'{self.type_of_token}'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
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
            
            else:
                char = self.current_char
                self.advance()
                return [], UndefinedCharacter("'" + char + "'")

        return tokens, None

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
            self.advance()

        if dot_count == 0:
            return Token(X_INT, int(num_str))
        else:
            return Token(X_FLOAT, float(num_str))

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error