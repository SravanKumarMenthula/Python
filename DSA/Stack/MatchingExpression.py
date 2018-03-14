class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def isEmpty(self):
        return self.head == None

    def pop(self):
        if(self.isEmpty()):
            print("Empty Stack")
            return 5
        temp = self.head
        self.head = temp.next
        return temp.data



def checkExpression(exp):
    stack = Stack()
    print(exp)
    i=0
    for i in range(len(exp)):
        if(exp[i]=='{' or exp[i] == '(' or exp[i] == '['):
            stack.push(exp[i])
        if(exp[i]=='}' or exp[i] == ')' or exp[i] == ']'):
            if(stack.isEmpty()):
                return 0
            elif (Check(stack.pop(),exp[i])):
                pass
            else:
                return 0
    '''
    while(i<len(exp)):
        if(exp[i]=='{' or exp[i] == '(' or exp[i] == '['):
            stack.push(exp[i])
        if(exp[i]=='}' or exp[i] == ')' or exp[i] == ']'):
            if(stack.isEmpty()):
                return 0
            elif (Check(stack.pop(),exp[i])):
                pass
            else:
                return 0
        i = i+1
    '''
    if(stack.isEmpty()):
        return 1
    else:
        return 0



def Check(a,b):
    if(a == '{' and b == '}'):
        return 1
    if(a == '[' and b == ']'):
        return 1
    if(a == '(' and b == ')'):
        return 1
    return 0


if __name__ == '__main__':

    s = '{()}[]{4}{}([{([])}])'

    if(checkExpression(s)):
        print("Balanced Expression")
    else:
        print('Not a Balanced Expression')
