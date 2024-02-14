class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None


head = None

def findMid(head):
    slow = head
    fast = head
    if(not head):
        return
    elif head.next is None or head.next.next is None:
        return head.data
    else:
        # fast.next is not None => for odd number of nodes in LL
        # fast.next.next is not None => for even number of nodes in LL
        while(fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow.data
head = Node(1)
head.next = Node(16)
head.next.next = Node(15)
head.next.next.next = Node(12)
# head.next.next.next.next = Node(22)

if(findMid(head)):
    print(findMid(head))
else:
    print("No mid")
            
