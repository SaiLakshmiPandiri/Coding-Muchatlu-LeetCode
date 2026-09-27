# Problem: 125. Valid Palindrome
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/valid-palindrome/
# Video Explanation (Telugu): https://youtu.be/TSLr5pzlhZE
#
# Time Complexity: O(N) - string filtering and reversal
# Space Complexity: O(N) - array memory for filtered characters


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        for i in s.lower():
            if i.isalnum():
                lst.append(i)
        if lst == lst[::-1]:
            return True
        else:
            return False


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(
        sol.isPalindrome("A man, a plan, a canal: Panama")
    )  # Output: True
