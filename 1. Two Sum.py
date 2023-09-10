def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(i)
                if nums[j] == target - nums[i]:
                
                    return [i,j]      
    
def main():
        
    nums = [3,2,4]
        
    answer = twoSum(nums, 6)

    print(answer)

main()