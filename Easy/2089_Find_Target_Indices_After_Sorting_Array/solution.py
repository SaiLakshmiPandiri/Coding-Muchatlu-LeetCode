class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        return [x for x in range(len(nums)) if nums[x] == target]

# Local terminal execution and test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 5, 2, 3]
    target1 = 2
    print(f"Test 1 Output: {solution.targetIndices(nums1, target1)}")  # Expected: [1, 2]
    
    # Test Case 2
    nums2 = [1, 2, 5, 2, 3]
    target2 = 3
    print(f"Test 2 Output: {solution.targetIndices(nums2, target2)}")  # Expected: [3]
    
    # Test Case 3
    nums3 = [1, 2, 5, 2, 3]
    target3 = 5
    print(f"Test 3 Output: {solution.targetIndices(nums3, target3)}")  # Expected: [4]
