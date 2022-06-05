# https://leetcode.com/problems/palindrome-number/
def palindrome(x):
    for i in range(1, len(str(x))):
        if str(x)[i-1] != str(x)[-i]:
            return False
    return True

print(palindrome(x))