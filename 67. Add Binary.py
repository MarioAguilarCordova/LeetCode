class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        bin_sum = lambda a,b : bin(int(a,2) + int(b,2))
        return str(bin_sum(a,b)[2:])