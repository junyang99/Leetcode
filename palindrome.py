def palindrome(x):
        num = str(x)
        loop_counter = 0
        for i in range(len(num)):
            a = num[i]
            loop_counter += 1
            a = num[i]
            b = num[-loop_counter]
            if num[i] != num[-loop_counter]:
                return False

        return True


x = 121
print(palindrome(x))