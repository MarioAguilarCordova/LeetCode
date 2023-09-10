def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        m = {")": "(", "}": "{", "]": "["}
        

        for i in s:
                if i in ('(','{', '['):
                        stack.append(i)
                else:
                    if not stack or stack.pop() != m[i]:
                        return False


        return not stack




def main():

        stri = "()"

        result = isValid(stri)

        print(result)

main()