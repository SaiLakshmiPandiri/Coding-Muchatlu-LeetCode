# Problem: 5. Longest Palindromic Substring
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/longest-palindromic-substring/
# Video Explanation (Telugu): https://youtu.be/wboieG5pX54
#
# Time Complexity: O(N^2) - center expansion algorithm
# Space Complexity: O(1) - auxiliary space


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s

        start = 0
        max_len = 1
        i = 0

        while i < n:
            # Remaining characters cannot form a longer palindrome
            if n - i <= max_len >> 1:
                break

            left = i
            right = i

            # Skip duplicate characters in bulk
            while right < n - 1 and s[right] == s[right + 1]:
                right += 1

            i = right + 1

            # Expand around center
            while right < n - 1 and left > 0 and s[right + 1] == s[left - 1]:
                right += 1
                left -= 1

            current_len = right - left + 1
            if current_len > max_len:
                start = left
                max_len = current_len

        return s[start : start + max_len]


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(sol.longestPalindrome("cbbd"))  # Output: "bb"
