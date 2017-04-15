import sys, os
from datagon import *

def PrintUsage() :
    print(
    """Usage: datagon command [arguments]
    Supported commands: """ + ', '.join(sorted([k for k in COMMANDS]))
    )
    exit(1)

def main() :
    if len(sys.argv) < 2: PrintUsage()
    
    cmd = sys.argv[1]
    if cmd not in COMMANDS: 
        mod = __import__('datagon.generator.generator', fromlist=[''])
        func = mod.__dict__['GenerateData']
        func(sys.argv[1:])
        return 

    f = ['datagon'] + COMMANDS[cmd].split('.')
    mod = __import__('.'.join(f[:-1]), fromlist=[''])
    func = mod.__dict__[f[-1]]

    args = sys.argv[2:]
    func(args)
