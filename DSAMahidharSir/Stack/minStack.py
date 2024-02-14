class minStackPy:
    def __init__(self) -> None:
        self.n = int(input("Enter length of stack : \n"))
        self.normalStack = []*self.n
        self.normalTop = -1

        self.minStack = []*self.n
        self.minTop = -1 

        self.run()
    
    def normalPush(self,val):
        if self.normalTop == self.n-1:
            print("Overflow : cant push")
        else:
            self.normalTop+=1
            self.normalStack.append(val)

    def minPush(self,val):
        if (self.minTop == self.n-1):
            print("Overflow")
        else:
            self.minTop+=1
            self.minStack.append(val)

    def normalPop(self) -> int:
        if (self.normalTop == -1):
            print("Underflow")
        else:
            temp=self.normalStack.pop()
            self.normalTop=self.normalTop-1
            return temp
        
    def minPop(self) -> int:
        if (self.minTop == -1):
            print("Underflow")
        else:
            temp = self.minStack.pop()
            self.minTop = self.minTop-1
            return temp
        
    def normalPeek(self) -> int:
        if (self.normalTop == -1):
            print("Underflow")
        else:
            temp = self.normalStack.pop()
            self.normalPush(temp)
            return temp
        
    def minPeek(self) -> int:
        if (self.minTop == -1):
            print("Underflow")
        else:
            temp = self.minPop()
            self.minPush(temp)
            return temp
        
    def run(self):
        flag = True
        while(flag):
            ch = int(input("1]Push 2]Pop 3]Peek 4]Print 5]Exit"))

            if ch == 1:
                val=int(input("\nEnter num to push:"))
                self.normalPush(val)

                if(self.minTop == -1):
                    self.minPush(val)

                elif (val <= self.minPeek()):
                    self.minPush(val)

                else:
                    self.minPush(self.minPeek())
                    
            if ch == 2:
                print("Popped : ",self.normalPop())
                print("Popped : ",self.minPop())

            if ch == 3:
                print("Peek :" , self.normalPeek())

            if ch == 4:
                print("Minimum is :", self.minPeek())

            if ch == 5:
                flag = False

obj = minStackPy()
