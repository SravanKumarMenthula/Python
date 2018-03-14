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

    def iter_find(self, key):
        temp = self.head
        count = 1
        while(temp!=None):
            if(temp.data == key):
                print("Element number:"+str(count))
                return
            count = count+1
            temp = temp.next
        print("Element not found")

    def recur_find(self, key):
        count = self.recur(self.head,key)
        print("Element numer: " + str(count))

    def recur(self,node,key):
        if (not node):
            return 0
        else:
            if(node.data == key):
                return 1
            else:
                return 1 + self.recur(node.next,key)

if __name__ == '__main__':
    llist = LinkedList() #creates a LinkedList

    llist.push(6)
    llist.push(7)
    llist.push(1)
    llist.push(4)
    llist.push(8)

    llist.iter_find(1)
    llist.recur_find(7)
