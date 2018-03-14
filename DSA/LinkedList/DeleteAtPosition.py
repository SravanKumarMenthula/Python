class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def Length(self):
        temp = self.head
        count  = 0
        while(temp!=None):
            count = count+1
            temp = temp.next
        return count


    def deleteAtPosition(self, pos):
        len = self.Length()
        print(len)
        i = 1
        temp =  self.head
        if(pos > len):
            print("Position out of index")
            return
        else:
            while(i!=pos):
                i = i+1
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp = None
            return

    def printList(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print()
        return

if __name__ == '__main__':
    llist = LinkedList() #creates a LinkedList

    llist.push(6)
    llist.push(7);
    llist.push(1);
    llist.push(4)
    llist.push(8)

    print ('Created linked list is:'),
    llist.printList()
    llist.deleteAtPosition(2)
    llist.printList()
    llist.deleteAtPosition(3)
    llist.printList()
