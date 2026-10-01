# Problem: 58. Length of Last Word
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/length-of-last-word/
# Video Explanation (Telugu): https://youtu.be/dNsmhlHM_7w
#
# Time Complexity: O(N) - splitting the string and traversing characters
# Space Complexity: O(N) - storing the list of words from split()


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = list(map(str, s.split()))
        return len(lst[-1])


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))                 # Output: 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  ")) # Output: 4
    print(sol.lengthOfLastWord("luffy is still joyboy"))       # Output: 6
