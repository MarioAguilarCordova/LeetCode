def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """

        word = str(x)

        length = len(word)

        for i in range(length):
            
            if word[i] != word[length - 1]:

                return False

            length = length - 1

        return True


def main():

    x = 121

    isPalindrome(x)

main()