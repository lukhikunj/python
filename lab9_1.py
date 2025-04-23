
def fun():
    print("Function fun() is called")

def disp():
    print("Function disp() is called")

def msg():
    print("Function msg() is called")

functions = [fun, disp, msg]

for f in functions:
    f()
