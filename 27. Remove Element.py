def removeElement( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0

        for j in range(len(nums)):

            if (nums[j] != val):

                nums[i] = nums[j]
                i += 1

            print(nums)

        return nums
                
        
        
def main():

    nums = [3,2,2,3]
    val = 3

    print(removeElement(nums,val))



main()