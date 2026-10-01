# Problem: 1614. Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Video Explanation (Telugu): https://youtu.be/YOUR_VIDEO_ID_HERE
#
# Time Complexity: O(N) - single pass through the string
# Space Complexity: O(1) - constant auxiliary space


class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = curr = 0
        for i in s:
            if i == '(':
                curr += 1
                res = max(curr, res)
            elif i == ')':
                curr -= 1
        return res


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))  # Output: 3
    print(sol.maxDepth("(1)+((2))+(((3)))"))    # Output: 3
    print(sol.maxDepth("()(())((()()))"))       # Output: 3
