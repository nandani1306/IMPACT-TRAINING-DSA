class circularQueue:
    def __init__(self) -> None:
        self.n = int(input("Enter size : "))
        self.cirQueue = []
        self.front = -1
        self.rear = -1
        self.run()

    def enqueue(self,value):
        if (self.front == 0 and self.rear == self.n-1) or (self.front == self.rear+1):
            print("Overflow")

        elif self.front==-1 and self.rear==-1:
            self.front = 0
            self.rear = 0
            self.cirQueue.append(value)

        else:
            self.rear = (self.rear+1)%self.n
            self.cirQueue.insert(self.rear, value)

        # else:
        #     self.rear+=1
        #     if self.rear == 0:
        #         self.front = 0
        #     self.cirQueue = value

    def dequeue(self) -> int:
        if not self.cirQueue:
            print("Empty queue")
        elif self.front == self.rear:
            temp = self.cirQueue.pop(self.front)
            self.cirQueue.insert(self.front,None)
            self.front = self.rear=-1
            return temp
        else:
            temp = self.cirQueue.pop(self.front)
            self.cirQueue.insert(self.front,None)
            self.front+=1
            return temp
    
    def display(self):
        print(self.cirQueue)

    def run(self):
        flag = True

        while (flag):
            ch = int(input("1]enque\t2]dequeue\t3]display\t4]exit\n"))

            if ch == 1:
                val = int(input("Enter number to push : "))
                self.enqueue(val)
            if ch == 2:
                print("Element popped :",self.dequeue())
            if ch == 3:
                self.display()
            if ch == 4:
                flag = False

obj = circularQueue()

