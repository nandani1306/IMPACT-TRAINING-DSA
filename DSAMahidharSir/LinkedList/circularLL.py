class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None
    
class CircularLL:
    def __init__(self) -> None:
        self.head = None

    def insertAtBegin(self,value):
        temp1 = Node(value)
        if not self.head:
            self.head = temp1
            self.head.next = self.head
        else:
            temp1.next = self.head
            self.head = temp1

    def insertAtEnd(self,value):
        temp1 = Node(value)
        if not self.head:
            self.head = temp1
            self.head.next = self.head
        else:
            temp = self.head
            while (temp.next != self.head):
                temp = temp.next
            temp.next = temp1
            temp1.next = self.head

    def delAtBegin(self):
        if not self.head:
            print("LL is empty")
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = self.head.next
            self.head = None
            self.head = temp.next

    def delAtEnd(self):
        if not self.head:
            print("LL is empty")
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            nextNode = temp.next
            nextNode = None 
            temp.next = self.head

    def detAtAny(self,target_data):
        if not self.head:
            print("LL is empty")
        else:
            temp = self.head
            while temp.next.data != target_data:
                temp = temp.next
            nextNode = temp.next
            temp.next = nextNode.next
            nextNode = None
            
    def disp(self):
        if self.head is None:
            print("LL is empty\n")
        else:
            temp = self.head
            print(temp.data, "-> ", end='')
            temp = temp.next
            while (temp != self.head):
                print(temp.data, "->" ,end=" ")
                temp = temp.next

cll = CircularLL()
cll.insertAtBegin(12)
cll.insertAtEnd(13)
cll.insertAtEnd(14)
cll.insertAtEnd(16)
cll.insertAtEnd(17)
cll.insertAtEnd(18)
cll.delAtBegin()
cll.delAtBegin()
cll.delAtEnd()
cll.detAtAny(16)
cll.disp()