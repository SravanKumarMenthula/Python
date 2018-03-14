class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while(current!=None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end = " ")
            temp = temp.next
        print()

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print ("Given Linked List:")
    llist.printList()
    llist.reverse()
    print ("\nReversed Linked List:")
    llist.printList()
