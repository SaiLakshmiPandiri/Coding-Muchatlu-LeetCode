# Problem: 35. Search Insert Position
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/search-insert-position/
# Video Explanation (Telugu): https://youtu.be/q4qytFt3kP4
#
# Time Complexity: O(N) - scanning through elements or checking list membership
# Space Complexity: O(1) - constant auxiliary space


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        elif target < nums[-1]:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i
        else:
            return len(nums)


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))  # Output: 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # Output: 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # Output: 4
