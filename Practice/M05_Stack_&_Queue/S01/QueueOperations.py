'''
enqueue -> append()
dequeue -> pop(0) - pops first element
peek (front) -> q[0]

'''
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self ,val):
        self.q.append(val)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.q.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.q[0]

    def isEmpty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.peek())
print(q.isEmpty())
print(q.size())