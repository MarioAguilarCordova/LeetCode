class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l = len(nums1)-1
        for i in range(n):
            nums1.pop(l-i)
        nums1.extend(nums2)
        nums1.sort()