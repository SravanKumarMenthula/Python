class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def Length_iter(self):
        temp = self.head
        count = 0
        while (temp!=None):
            count =count+1
            temp = temp.next
        return count

    def Length_recur(self): #to call recursion
        count = self.recur(self.head)
        return count

    def recur(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.recur(node.next)


if __name__ == '__main__':
    llist = LinkedList() #creates a LinkedList

    llist.push(6)
    llist.push(7)
    llist.push(1)
    llist.push(4)
    llist.push(8)

    Length = llist.Length_iter()
    print(Length)
    llist.push(10)
    Length = llist.Length_recur()
    print(Length)
