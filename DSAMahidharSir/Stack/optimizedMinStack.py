class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
    
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        
    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]

def run():
    flag = True
    obj = Stack()
    min = Stack()
    while flag:
        print("1]Push 2]Pop 3]Peek 4]Display 5]min 6]Exit")
        choice = int(input("Enter Choice : "))
        if choice==1:
            val=int(input("Enter the number: "))
            obj.push(val)
            if not min.stack: 
                min.push(val)
            elif(val<=min.peek()):
                min.push(val)
            else:
                min.push(min.peek())
        elif choice==2:
            obj.pop()
            min.pop()
        elif choice==3:
            obj.peek()
        elif choice==4:
            obj.Display()
            min.Display()
        elif choice==5:
            print(min.peek(),"is the min value in the Stack...")
        elif choice==6:
            flag=False
        else:
            print("invalid choice...")                   

run()