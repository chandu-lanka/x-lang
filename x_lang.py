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
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def printError(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

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
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text
        self.pos = Position(-1, 0, -1, file_name, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

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
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

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

## Nodes ##
class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'

def run(file_name, text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()

    return tokens, error