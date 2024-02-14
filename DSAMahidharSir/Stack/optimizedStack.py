class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
    
    def display(self):
        print(self.stack)
    
def run():
    obj = Stack()
    flag = True
    while flag:
        choice = int(input("Enter Choice\n1]Push 2]Pop 3]Peek 4]Display 5]Exit : "))
        if choice == 1:
            value = int(input("Enter Value : "))
            obj.push(value)
        elif choice == 2:
            print(obj.pop())
        elif choice == 3:
            print(obj.peek())
        elif choice == 4:
            obj.display()
        elif choice == 5:
            flag = False
        else:
            print("Enter valid choice")

run()