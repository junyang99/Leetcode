def ishappy(n):
    counter = 0
    while n != 1:
        new_n = 0
        for i in str(n):
            new_n += int(i)**2
            n = new_n
            counter += 1
        if counter >= 30:
            return False
    return True


print(ishappy(2))
