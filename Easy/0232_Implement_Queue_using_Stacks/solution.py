class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.s2.pop()    

    def peek(self):
        """
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1 and not self.s2

# Local terminal execution and test driver
if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1) # queue is: [1]
    myQueue.push(2) # queue is: [1, 2]
    print(f"Peek: {myQueue.peek()}")   # Expected: 1
    print(f"Pop: {myQueue.pop()}")     # Expected: 1, queue is [2]
    print(f"Empty: {myQueue.empty()}") # Expected: False
