class MinStack:
    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        del self.arr[-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)
    
if __name__ == "__main__":
    stack = MinStack()
    stack.push(1)
    stack.push(5)
    stack.push(2)
    print(stack.top())
    print(stack.getMin())
    stack.pop()
    print(stack.top())