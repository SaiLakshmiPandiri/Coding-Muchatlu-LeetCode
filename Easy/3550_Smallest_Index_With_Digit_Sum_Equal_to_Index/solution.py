# Problem: 3550. Smallest Index With Digit Sum Equal to Index
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# Video Explanation (Telugu): https://youtu.be/-FnySlpe5ZI
#
# Time Complexity: O(N * log10(MAX_NUM)) - digit sum per element
# Space Complexity: O(1) - auxiliary space

from typing import List


class Solution:

    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num < 10 and i == num:
                return i
            s = 0
            while num:
                s += num % 10
                num //= 10
            if s == i:
                return i
        return -1


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestIndex([0, 1, 2]))  # Output: 0
