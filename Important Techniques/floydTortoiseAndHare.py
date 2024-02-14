class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None

class CircularLL:
    def __init__(self) -> None:
        self.head = None

    # circular ll
    # def insertAtBegin(self,value):
    #     temp1 = Node(value)
    #     if not self.head:
    #         self.head = temp1
    #         self.head.next = self.head
    #     else:
    #         temp1.next = self.head
    #         self.head = temp1

    # single ll
    # def addAtBegin(self,value):
    #     if self.head is None:
    #         self.head = Node(value)
    #     else:
    #         temp = Node(value)
    #         temp.next = self.head
    #         self.head = temp

    def detectCycle(self):
        slow = self.head
        fast = self.head
        while(slow is not None and fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
         
            if (fast == slow):
                return 1
        return 0
         
    

cll = CircularLL()


# circ ll addtion at beginning
# cll.insertAtBegin(2)
# cll.insertAtBegin(22)
# cll.insertAtBegin(24)
# cll.insertAtBegin(24)

# single ll addtion at beginning
# cll.addAtBegin(2)
# cll.addAtBegin(13)
# cll.addAtBegin(20)
# cll.addAtBegin(22)
print(cll.detectCycle())