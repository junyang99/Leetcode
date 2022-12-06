def two_sum(num_lst, target):
    for i in range(len(num_lst)):
        for q in range(len(num_lst)):
            if i == q:
                continue
            if num_lst[i] + num_lst[q] == target:
                return [i, q]

num_lst = [3,3]
target = 6
print(two_sum(num_lst, target))