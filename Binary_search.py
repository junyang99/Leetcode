# https://leetcode.com/problems/binary-search/
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(search(nums, target))
