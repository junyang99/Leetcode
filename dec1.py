def two_sum(num_lst, target):
    index_1_counter = -1
    for index_1 in num_lst:
        index_2_counter = 0
        index_1_counter += 1

        for index_2 in num_lst[1::]:
            index_2_counter += 1
            ans = index_1 + index_2
            if ans == target:
                return [index_1_counter, index_2_counter]

num_lst = [3, 3]
target = 6
print(two_sum(num_lst, target))

