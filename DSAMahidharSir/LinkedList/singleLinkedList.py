class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.link = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def search(self,value):
        if self.head is None:
            print("LL is empty\n")
        else:
            temp = self.head
            while temp.data != value:
                temp = temp.link
            if temp.data == value:
                return temp
            else:
                return None

    def addAtBegin(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.link = self.head
            self.head = temp
 
    def addAtEnd(self,value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            temp = self.head
            while temp.link != None:
                temp = temp.link
            temp1 = Node(value)
            temp.link = temp1
            # self.tail = temp1
            # self.temp1.link = None

    def addAtAnyPosition(self,value,prev):
        temp1 = Node(value)
        prevNode = self.search(prev)
        if(prevNode):
            temp1.link = prevNode.link
            prevNode.link=temp1
        else:
            print("No prev found\n")

    def delAtBegin(self):
        if self.head is None:
            print("LL is empty\n")
        else:
            temp = self.head
            self.head = self.head.link
            temp = None

    def delAtEnd(self):
        if self.head is None:
            print("LL is empty\n")
        else:
            temp = self.head
            # temp2 = temp.link
            while temp.link.link != None:
                temp = temp.link
            # last = temp.link
            temp.link = None
            # last = None

    # def delAtAnyPosition(self,prev):
    #     if self.head is None:
    #         print("LL empty\n")
    #     prevNode = self.search(prev)
    #     if prevNode:
    #         prevNode.link = prevNode.link.link
    #     else:
    #         print("No prev found\n")
            
    def delAtAnyPosition(self,prev):
        if self.head is None:
            print("LL empty\n")
        prevNode = self.search(prev)
        if prevNode:
            if prevNode == self.head:
                self.delAtBegin()
            elif prevNode.link == None:
                self.delAtEnd()
            else:
                prevNode.link = prevNode.link.link
        else:
            print("No prev found\n")

    def disp(self):
        if self.head is None:
            print("LL is empty\n")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "->" ,end=" ")
                temp = temp.link

    def findMid(self):
        slow = self.head
        fast = self.head
        if(not self.head):
            return
        elif self.head.link is None or self.head.link.link is None:
            return self.head.data
        else:
            # fast.next is not None => for odd number of nodes in LL
            # fast.next.next is not None => for even number of nodes in LL
            while(fast.link is not None and fast.link.link is not None):
                slow = slow.link
                fast = fast.link.link
            return slow.data

def run():
    ll = LinkedList()
    flag = True
    while flag:
        ch = int(input("\n1]InsertAtBegin 2]InsertAtEnd 3]InsertAtAnyPosition 4]InsertAtBegin 5]InsertAtEnd 6]InsertAtAnyPosition 7]display 8]findMidElement 9]exit\n"))
        if ch == 1:
            value = int(input("Enter value:\n"))
            ll.addAtBegin(value)
        if ch == 2:
            value = int(input("Enter value:\n"))
            ll.addAtEnd(value)
        if ch == 3:
            value = int(input("Enter value:\n"))
            ll.addAtAnyPosition(value)
        if ch == 4:
            ll.delAtBegin()
        if ch == 5:
            ll.delAtEnd()
        if ch == 6:
            prev = int(input("Enter prev element :\n"))
            ll.delAtAnyPosition(prev)
        if ch == 7:
            ll.disp()
        if ch == 8:
            print("Mid element is :",ll.findMid())
        if ch == 9:
            flag = False

run()


