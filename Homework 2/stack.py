class Stack:
    def __init__(self):
        self.stack = []
        self.max = 0

    def push(self, item):
        return self.stack.append(item)

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            raise IndexError("Tried to peek on empty stack.")

    def size(self):
        return len(self.stack)

    def pop(self):
        try:
            value = self.stack[-1]
            self.stack = self.stack[:-1]
            return value
        except IndexError:
            raise IndexError("Tried to pop from empty stack.")

