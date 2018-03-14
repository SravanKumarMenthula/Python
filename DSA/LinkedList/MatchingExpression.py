class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, data):
        new_node = Node(data)
        new_node.next = None
        self.head = None

    def pop(self):
        if(self.isEmpty()):
            print("Empty Stack")
            return 0
        temp = self.head
        self.head = temp.next
        return temp.data


def Check(a,b):
    if(a == '{' and b == '}'):
        return 1
    if(a == '[' and b == ']'):
        return 1
    if(a == '(' and b == ')'):
        return 1
    return 0

def checkExpression(expression):
    logic = 1
    length = len(expression)
    stack = Stack()
    while(i>0):
        if(expression[i] =='{' or expression[i] == '(' or  expression[i] =='[' ):
            stack.push(expression[i])
        if(expression[i] =='}' or expression[i] == ')' or  expression[i] ==']' ):
            if(Check(expression[i],stack.pop())!=1):
                print('Not Balanced')
                return 0
        i = i+1
    return 1
if __name == '__main__':

    s = '{()}[]'

    if(checkExpression(s)==1):
        print("Ok")
    else:
        print('Not')
