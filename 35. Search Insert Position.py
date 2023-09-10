def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # for i in range(len(nums) - 1):

        #     if nums[i] == target:

        #         return i
            
        #     elif target < nums[i] and i == 0:
                
        #         return i
            
        #     elif nums[i] < target and i + 1 < len(nums) and target < nums[i + 1]:
                
        #         return i + 1
            
        
        # return len(nums)

        # Faster Solution

        # index =0
        # for i in range(len(nums)):
        #     if target<= nums[i]:
        #         return index
        #     else:
        #         index = index + 1
        # return index

        # My attempt at binary search

        # n = len(nums)
        # left = 0
        # right = n - 1
        
        # while left <= right:
        #     middle = (left + right) // 2
        #     if target < nums[middle]:
        #         right = middle - 1
        #     elif target > nums[middle]:
        #         left = middle + 1
        #     elif nums[middle] < target and middle + 1 < len(nums) and target < nums[middle + 1]:
                
        #         return middle + 1
        #     else:
        #         print(middle)
        #         return middle
        #     print(middle)

        # return len(nums)

        left = 0
        right = len(nums) - 1
    
        while left <= right:
            middle = (left + right)//2
            if nums[middle] == target: 
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

            print(left)
            print(right)
            print(middle)
            
        return len(nums)


def main():

    nums = [1,3,5,6]

    target = 2

    print(searchInsert(nums,target))
    print("\n")

    nums2 = [1,3,5,6]

    target2 = 7

    print(searchInsert(nums2,target2))




main()