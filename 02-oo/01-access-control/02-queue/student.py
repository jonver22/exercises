class Queue:
    def __init__(self):
        self.Queue = []

    def add(self, item):
        self.Queue.append(item)
    
    def next(self):
        ret = self.Queue[0]
        self.Queue.pop(0)
        return ret

    def is_empty(self):
        return (self.Queue == [])

    




