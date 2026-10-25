class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
        
        result = a + b
        
        return str(bin(result)[2:])

# Local terminal execution and test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    a1, b1 = "11", "1"
    print(f"Test 1 Output: {solution.addBinary(a1, b1)}")  # Expected: "100"
    
    # Test Case 2
    a2, b2 = "1010", "1011"
    print(f"Test 2 Output: {solution.addBinary(a2, b2)}")  # Expected: "10101"
