

old_list = [2, 6, 9, 7, 8]


def insertion_sort(seq):
    for i in range(1, len(seq)):
        for j in range(i - 1, 0, -1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
            else:
                break
    return seq

print(insertion_sort(old_list))


#  ___________optimized version_______
old_list = [2, 6, 9, 7, 8]


def insertion_sort_optimized(seq):
    for i in range(1, len(seq)):
        cur_num = seq[i]
        for j in range(i - 1, 0, -1):
            if seq[j] > cur_num:
                seq[j + 1] = seq[j]
            else:
                seq[j + 1] = cur_num
                break
    return seq

print(insertion_sort_optimized(old_list))