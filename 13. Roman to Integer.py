def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """

        result = 0

        diction = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        for i in range(len(s)):
           if i + 1 != len(s):
               if diction[s[i]] >= diction[s[i+1]]:
                    result += diction[s[i]]
               else:
                   result -= diction[s[i]]
           else:
                result += diction[s[i]]

           print(result)


        return result


def main():

    s = "MCMXCIV"

    answer = romanToInt(s)

    print(answer)

main()