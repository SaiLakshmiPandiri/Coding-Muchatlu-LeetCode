class Solution(object):
    def scoreOfParentheses(self, s):
        """:type s: str
        :rtype: int
        """
        # Approach: Using a stack to accumulate scores based on nesting levels.
        # Initialize stack with a baseline score of 0 for the outer level.
        stack = [0]

        for char in s:
            if char == "(":
                # A new opening parenthesis starts a nested block with initial score 0
                stack.append(0)
            else:
                # When encountering ')', pop the score of the inner block
                v = stack.pop()
                # If v == 0, it means it's an immediate "()" pair (score 1).
                # Otherwise, it's a nested "(A)" block which doubles the score (2 * v).
                score = 1 if v == 0 else 2 * v
                # Add this score to the parent block's accumulator
                stack[-1] += score

        return stack[0]

# Complexity Analysis & Example Test Runs:
# ----------------------------------------------------
# Time Complexity: O(N) - Where N is the length of the string s. We iterate through each character once.
# Space Complexity: O(N) - In the worst-case scenario (e.g., nested parentheses like "((...))"), the stack will grow up to O(N) depth.
#
# Example Test Run:
# Input: s = "(()())"
# - '(' -> stack = [0, 0]
# - '(' -> stack = [0, 0, 0]
# - ')' -> v = 0 -> score = 1 -> stack = [0, 1]
# - '(' -> stack = [0, 1, 0]
# - ')' -> v = 0 -> score = 1 -> stack = [0, 1 + 1] = [0, 2]
# - ')' -> v = 2 -> score = 2 * 2 = 4 -> stack = [0 + 4] = [4]
# Output: 4
