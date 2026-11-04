class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) // 2]
        
        result = 0
        for num in nums:
            result += abs(num - median)
            
        return result

# Local terminal execution and test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 3]
    print(f"Test 1 Output: {solution.minMoves2(nums1)}")  # Expected: 2
    
    # Test Case 2
    nums2 = [1, 10, 2, 9]
    print(f"Test 2 Output: {solution.minMoves2(nums2)}")  # Expected: 16
