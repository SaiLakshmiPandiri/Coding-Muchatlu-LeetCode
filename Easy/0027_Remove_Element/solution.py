class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums.count(val) == len(nums):
            return 0
            
        low = 0
        high = len(nums) - 1
        
        while low < high:
            while high >= 0 and nums[high] == val:
                high -= 1
            if low >= high:
                break
            if nums[low] == val:
                nums[low], nums[high] = nums[high], nums[low]
                high -= 1
            else:
                low += 1
                
        return high + 1

# Local testing and verification
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Test 1 -> k: {k1}, Modified nums (first k elements): {nums1[:k1]}")
    
    # Test Case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Test 2 -> k: {k2}, Modified nums (first k elements): {nums2[:k2]}")
