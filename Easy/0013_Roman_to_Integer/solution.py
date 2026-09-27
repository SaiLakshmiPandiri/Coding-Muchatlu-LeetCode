# Problem: 13. Roman to Integer
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/roman-to-integer/
# Video Explanation (Telugu): https://youtu.be/T5U0JGTqMEo
#
# Time Complexity: O(N) - iterating through string length
# Space Complexity: O(1) - fixed dictionary size for Roman symbols


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for symbol in s:
            result += dict[symbol]

        if "CM" in s or "CD" in s:
            result -= 200
        if "XL" in s or "XC" in s:
            result -= 20
        if "IV" in s or "IX" in s:
            result -= 2

        return result


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))  # Output: 1994
