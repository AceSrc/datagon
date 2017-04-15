def Tokenizer(input):
    current = 0
    tokens = []
    print(input)
    while current < len(input):
        char = input[current]
        if char == '(':
            tokens.append({
                'type': 'paren',
                'value': '(',
            })
            current += 1
            continue
        
        if char == ')':
            tokens.append({
                'type': 'paren',
                'value': ')',
            })
            current += 1
            continue

        if char == '[':
            tokens.append({
                'type': 'paren',
                'value': '[',
            })
            current += 1
            continue

        if char == ']':
            tokens.append({
                'type': 'paren',
                'value': ']',
            })
            current += 1
            continue

        if char.islower():
            value = ''
            while char.islower() and current < len(input):
                value += char
                current += 1
                char = input[current]
            tokens.append({
                'type': 'string',
                'value': value,
            })
            continue
        
        if char.isdigit() or char == '-':
            value = char 
            current += 1
            while current < len(input):
                char = input[current]
                if not char.isdigit(): 
                    break
                value += char
                current += 1
            tokens.append({
                'type': 'number',
                'value': value,
            })
            continue
    
        if char == '\n':
            tokens.append({
                'type': 'format',
                'value': 'newline',
            })
            current += 1
            continue

        if char == '#':
            tokens.append({
                'type': 'format',
                'value': 'clearline',
            })
            current += 1
            continue
        
        if char == '=':
            tokens.append({
                'type': 'order',
                'value': '=',
            })
            current += 1
            continue
        
        if char == ',':
            tokens.append({
                'type': 'format',
                'value': ','
            })
            current += 1
            continue

        if char == ' ' or char == '\r':
            current += 1
            continue
        print("Invaild Syntax " + char)
        exit(1)
    return tokens
