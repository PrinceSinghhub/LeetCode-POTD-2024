class CustomStack:

    def __init__(self, maxSize: int):

        self.stackSize = maxSize
        self.pointer = -1
        self.stack = []

    def push(self, x: int) -> None:

        if len(self.stack) < self.stackSize:
            self.stack.append(x)
            self.pointer += 1
            return self.stack
        return -1

    def pop(self) -> int:

        if self.pointer > -1:
            x = self.stack.pop(self.pointer)
            self.pointer -= 1
            return x
        else:
            return -1

    def increment(self, k: int, val: int) -> None:

        if len(self.stack) < k:
            for i in range(len(self.stack)):
                self.stack[i] = self.stack[i] + val

        else:
            for i in range(k):
                self.stack[i] = self.stack[i] + val

        return self.stack

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)