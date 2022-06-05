#https://leetcode.com/problems/running-sum-of-1d-array/
def runningSum(nums):
    ans = []
    for i in range(len(nums)):
        if i == 0:
            ans.append(nums[i])
        else:
            ans.append(nums[i] + ans[i-1])
    return ans

nums = [1, 1, 1, 1]
print(runningSum(nums))