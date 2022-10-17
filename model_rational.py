# x = 0
# y = 0

def init(a, b, c):
    global x
    global y
    global z
    x = a
    y = b
    z = c

def sum_rational(): 
    return x + y

def sub_rational(): 
    return x - y

def mult_rational(): 
    return x * y

def div_rational(): 
    return x / y

def write_File_rational(string, fileName):
    f = open(fileName, 'w')
    f.write(string)
    f.close()

