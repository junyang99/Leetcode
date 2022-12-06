def isPerfectSquare(num):
    if num == 1:
        return False

    for i in range(2, num):
        ans = num/i
        if ans == i:
            return True
    return False


print(isPerfectSquare(5))
