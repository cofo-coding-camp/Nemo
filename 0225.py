class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qin = []
        self.qout = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.qin.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while self.qin:
            temp = self.qin.pop(0)
            if self.qin:
                self.qout.append(temp)
            else:
                return temp
        while self.qout:
            temp = self.qout.pop(0)
            if self.qout:
                self.qin.append(temp)
            else:
                return temp

    def top(self) -> int:
        """
        Get the top element.
        """
        while self.qin:
            a = self.qin.pop(0)
            self.qout.append(a)
            if not self.qin:
                return a
        while self.qout:
            a = self.qout.pop(0)
            self.qin.append(a)
            if not self.qout:
                return a

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.qin and not self.qout:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
