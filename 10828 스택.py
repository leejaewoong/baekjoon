# 문제 링크: https://www.acmicpc.net/problem/10828

class Stack:

    def __init__(self):        
        self.stk = []
        self.ptr = 0

    def empty(self):
        if self.ptr == 0:
            return 1
        else: 
            return 0        

    def push(self, x):        
        self.stk.append(x)
        self.ptr += 1
        return x

    def pop(self):
        if not self.empty():        
            self.ptr -=1
            return self.stk.pop()
        else:
            return -1
    
    def top(self):
        if not self.empty():        
            return self.stk[self.ptr - 1] 
        else:
            return -1
    
    def size(self):
        return self.ptr
    
import sys

stack = Stack()
orderNumber = int(sys.stdin.readline())

for order in range(orderNumber):
    order = sys.stdin.readline().split() 
    cmd = order[0]      

    if cmd == "push":
        stack.push(int(order[1]))
    elif cmd == "pop":
        print(stack.pop())
    elif cmd == "top":
        print(stack.top())
    elif cmd == "size":
        print(stack.size())
    elif cmd == "empty":
        print(stack.empty())

        



        

