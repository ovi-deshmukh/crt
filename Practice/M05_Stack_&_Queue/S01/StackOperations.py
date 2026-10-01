'''
Implementation of a stack using list
Time Complexity - O(1) - for each operation
'''
class Stack:
    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append(val)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.s.pop()

    def isEmpty(self):
        return len(self.s) == 0

    def size(self):
        return len(self.s)

    def peek(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.s[-1]

st = Stack() 
st.push(10)
st.push(20)
st.push(30)
print(st.isEmpty())
print(st.peek())
st.pop()
print(st.peek())
'''
top variable is th pointer that points to the top of the stack
if top of stack == size -1, stack is full
if top == -1, stack is empty
'''

#Stack Implementation using top variable
class StackWithTop():

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.s = [None] * self.size

    def push(self,val):
        if self.top == self.size -1:
            return "Stack is full"
        self.top += 1
        self.s[self.top] = val

    def isEmpty(self):
        return self.top == -1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        val = self.s[self.top]
        self.top -= 1 #decrementing top value also works instead of having to delete or pop the top
        return val

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.s[self.top]

    def stackSize(self):
        return self.top + 1

stt = StackWithTop(2)
stt.push(10)
stt.push(20)
print(stt.push(30))
print(stt.isEmpty())
print()
print(stt.stackSize())
print(stt.pop())
print(stt.peek())

#Stack implementation using Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class StackWithSLL:

    def __init__(self):
        self.top = None 

    def push(self, val):
        newNode = Node(val)
        newNode.next = self.top 
        self.top = newNode

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        val = self.top.data
        self.top = self.top.next
        return val

    def isEmpty(self):
        return self.top == -1

    def peek(self):
        if self.top is None: #Can be used instead of isEmpty()
            return "Stack is empty."
        return self.top.data

    def size(self):
        return self.top - 1

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")

sws = StackWithSLL()
sws.push(10)
sws.push(20)
sws.push(30)
sws.push(40)
sws.display()
print(sws.pop())
print(sws.peek())
sws.display()