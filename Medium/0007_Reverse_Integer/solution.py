# Problem: 7. Reverse Integer
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/reverse-integer/
# Video Explanation (Telugu): https://youtu.be/kEvCRRgUrqk
#
# Time Complexity: O(log10(X)) - number of digits in X
# Space Complexity: O(1) - constant auxiliary space


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x:
            digit = x % 10
            x //= 10

            if rev > (2**31 - 1 - digit) // 10:
                return 0

            rev = rev * 10 + digit
        return sign * rev


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))  # Output: 321
    print(sol.reverse(-123))  # Output: -321
