# x = 0
# y = 0

def init(a, b, c):
    global x
    global y
    global z
    x = complex(a[0],a[1])
    y = complex(b[0],b[1])
    z = c

    
    

def sum_kpl(): 
    return x + y

def sub_kpl(): 
    return x - y

def mult_kpl(): 
    return x * y

def div_kpl(): 
    return x / y

def wrire_resalt(arg1, arg2, sing, res):
    with open ('file.txt', 'w') as data:
        data.write(f'{arg1} {sing} {arg2} = {res}')