class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = max(nums)
        return sum(maximum - i for i in nums)

# Local terminal execution and test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [2, 1, 3]
    print(f"Test 1 Output: {solution.minMoves(nums1)}")  # Expected: 3
    
    # Test Case 2
    nums2 = [4, 4, 5]
    print(f"Test 2 Output: {solution.minMoves(nums2)}")  # Expected: 2
