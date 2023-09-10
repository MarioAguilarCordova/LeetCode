# My first Hard Leet Code Question Ever!

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 != 0:
            median = nums1[len(nums1) // 2]
        else:
            middle = len(nums1) // 2
            median = (nums1[middle] + nums1[middle - 1]) / 2
            
            
        return nums1 and median