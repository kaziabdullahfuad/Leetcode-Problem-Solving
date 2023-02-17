#from collections import deque
from queue import Queue
# q=deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q)
# q.popleft()
# print(q)
# print(len(q))
def upsidedown(q):
    
    n=q.qsize()
    for i in range(n-1):
        temp=q.get()
        q.put(temp)
    
def twoqueues(q,q2):

    n=q.qsize()
    
    while(not q.empty()):
        upsidedown(q)
        q2.put(q.get())
    
   

def display(q):

    while(not q.empty()):
        print(q.get())
    


q=Queue(maxsize=4)
#print(q.qsize())


# for i in range(1,4):
#     q.put(i)

q2=Queue(maxsize=4)
#print("The size of q2 :",q2.qsize())
#print(q.full())
# print(q.get())
# print(q.get())

#implementing queue using two stacks
# print("Displaying the first q before changing: ")
# display(q)


# q2=twoqueues(q,q2)

# print("The first q became empty:",q.empty())

# print("The q2 still reamins empty:",q2.empty())


# print("Displaying the q2 after function call ",display(q2))

#print("Displaying the q after function call ",display(q))

for i in range(4):
    value=input("Enter your value: ")
    if not q.empty():
        while(not q.empty()):
            q2.put(q.get())
        
        q.put(value)

        while(not q2.empty()):
            q.put(q2.get())
        
    else:
        q.put(value)

display(q)
        