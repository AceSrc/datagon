class Number:
    def __init__(self, value=0, offset=0):
        self.value = value

class String:
    def __init__(self, name):
        self.name = name

class Function:
    def __init__(self, type, params):
        self.type = type
        self.params = params

class Interval:
    def __init__(self, left=Number(), right=Number(), leftoffset=0, rightoffset=0):
        self.left = left
        self.right = right 
        self.leftoffset = leftoffset
        self.rightoffset = rightoffset

class Program:
    def __init__(self, params):
        self.params = params

class Format:
    def __init__(self, value=''):
        self.value = value

class Setvar:
    def __init__(self, name='', value=None):
        self.name = name
        self.value = value

current = 0
def Parser(tokens):
    def Walk():
        global current
        if current >= len(tokens):
            print('------ current >= len(tokens) ------')
            exit(1)
        token = tokens[current]
        print('Processing token ' + str(current) + ' : ' + str(token))
        if token['value'] == ')' or token['value'] == ']':
            print('------ Extra enclosed ' + token['value'] + ' ------')
            exit(1)
        if token['type'] == 'number':
            current += 1
            return Number(int(token['value']))

        if token['type'] == 'string':
            current += 1
            if current < len(tokens) and tokens[current]['value'] == '(':
                current += 1
                rt = Function(token['value'], [])
                while current < len(tokens) and tokens[current]['value'] != ')':
                    rt.params.append(Walk())
                if not (current < len(tokens) and tokens[current]['value'] == ')'):
                    print('------ Invaild string: not closed paren ------')
                    exit(1)
                current += 1
                return rt
            else:
                if tokens[current]['value'] == '=':
                    current += 1
                    return Setvar(tokens[current - 2]['value'], Walk())
                return String(token['value'])
        
        if token['value'] == '(' or token['value'] == '[':
            tmp = token
            current += 1
            print('    Type: Interval')
            rt = Interval(Walk(), Walk())
            if current >= len(tokens) or (tokens[current]['value'] != ')' and tokens[current]['value'] != ']'): 
                print('------ Invaild Interval: not closed paren ------')
                exit(1)
            if tmp['value'] == '(':
                rt.leftoffset = 1
            else:
                rt.leftoffset = 0
            
            if tokens[current]['value'] == ')':
                rt.rightoffset = -1
            else:
                rt.rightoffset = 0
            current += 1
            return rt
        
        if token['value'] == ',':
            current += 1
            return Walk()
        if token['type'] == 'format':
            current += 1
            return Format(token['value'])
    
    ast = Program([])
    while current < len(tokens):
        ast.params.append(Walk())
    return ast
