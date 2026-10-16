class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Frequency array for 26 lowercase English letters
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        # If all counts returned to 0, it's an anagram
        return count.count(0) == 26


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Valid Anagram
    s1, t1 = "anagram", "nagaram"
    print(f"Input: s='{s1}', t='{t1}' | Output: {sol.isAnagram(s1, t1)}")  # Expected: True
    
    # Test Case 2: Not an Anagram
    s2, t2 = "rat", "car"
    print(f"Input: s='{s2}', t='{t2}' | Output: {sol.isAnagram(s2, t2)}")  # Expected: False
