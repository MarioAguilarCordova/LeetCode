class Solution:
    def climbStairs(self, n: int) -> int:
        
        arr = [0,1]
        
        for i in range(n):
            arr.append(arr[-1]+arr[-2])
            
        return arr[-1]
            
            
        