
class Node:

    def __init__(self,data):
        self.data = data #Assign data
        self.next = None #Initialise to Null/None

class LinkedList:

    def __init__(self):
        self.head = None

    #Insert at begining of the LinkedList
    def push(self,data):
        new_node = Node(data) #creating new_node and assigning the value too
        new_node.next = self.head #assigning the next of the new_node to head
        self.head = new_node #assigning head to this new Node

    def insertAfter(self, prev_node, data):
        if prev_node is None:  #checking whether prev_node exists or not
            print("prev_node cannot be Null")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def printList(self):
        node = self.head
        while(node):
            print(node.data," ")
            node = node.next


if __name__ == "__main__": #code execution starts here

    llist = LinkedList() #creates a LinkedList
     # Insert 6.  So linked list becomes 6->None
    llist.append(6)
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    print ('Created linked list is:'),
    llist.printList()
