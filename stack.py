class Stack():
    def __init__(self):
        self.data = []
    
    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        return self.data.pop(len(self.data) -1)
    
    def peek(self):
        return self.data[-1]