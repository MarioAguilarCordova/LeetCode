class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        p1,p2 = 0,1

        while not(numbers[p1] + numbers[p2] == target):
            print(numbers[p1], " ", numbers[p2])
            if numbers[p1] + numbers[p2] < target:
                p2 += 1
                p1 += 1
            else:
                p1 -= 1
        print(numbers[p1], " ", numbers[p2])
        return [p1+1,p2+1]
