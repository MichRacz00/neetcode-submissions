class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = min(val, self.minimum_vals[-1] if self.minimum_vals else val)
        self.minimum_vals.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.stack)
        print(self.minimum_vals)
        return self.minimum_vals[-1]
