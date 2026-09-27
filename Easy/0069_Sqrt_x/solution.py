# Problem: 69. Sqrt(x)
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/sqrtx/
# Video Explanation (Telugu): https://youtu.be/q34WV6ZnYYM
#
# Time Complexity: O(sqrt(X)) - linear count up to square root
# Space Complexity: O(1) - auxiliary space


class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i * i <= x:
            i += 1
        return i - 1


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(8))  # Output: 2
