class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :type rtype: List[int]
        """
        if not nums:
            return []
            
        start = min(nums)
        end = max(nums)
        
        nums_set = set(nums)
        lst = []
        
        # Use a set for O(1) membership lookups for efficiency
        for i in range(start + 1, end):
            if i not in nums_set:
                lst.append(i)
        return lst

# Local terminal execution and test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 4, 2, 5]
    print(f"Test 1 Output: {solution.findMissingElements(nums1)}")  # Expected: [3]
    
    # Test Case 2
    nums2 = [7, 8, 6, 9]
    print(f"Test 2 Output: {solution.findMissingElements(nums2)}")  # Expected: []
    
    # Test Case 3
    nums3 = [5, 1]
    print(f"Test 3 Output: {solution.findMissingElements(nums3)}")  # Expected: [2, 3, 4]
