from sys import maxsize

def createStack():
    stack = []
    return stack

def push(stack,data):
    stack.append(data)
    print("Item pushed to stacked: " + str(data))

def isEmpty(stack):
    if(stack):
        return len(stack) == 0

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)

    return stack.pop()

def printStack(stack):
    for i in stack:
        print(i)

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
printStack(stack)
print(pop(stack) + " popped from stack")
printStack(stack)
