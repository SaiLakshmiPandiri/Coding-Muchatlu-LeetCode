# Problem: 20. Valid Parentheses
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/valid-parentheses/
# Video Explanation (Telugu): https://youtu.be/Qm5-YyS9h6M
#
# Time Complexity: O(N) - single pass through characters
# Space Complexity: O(N) - stack memory for open brackets


class Solution(object):

    def isValid(self, s):
        stack = []

        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            elif not stack or stack.pop() != c:
                return False
        return not stack


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))  # Output: True
    print(sol.isValid("(]"))  # Output: False
