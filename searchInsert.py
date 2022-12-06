def searchInsert(nums, target):
    i = 0
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    else:
        while target > nums[i]:
            i += 1
        return i


nums = [1, 3, 5, 6]
target = 7
print(searchInsert(nums, target))
