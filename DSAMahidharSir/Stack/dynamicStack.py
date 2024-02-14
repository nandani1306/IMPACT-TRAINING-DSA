class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1
    
    def push(self,val):
        self.top += 1
        self.stack.append(val)
    
    def pop(self) -> int:
        if self.top == -1:
            print("Underflow")
        else:
            temp = self.stack.pop()
            self.top -= 1
            return temp
        
    def peek(self) -> int:
        if self.top == -1:
            print("Underflow")
        else:
            temp = self.stack.pop()
            self.stack.append(temp)
            return temp
    
    def display(self):
        print(self.stack)
    
    def run(self):
        flag = True
        while flag:
            print("1]Push 2]Pop 3]Peek 4]Display 5]Exit")
            choice = int(input("Enter Choice : "))
            if choice == 1:
                val = int(input("Enter Value : "))
                self.push(val)
            elif choice == 2:
                print(self.pop())
            elif choice == 3:
                print(self.peek())
            elif choice == 4:
                self.display()
            elif choice == 5:
                flag = False
            else:
                print("Invalid choice")

obj = Stack()
obj.run()    