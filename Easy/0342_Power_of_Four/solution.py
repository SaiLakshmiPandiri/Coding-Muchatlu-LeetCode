# Problem: 342. Power of Four
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/power-of-four/
# Video Explanation (Telugu): https://youtu.be/YOUR_VIDEO_ID_HERE
#
# Time Complexity: O(log4 N) - repeatedly dividing n by 4
# Space Complexity: O(1) - only using constant extra space


class Solution(object):

    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfFour(16))  # Output: True
    print(sol.isPowerOfFour(5))   # Output: False
    print(sol.isPowerOfFour(1))   # Output: True
