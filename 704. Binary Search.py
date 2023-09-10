class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # If the target is not in the initial list
        if target not in nums:
            return -1
        
        # we need to set pointers if we are going to slice the list based off 
        # the middle element this will make it so we do not have to go 
        # through the enitre list and circumvent O(n) time
        mid = len(nums)//2
        lo = 0
        hi = len(nums)

        # while loop to perform calculation of mid = (lo + hi) // 2 then 
        # based off how mid works with target we can cut off the top half
        # of the bottom half of the list or just return the index of mid
        # if mid equals target
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid

        