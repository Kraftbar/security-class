import hashlib, binascii, random
import time
import permNew
import perm
from itertools import permutations
from operator import itemgetter
import itertools
import permNyTest
import permTesting
from multiprocessing import Pool
start = time.time()

m = hashlib.md5()
m.update("Nobody will care".encode('utf-8'))
print(m.hexdigest())

rand_pass = [''] * 10
print(rand_pass)

# Generating random strings.
for i in range(10):
    a = [random.randint(65, 67), random.randint(65, 67), random.randint(65, 67)]
    b = chr(a[0]) + chr(a[1]) + chr(a[2])
    rand_pass[i] = b
    print(b)

print(type(m))
rand_pass_hashed = list()

# hashing all MD5
for i in range(10):
    print("liste")
    m.update(rand_pass[i].encode('utf-8'))  # can move .encode('utf-8') to the rand_pass[i]=b line
    rand_pass_hashed.append(m.hexdigest())

newList = [rand_pass, rand_pass_hashed]


end = time.time()

# Display
print("		Hased to MD5")
line = "-------------------------------------------------"
print(line)
for i in range(10):
    print("|   " + rand_pass[i] + " --> " + rand_pass_hashed[i] + "    |")
print(line)

print("Time elapced:"+str(end - start)+"\n\n")


print("		Permuations:")
permutat=itertools.product(range(3), repeat=3)
for line in permutat:
    print(chr(65 + line[0]) + chr(65 + line[1]) + chr(65 + line[2]))
