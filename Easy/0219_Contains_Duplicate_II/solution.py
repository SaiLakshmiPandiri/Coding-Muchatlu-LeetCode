class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Set to maintain a sliding window of size at most k
        seen = set()
        
        for i, val in enumerate(nums):
            # If the current value is already in our sliding window set,
            # we found a duplicate within distance k
            if val in seen:
                return True
            
            seen.add(val)
            
            # Maintain window size k by removing the element that fell out of bounds
            if len(seen) > k:
                seen.remove(nums[i - k])
                
        return False


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Contains nearby duplicate within k=3
    nums1, k1 = [1, 2, 3, 1], 3
    print(f"Input: nums={nums1}, k={k1} | Output: {sol.containsNearbyDuplicate(nums1, k1)}")  # Expected: True
    
    # Test Case 2: Contains nearby duplicate within k=1
    nums2, k2 = [1, 0, 1, 1], 1
    print(f"Input: nums={nums2}, k={k2} | Output: {sol.containsNearbyDuplicate(nums2, k2)}")  # Expected: True
    
    # Test Case 3: Duplicate exists but distance > k=2
    nums3, k3 = [1, 2, 3, 1, 2, 3], 2
    print(f"Input: nums={nums3}, k={k3} | Output: {sol.containsNearbyDuplicate(nums3, k3)}")  # Expected: False
