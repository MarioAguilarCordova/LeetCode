class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
          
            num = ''.join([str(i) for i in digits])
            result = int(num) + 1
            return [int(i) for i in str(result)]
    