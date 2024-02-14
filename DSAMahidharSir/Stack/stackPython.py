class Stack:
    def __init__(self) -> None:
        self.n = int(input("Enter length of stack :"))
        self.stack = []*self.n
        self.top = -1
        self.run()

    def push(self,val):
        if (self.top == self.n-1):
            print("Stack overflow")
        else:
            self.top+=1
            self.stack.append(val)

    def pop(self) -> int:
        if (self.top == -1):
            return -1
        else:
            temp=self.stack.pop()
            self.top=self.top-1
            return temp
            
    def peek(self) -> int:
        if (self.top == -1):
            return -1
        else:
            temp=self.stack.pop()
            self.push(temp)
            return temp
        
    def run(self):
        flag=True
        while(flag):
            ch=int(input("1]push 2]pop 3]peek 4]exit\n"))
            if ch == 1:
                val=int(input("\nEnter num to push:"))
                self.push(val)
            if ch == 2:
                print("Element popped is : ",self.pop())
            if ch == 3:
                print(self.peek())
            if ch == 4:
                flag=False
obj=Stack()
