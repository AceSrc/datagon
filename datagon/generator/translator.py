import parser
import random

result = ''
symbol = {}
cnt = 0

def Translator(ast):
    def PrintError(x):
        print(x)
        exit(1)

    def PrintMsg(x):
        print(x)

    def Output(x):
        global result
        result += str(x) + ' '

    def GetRandomInt(interval):
        if isinstance(interval, str):
            PrintError('Error: ' + interval)
        if isinstance(interval, int):
            return interval
        if interval[0] > interval[1]:
            print('!!! Invaild Interval ')
            exit(1)
        rt = random.randint(interval[0], interval[1])
        return rt
    
    def AddPermutation(interval):
        n = GetRandomInt(interval)
        p = [i for i in range(1, n + 1)]
        random.shuffle(p)
        global result
        for i in p:
            result += str(i) + ' '
        return None

    def Add(a, b):
        return GetRandomInt(a) + GetRandomInt(b)
    
    def Mul(a, b):
        return GetRandomInt(a) + GetRandomInt(b)
    
    def Sub(a, b):
        return GetRandomInt(a) + GetRandomInt(b)

    def AddWeight(n, interval):
        n = GetRandomInt(n)
        for i in range(0, n):
            Output(GetRandomInt(interval))    

    def RepeatOutput(node):
        times = TranslateNode(node.params[0], node)
        for i in range(0, times):
            TranslateArray(node)
            AddNewLine()

    def HandleFunction(node):
        print('handling function: ' + node.type)
        print(node.params)
        cases = {
            'print': lambda x: Output(GetRandomInt(TranslateNode(node.params[0], x))),
            'add': lambda x: Add(TranslateNode(x.params[0], x), TranslateNode(x.params[1], x)),
            'sub': lambda x: Sub(TranslateNode(x.params[0], x), TranslateNode(x.params[1], x)), 
            'mul': lambda x: Mul(TranslateNode(x.params[0], x), TranslateNode(x.params[1], x)),
            'permutation': lambda x: AddPermutation(TranslateNode(x.params[0], x)),
            'weight': lambda x: AddWeight(TranslateNode(x.params[0], x), TranslateNode(x.params[1], x)),
            'repeat': lambda x: RepeatOutput(x),
            'set': lambda x: SetVariableValue(x.params[0].name, TranslateNode(x.params[1], x))
        }
        return cases.get(node.type, lambda x: None)(node)

    def AddNewLine():
        global cnt
        cnt += 1
        if cnt <= 0: 
            return 
        cnt -= 1
        global result
        result += '\n'

    def CleanLine():
        print("Clean")
        global cnt
        cnt -= 1

    def HandleFormat(node):
        print("Handling Format: " + node.value)
        cases = {
            'newline': lambda x: AddNewLine(),
            'clearline': lambda x: CleanLine(),
        }
        return cases.get(node.value, lambda x: None)(node)

    def GetVariableValue(name):
        return symbol.get(name, name)

    def SetVariableValue(name, value):
        value = GetRandomInt(value)
        symbol[name] = value
        print('Set variable: ' + str(name) + ' = ' + str(symbol[name]))
        return symbol[name]

    def TranslateArray(node):
        for x in node.params:
            TranslateNode(x, node)

    def TranslateNode(node, parent):
        cases = {
            parser.Function: lambda x: HandleFunction(x),
            parser.Number: lambda x: x.value,
            parser.Interval: 
                lambda x: [TranslateNode(x.left, x) + x.leftoffset, TranslateNode(x.right, x) + x.rightoffset],
            parser.String: lambda x: GetVariableValue(x.name),
            parser.Setvar: lambda x: SetVariableValue(x),
            parser.Program: lambda x: TranslateArray(x),
            parser.Format: lambda x: HandleFormat(x),
        }
        return cases.get(node.__class__, lambda x: None)(node)
    
    TranslateArray(ast)
    return result 
