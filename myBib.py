import itertools
import random

def randomString(kombinasjoner,lengde):
    b=kombinasjoner+96
    random.randint(97, b)
    retur=list()
    for i in range(lengde):
        retur.append(chr(random.randint(97, b)))

    return ''.join(retur)


def numbersToString(kombiansjoner, lengde):
    kombiansjoner=kombiansjoner+96
    permutatt = itertools.product(range(kombiansjoner), repeat=lengde)
    retur = list()
    for line in permutatt:
        word=list()
        for k in line:
             word.append(chr(k))
        ''.join(word)
        retur.append(word)
    return retur