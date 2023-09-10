class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        diction = {}
        for x in nums:
            if diction.get(x) == None:
                diction[x] = 1
            else:
                return True
        return False
