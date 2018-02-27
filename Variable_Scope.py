#Global scope

a = 100

def variable_scope(a):
    #a = 36
    print(a)

def another_function():
    print(a)


variable_scope(234)
another_function()
