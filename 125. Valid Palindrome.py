class Solution:
    def isPalindrome(self, s: str) -> bool:

        punc_list = '''`#!()-[]{};*:'"\,<>./?@_~'''

        for i in punc_list:
            s = s.replace(i,"")
        
        s = s.replace(" ","")
        s = s.lower()

        print(s)

        reverse = s[::-1]

        if s != reverse:
            return False

        return True
        