

old_list = [7, 8, 5, 4, 9, 2]


def selection_sort(seq):
    for i in range(0, len(seq) - 1):
        min_index = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq

print(selection_sort(old_list))