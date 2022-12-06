def findTheDistanceValue(arr1, arr2, d):
    count = 0
    for num1 in arr1:
        for num2 in arr2:
            if abs((num1 - num2)) <= d:
                count += 1
                break
    return len(arr1) - count


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))
