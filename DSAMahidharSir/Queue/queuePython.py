class queue:
    def __init__(self) -> None:
        self.n = int(input("Enter length of queue :"))
        self.queue = []*self.n
        self.rear = -1
        self.front = -1 
        self.run()

    def enqueue(self,val):
        if self.rear == self.n-1:
            print("Cant insert Queue Overflow")
        self.rear+=1
        self.queue.append(val)
        if self.rear == 0:
            self.front = 0

    def dequque(self) -> int:
        if self.front == -1 and self.rear == -1:
            print("Queue empty")
        elif self.front == self.rear:
            temp = self.queue.pop(0)
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue.pop(0)
            self.rear-=1
            return temp
        
    def run(self):
        flag=True
        while(flag):
            ch=int(input("1]push 2]pop 3]exit\n"))
            if ch == 1:
                val=int(input("\nEnter num to push:"))
                self.enqueue(val)
            if ch == 2:
                print("Element dequeued is : ",self.dequque())
            if ch == 3:
                flag=False

obj = queue()
