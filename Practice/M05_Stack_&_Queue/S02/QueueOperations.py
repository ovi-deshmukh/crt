'''
front == -1 means queue is empty
rear == size - 1 means queue is full
'''
#Queue Implementation using front and rear pointers
class Queue:
    def __init__(self, size):
        self.size = size
        self.front = -1 
        self.rear = -1
        self.q = [None] * size

    def enqueue(self, val):
        if self.rear == self.size - 1:
            return "Queue is full"
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.q[self.rear] = val

    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        self.front += 1
        val = self.q[self.front]
        return val

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        for i in range(self.front, self.rear + 1):
            print(self.q[i], end=" -> ")
        print("None")

q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.dequeue()
q.display()

#Queue Implementation Using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        newNode = Node(val)
        if self.front == None:
            self.front = self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        val = self.front.data
        self.front = self.front.next
        if self.front is None: #???
            self.rear = None
        return val

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")

qu = QueueLL()
qu.enqueue(100)
qu.enqueue(200)
qu.enqueue(300)
qu.enqueue(400)
qu.display()
qu.dequeue()
qu.dequeue()
qu.display()