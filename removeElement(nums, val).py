def removeElement(nums, val):
    for i in nums:
        if i == val:
            nums.pop()
        return nums 


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))
