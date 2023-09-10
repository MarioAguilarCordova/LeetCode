def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        diction = {}

        k = len(nums)

        for i in range(len(nums) - 1):

            if not diction.get(nums[i]):

                diction[nums[i]] = 1
            else:

                nums.pop(nums[i])
                k -= 1

        return k

def main():

    nums = [0,0,1,1,2,2,3,3,4,4]

    answer = removeDuplicates(nums)

    print(answer)


main()