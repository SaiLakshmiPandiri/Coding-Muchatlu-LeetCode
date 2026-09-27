# Problem: 9. Palindrome Number
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/palindrome-number/
# Video Explanation (Telugu): https://youtu.be/BEtwm0vMkeQ
#
# Time Complexity: O(log10(N)) - reversing half of the digits
# Space Complexity: O(1) - no extra string conversion used


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse = 0

        while x > reverse:
            reverse = reverse * 10 + (x % 10)
            x //= 10
        return x == reverse or x == reverse // 10


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))  # Output: True
    print(sol.isPalindrome(-121))  # Output: False
