import parser
def Traverser(ast, visitor):
    def TraverseArray(array, parent):
        for child in array:
            TraverseNode(child, parent)
    
    def TraverseNode(node, parent):
        methods = visitor.get(node.__class__, None)
        
        if methods and methods.enter:
            methods.enter(node, parent)
        
        cases = {
            parser.Program: 
                lambda x: TraverseArray(x.params, x),
            parser.Function:
                lambda x: TraverseArray(x.params, x),
            parser.Number: 
                lambda x: x,
            parser.Interval:
                lambda x: x,
            parser.String:
                lambda x: x,
            parser.Format:
                lambda x: x,
        }
        cases.get(node.__class__, lambda x: exit(1))(node)

    TraverseNode(ast, None)
