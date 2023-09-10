class Solution:
    def isPalindrome(self, s: str) -> bool:

        punc_list = '''`#!()-[]{};*:'"\,<>./?@_~'''

        for i in punc_list:
            s = s.replace(i, "")

        s = s.replace(" ", "")
        s = s.lower()

        l, r = 0, len(s) - 1

        while l < r:

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
