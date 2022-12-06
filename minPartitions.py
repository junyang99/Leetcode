def minPartitions(n):
    highest_digit = 0
    for digit in n:
        a = int(digit)
        if a > highest_digit:
            highest_digit = a
    return highest_digit

n = "27346209830709182346"
print(minPartitions(n))