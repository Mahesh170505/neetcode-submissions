class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    def push(self, x: int) -> None:
        self.queue2.append(x)
        while(len(self.queue1) != 0):
            self.queue2.append(self.queue1.popleft())
        while(len(self.queue2) != 0):
            self.queue1.append(self.queue2.popleft())
        
    def pop(self) -> int:
        return int(self.queue1.popleft())

    def top(self) -> int:
        return int(self.queue1[0])

    def empty(self) -> bool:
        if(len(self.queue1) == 0):
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()