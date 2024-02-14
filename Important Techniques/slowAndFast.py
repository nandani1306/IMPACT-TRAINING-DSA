class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None

class CircularLL:
    def __init__(self) -> None:
        self.head = None

def detectCycle(head):
    slow = head
    fast = head
    while(slow is not None and fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        
        if (fast == slow):
            return 1
    return 0

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

temp = head
while (temp.next is not None):
    temp = temp.next
temp.next = head

if(detectCycle(head)):
    print("Cycle Detected")
else:
    print("Cycle Not Detected")