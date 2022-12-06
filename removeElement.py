def removeElement(nums, val):
    index = []
    for i in range(len(nums)):
        if nums[i] == val:
            index.append(i)
    
    second_list = []
    counter = 0
    for i in index:
        second_list.append(i-counter)
        counter += 1
    for i in second_list:
        nums.pop(i)
    return len(nums)


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))
