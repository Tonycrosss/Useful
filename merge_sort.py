import sys

seq = [5, 9, 1, 2, 4, 8, 6, 3, 7]


def merge_sort(seq, first=0, last=len(seq) - 1):
    if first < last:
        middle = (first + last) // 2
        merge_sort(seq, first, middle)
        merge_sort(seq, middle + 1, last)
        merge(seq, first, middle, last)


def merge(seq, first, middle, last):
    L = seq[first:middle + 1]
    R = seq[middle + 1:last + 1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0

    for k in range(first, last + 1):
        if L[i] <= R[j]:
            seq[k] = L[i]
            i += 1
        else:
            seq[k] = R[j]
            j += 1


print(seq)
merge_sort(seq)
print(seq)