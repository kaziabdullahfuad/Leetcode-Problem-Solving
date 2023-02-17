from queue import Queue

class MyStack:
    
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.stack_length=0

    def push(self, x: int) -> None:
        self.stack_length+=1
        
        if self.q1.empty():
            self.q1.put(x)
        elif not self.q1.empty():
            
            while(not self.q1.empty()):
                self.q2.put(self.q1.get())
            
            self.q1.put(x)

            while(not self.q2.empty()):
                self.q1.put(self.q2.get())


    def pop(self) -> int:
        
        if self.stack_length==0:
            return 0
        else:
            self.stack_length-=1
            return self.q1.get()

    def top(self) -> int:
        if (self.q1.empty()):
            return None
        return self.q1.queue[0]

    def empty(self) -> bool:
        if self.stack_length==0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

obj=MyStack()

obj.push(1)
obj.push(2)
obj.push(3)

print(obj.stack_length)

print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.stack_length)