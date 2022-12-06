#check on listnode vs normal list 

def mergeTwoLists(list1, list2):
    ans = []
    for i in range(len(list1)):
        ans.append(list1[i])
        ans.append(list2[i])
    return ans




lst1 = [1, 2, 4]
lst2 = [1, 3, 4 ]
print(mergeTwoLists(lst1, lst2))

# tup_lst = list(zip(list1, list2))
# ans = []
    # for indi_tup in tup_lst:
    #     for i in indi_tup:
    #         ans.append(i)
    # return ans