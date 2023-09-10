class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        if c == 0:
            return True
        
        i = 0
        while i * i < c:
            
            value = c - (i * i)
            
            root = sqrt(value)
            
            if int(root + 0.5) ** 2 == value:
                return True
            
            i += 1
        
        return False
                
            
        