def strStr(haystack, needle):
    ans = -1
    if needle == haystack and len(needle) > 0:
        return 0
    if needle in haystack:
        ans = haystack.find(needle)
        return ans 
    else:
        return ans

haystack = "mississippi"
needle = "issip"

print(strStr(haystack, needle))