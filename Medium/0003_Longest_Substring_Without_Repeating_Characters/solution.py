# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Video Explanation (Telugu): https://youtu.be/bu0vLYIPt4s
#
# Time Complexity: O(N) - single pass with sliding window
# Space Complexity: O(min(N, M)) - hash map storing character indices (M is charset size)


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        max_len = 0

        for right, num in enumerate(s):
            if num in seen and seen[num] >= left:
                left = seen[num] + 1
            max_len = max(max_len, right - left + 1)
            seen[num] = right

        return max_len


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(
        sol.lengthOfLongestSubstring("abcabcbb")
    )  # Output: 3 (substring: "abc")
    print(sol.lengthOfLongestSubstring("bbbbb"))  # Output: 1 (substring: "b")
    print(
        sol.lengthOfLongestSubstring("pwwkew")
    )  # Output: 3 (substring: "wke")
