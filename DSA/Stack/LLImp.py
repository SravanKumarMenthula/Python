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
            return
        temp = self.head
        print("Poped Out the Item: " + str(temp.data))
        self.head = temp.next
        temp = None

    def printStack(self):
        if(self.isEmpty()):
            print("Empty Stack")
            return
        temp = self.head
        while (temp!=None):
            print(temp.data,end=' ')
            temp = temp.next
        print()

    def peek(self):
        if(self.isEmpty()):
            print("Empty Stack")
            return
        print(self.head.data)


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.peek()
    stack.printStack()
    stack.pop()
    stack.peek()
    stack.pop()
    stack.peek()
    stack.pop()
    stack.printStack()
