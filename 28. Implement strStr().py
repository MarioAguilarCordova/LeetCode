def strStr(haystack: str, needle: str) -> int:

    if len(needle) == 0: return 0

    j = 0

    for i in range(len(haystack) - 1):

        # print(haystack[i], " ", needle[j])

        if haystack[i] == needle[j]:

            j += 1

    return j if j == len(needle) else -1

def main():

    print(strStr(haystack="hello",needle="ll"),"\n")
    print(strStr(haystack="aaaaaaaaaa",needle="bba"))


main()