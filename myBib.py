import random

def randomString(kombinasjoner,lengde):
    b=kombinasjoner+96
    random.randint(97, b)
    retur=list()
    for i in range(lengde):
        retur.append(chr(random.randint(97, b)))

    return ''.join(retur)