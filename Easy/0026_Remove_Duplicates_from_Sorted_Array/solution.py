# Problem: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Video Explanation (Telugu): https://youtu.be/9fc22zeZNR4
#
# Time Complexity: O(N^2) due to list popping and frequency counts during iteration
# Space Complexity: O(1) - in-place modification of the array


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int  
        """
        for i in range(len(nums) - 1, -1, -1):
            if len(nums) == nums.count(nums[i]):
                return 1
            elif nums.count(nums[i]) > 1:
                nums.pop(i)
        return len(nums)


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: [1, 1, 2] -> k = 2, nums[:2] = [1, 2]
    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(f"k = {k1}, nums = {nums1[:k1]}")  # Output: k = 2, nums = [1, 2]

    # Test 2: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> k = 5, nums[:5] = [0, 1, 2, 3, 4]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(f"k = {k2}, nums = {nums2[:k2]}")  # Output: k = 5, nums = [0, 1, 2, 3, 4]
