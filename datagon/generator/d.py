current = 0

def f():
    global current
    if current == 50:
        return 
    print(current)
    current += 1
    f()

f()
