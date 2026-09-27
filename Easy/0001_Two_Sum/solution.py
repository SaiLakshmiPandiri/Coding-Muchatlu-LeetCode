# Problem: 1. Two Sum
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/two-sum/
# Video Explanation (Telugu): https://youtu.be/x2CC-_4OsxA
#
# Time Complexity: O(N) - single pass through the list
# Space Complexity: O(N) - hash map stores up to N elements


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]

        :type target: int

        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], i]

            seen[num] = i


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
