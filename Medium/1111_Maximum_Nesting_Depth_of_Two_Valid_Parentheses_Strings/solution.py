class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        # Approach: Distribute parentheses alternatingly based on current nesting depth parity.
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                depth += 1
                # Assign to group A (0) or B (1) based on odd/even depth
                ans.append(depth % 2)
            else:  # char == ')'
                # Close the parenthesis from the corresponding group
                ans.append(depth % 2)
                depth -= 1
                
        return ans

# Complexity Analysis & Example Test Runs:
# ----------------------------------------------------
# Time Complexity: O(N) - Where N is the length of the string seq. We iterate through the string exactly once.
# Space Complexity: O(N) - To store and return the result array of length N.
#
# Example Test Run:
# Input: seq = "(()())"
# - '(' -> depth = 1 -> ans.append(1 % 2) -> 1 [Group B]
# - '(' -> depth = 2 -> ans.append(2 % 2) -> 0 [Group A]
# - ')' -> ans.append(2 % 2) -> 0, depth = 1
# - '(' -> depth = 2 -> ans.append(2 % 2) -> 0 [Group A]
# - ')' -> ans.append(2 % 2) -> 0, depth = 1
# - ')' -> ans.append(1 % 2) -> 1, depth = 0
# Output: [1, 0, 0, 0, 0, 1] (or valid alternative mapping)
