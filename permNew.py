from itertools import permutations
from operator import itemgetter


# https://stackoverflow.com/questions/23277518/modifying-heaps-algorithm-for-generating-permutations
def s_permutations(seq):
    def s_perm(seq):
        if not seq:
            return [[]]
        else:
            new_items = []
            for i, item in enumerate(s_perm(seq[:-1])):
                if i % 2:
                    new_items += [item[:i] + seq[-1:] + item[i:]
                                  for i in range(len(item) + 1)]
                else:
                    new_items += [item[:i] + seq[-1:] + item[i:]
                                  for i in range(len(item), -1, -1)]
            return new_items

    return [(tuple(item), -1 if i % 2 else 1)
            for i, item in enumerate(s_perm(seq))]

