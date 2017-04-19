from stack import Stack

class IntegerStack(Stack):
    def max(self):
        if not self.stack:
            return None
        for v in self.stack:
            if v > self.max:
                self.max = v
