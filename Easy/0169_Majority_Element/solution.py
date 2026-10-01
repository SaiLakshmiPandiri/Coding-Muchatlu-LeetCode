#Problem: 169. Majority Element
#Difficulty: Easy
#LeetCode Link: https://leetcode.com/problems/majority-element/
#Video Explanation (Telugu): https://youtu.be/EEKirc1I0Sg
#Time Complexity: O(N) - traversing the array to record and check element frequencies
#Space Complexity: O(N) - storing element counts in the dictionary
class Solution(object):
def majorityElement(self, nums):
"""
:type nums: List[int]
:rtype: int
"""
dict = {}
for i in nums:
dict[i] = dict.get(i, 0) + 1
if dict[i] > len(nums) // 2:
return i
return 0

#Example test run:
if name == "main":
sol = Solution()
print(sol.majorityElement([3, 2, 3]))              # Output: 3
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
