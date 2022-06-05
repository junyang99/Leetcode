# https://leetcode.com/problems/longest-common-prefix/
def longestCommonPrefix(strs):
    ans = ""
    loop = min(len(s) for s in strs)
    flag = False
    for i in range(loop):
        char = strs[0][i]
        for word in strs[1::]:
            if char != word[i]:
                flag = True
                break
        if not flag:
            ans += char
    return ans


strs = ["flower", "flank", "flute"]
print(longestCommonPrefix(strs))
print("hello world")