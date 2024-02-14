class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self,value):
        self.stack.append(value)

    def pop(self) -> chr:
        if self.stack:
            return self.stack.pop()
        
    def peek(self) -> chr:
        if self.stack:
            return self.stack[-1]
        

def priority(symbol) -> int:
    if symbol == '(':
        return 0
    elif symbol == '+' or symbol == '+':
        return 1
    elif symbol == '*' or symbol == '/':
        return 2
    elif symbol == '^':
        return 3
    return 0


def InfixToPostfix(exp):
    s=Stack()
    tempstr = ''
    for c in exp:

        if c.isalnum():
            tempstr+=c
        
        elif c in '+-/*':
            if not s.stack:
                s.push(c)
            else:
                while s.stack and priority(s.peek()) >= priority(c):
                    tempstr += s.pop()

                s.push(c)

        elif c == '(':
            s.push(c)

        elif c == ')':
            while s.stack and s.peek() != '(':
                tempstr += s.pop()
            s.pop()

    while s.stack:
        tempstr += s.pop()
    return tempstr


exp = input("Enter infix expression : ")
# exp = "a+b"
result = InfixToPostfix(exp)
print("Infix to postfix :" ,result)


            


    