class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def swap(self,x,y):
        currentX = self.head
        currentY = self.head
        prevX = None
        prevY = None

        #find X
        while(currentX!=None and currentX.data!=x):
            prevX = currentX
            currentX = currentX.next

        while(currentY!=None and currentY.data!=y):
            prevY = currentY
            currentY = currentY.next

        if currentX==None or currentY==None :
            return

        if prevX!=None: #X is not head
            prevX.next = currentY
        else:
            self.head = currentY

        if prevY!=None: #Y is not head
            prevY.next = currentX
        else:
            self.head = currentX

        temp  = currentX.next
        currentX.next = currentY.next
        currentY.next = temp



    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    llist = LinkedList() #creates a LinkedList

    llist.push(6)
    llist.push(7)
    llist.push(1)
    llist.push(4)
    llist.push(8)
    llist.push(2)

    print("List before swap:", end = ' ')
    llist.printList()
    llist.swap(8,7)
    print("List after swap:", end = ' ')
    llist.printList()
