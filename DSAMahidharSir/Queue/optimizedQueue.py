class optiQueue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self,value):
        self.queue.append(value)
    
    def dequeue(self)->int:
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue Empty")

    def display(self):
        print(self.queue)


def run():
    obj = optiQueue()
    flag = True
    while(flag):
        ch = int(input("1]enqueue 2]dequeue 3]print 4]exit\n"))
        if ch == 1:
            value = int(input("Enter number to enqueue:"))
            obj.enqueue(value)
        elif ch == 2:
            print("Element popped :", obj.dequeue())
        elif ch == 3:
            obj.display()
        elif ch == 4:
            flag = False
        else:
            print("Enter valid choice")

run()
