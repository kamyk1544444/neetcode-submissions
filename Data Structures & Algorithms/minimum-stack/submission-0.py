class MinStack:

    def __init__(self):
        self.stack = []
        self.miner = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.miner[-1] if self.miner else val)
        self.miner.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.miner.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.miner[-1]
