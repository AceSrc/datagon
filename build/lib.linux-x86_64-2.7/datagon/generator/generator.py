import sys, os
import tokenizer
import parser
import translator

def GenerateData(argv):
    savedStdout = sys.stdout
    file = open('.datagon.log', 'w')
    sys.stdout  = file

    print('------ Starting Generating Data. ------')
    f = open(os.path.join(os.getcwd(), argv[0]), 'r')
    tokens = tokenizer.Tokenizer(f.read())
    ast = parser.Parser(tokens)
    result = translator.Translator(ast)
    
    sys.stdout = savedStdout
    if len(argv) > 1:
        with open(argv[1], 'w') as file:
            file.write(result)
    else:
        print(result)
    
    
    
if __name__ == '__main__':
    GenerateData(sys.argv[1:])
