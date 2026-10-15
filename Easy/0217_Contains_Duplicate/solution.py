class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # A set in Python stores only unique elements.
        # Comparing the length of the list to the length of its set 
        # instantly tells us if there were any duplicate values.
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Contains duplicates
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1} | Output: {sol.containsDuplicate(nums1)}")  # Expected: True
    
    # Test Case 2: All unique elements
    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums2} | Output: {sol.containsDuplicate(nums2)}")  # Expected: False
    
    # Test Case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums3} | Output: {sol.containsDuplicate(nums3)}")  # Expected: True
