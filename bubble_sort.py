

# _________0___1___2___3___4____5___6
oldlist = [10, 75, 43, 15, 25, -4, 27]


def bubble_sort(seq):
    last_item = len(seq) - 1
    for z in range(0, last_item):
        for x in range(0, last_item):
            if seq[x] > seq[x + 1]:
                # swap them!
                seq[x], seq[x + 1] = seq[x + 1], seq[x]
    return seq
print('\n Not optimized')
print(bubble_sort(oldlist))

# __________________Optimized ver.______________


def bubble_sort_optimized(seq):
    last_item = len(seq) - 1
    for z in range(0, last_item):
        for x in range(0, last_item - z):  # ecxepting last item
            if seq[x] > seq[x + 1]:
                # swap them!
                seq[x], seq[x + 1] = seq[x + 1], seq[x]
    return seq
print('\n Optimized')
print(bubble_sort_optimized(oldlist))
