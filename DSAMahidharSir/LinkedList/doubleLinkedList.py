class Node:
    def __init__(self,data) -> None:
        self.prev = None
        self.data = data
        self.next = None 

class doubleLL:
    def __init__(self) -> None:
        self.head = None

    def search(self,value):
        if self.head is None:
            print("LL is empty\n")
        else:
            temp = self.head
            while temp.data != value:
                temp = temp.next
            if temp.data == value:
                return temp
            else:
                return None
            
    def addAtBegin(self,value):
        temp1=Node(value)
        if self.head is None:
            self.head = temp1
        else:
            temp1.next = self.head
            self.head.prev = temp1
            self.head = temp1

    def addAtEnd(self,value):
        temp1 = Node(value)
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = temp1
            temp1.prev = temp

    def addAtAnyPosition(self,value,prev):
        temp1 = Node(value)
        prevNode = self.search(prev)
        if(prevNode):
            prevNode.next.prev = temp1
            temp1.next = prevNode.next
            prevNode.next = temp1
            temp1.prev = prevNode
        else:
            print("No prev found")

    def delAtBegin(self):
        if self.head is None:
            print("DLL is Empty")
        else:
            temp = self.head
            self.head = self.head.next
            temp = None

    def delAtEnd(self):
        if self.head is None:
            print("DLL is Empty")
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None 

    def delAtAny(self,prev):
        if self.head is None:
            print("DLL is empty")
        prevNode = self.search(prev)
        if prevNode == self.head:
            self.delAtBegin()
        elif prevNode.next is None:
            self.delAtEnd()
        elif(prevNode):
            prevNode.next.prev = prevNode.prev
            prevNode.prev.next = prevNode.next
        else:
            print("No prev found")
    
    
    def display(self):
        if self.head is None:
            print("LL is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,"->", end=" ")
                temp = temp.next

def run():
    dll = doubleLL()
    flag = True
    while flag:
        ch = int(input("\n1]InsertAtBegin 2]InsertAtEnd 3]InsertAtAnyPosition 4]DeleteAtBegin 5]DeleteAtEnd 6]DeleteAtAnyPosition 7]display 8]exit\n"))
        if ch == 1:
            value = int(input("Enter value:\n"))
            dll.addAtBegin(value)
        if ch == 2:
            value = int(input("Enter value:\n"))
            dll.addAtEnd(value)
        if ch == 3:
            value = int(input("Enter value:\n"))
            dll.addAtAnyPosition(value)
        if ch == 4:
            dll.delAtBegin()
        if ch == 5:
            dll.delAtEnd()
        if ch == 6:
            prev = int(input("Enter prev element :\n"))
            dll.delAtAny(prev)
        if ch == 7:
            dll.display()
        if ch == 8:
            flag = False
        if ch == 9:
            print("Invalid choice\n")

run()


