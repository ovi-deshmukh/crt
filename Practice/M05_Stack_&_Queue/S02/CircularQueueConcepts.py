class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q = [None] * self.size

    def enqueue(self, val):
        if self.front == (self.rear + 1) % self.size:
            return "Queue is full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = val

    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        val = self.q[self.front]
        if self.front == self.rear:
            # Removing the final item restores the empty-queue state.
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        index = self.front
        while True:
            print(self.q[index], end=" -> ")
            if index == self.rear:
                break
            index = (index + 1) % self.size
        print("None")
        
