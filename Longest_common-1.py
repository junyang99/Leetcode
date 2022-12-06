# def longestCommonPrefix(strs):
#     shortest_word = "qwertyuiopasdfghjklzxcvbnm"
#     loop = []
#     prefix = ""
#     ans = ""
#     counter = -1
#     for i in range(len(strs)):
#         loop.append(i)
#         if len(strs[i]) < len(shortest_word):
#             shortest_word = strs[i]

#     for i in loop:

#         for q in range(len(shortest_word)):
#             if i != loop[-1]:
#                 if strs[i][q] == strs[i+1][q]:
#                     prefix += strs[i][q]
#     print(prefix)

    # for q in range(len(shortest_word)):
    #     for i in range(len(strs)):
    #         if len(ans) > 0 and len(ans) < i:
    #             continue
    #         elif prefix[q] == strs[i][q]:
    #             ans += prefix[q]
    #             continue
    # print(ans)

# strs = ["flower","flow","flight"]
# longestCommonPrefix(strs)
# def getshortestword(strs):
#     shortest_word = "qwertyuiopasdfghjklzxcvbnm"    
#     for i in range(len(strs)):
#         if len(strs[i]) < len(shortest_word):
#             shortest_word = strs[i]
#     return shortest_word

# def longestCommonPrefix(strs):
#     check_1 = ""
#     ans = ""
#     counter = 0
#     shortest_word = getshortestword(strs)

#     strs.remove(shortest_word)

#     for word in strs:
#         counter = -1

#         for char in word:
#             counter += 1

#             for i in range(len(strs)):
#                 if counter < len(strs[i]):
#                     if check_1 == "":
#                         if char == strs[i][counter]:
#                             check_1 += char

#                     elif char == strs[i][counter]:
#                         a = check_1[-1]
#                         b = strs[i][counter]
#                         if char != check_1[-1]:
#                             check_1 += char
#     return check_1


def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        
        for i in zip(*strs):
            if len(set(i)) == 1:
                prefix.append(i[0])
            else:
                break
        
        return "".join(prefix)
        

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

