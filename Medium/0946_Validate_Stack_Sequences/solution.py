class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        curr = 0
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and curr < len(popped) and stack[-1] == popped[curr]:
                stack.pop()
                curr += 1

        return not stack

# Local terminal execution and test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    pushed1, popped1 = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
    print(f"Test 1 Output: {solution.validateStackSequences(pushed1, popped1)}")  # Expected: True
    
    # Test Case 2
    pushed2, popped2 = [1, 2, 3, 4, 5], [4, 3, 5, 1, 2]
    print(f"Test 2 Output: {solution.validateStackSequences(pushed2, popped2)}")  # Expected: False
