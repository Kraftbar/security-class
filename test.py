import hashlib, binascii, random
import time
import permNew
import perm
from itertools import permutations
from operator import itemgetter
import itertools
import myBib
import permNyTest
import permTesting
from multiprocessing import Pool

start = time.time()
from pprint import pprint






m = hashlib.md5()
m.update("Nobody will care".encode('utf-8'))
# print(m.hexdigest())

sizeof_list = 3

rand_pass = list()

masterlist = [] * sizeof_list

counter = 0

# Generating random strings.
#  "Passwordlist of server"
# Setting them into the list
while counter < sizeof_list:
    counter = counter + 1
    rand_pass = list()
    masterlist.append(rand_pass)
    for j in range(counter):
        word = myBib.randomString(3, 3)
        rand_pass.append(word)

endListe = time.time()

rand_pass_hashed = list()


# Generating all the hashes
#   "of the passwordlist"
#
##     RUNNES TROUGH THE WHOLE MASTER LIST
#

### Calculating the perms before
permutat = itertools.product(range(3), repeat=3)

print(permutat)

hashedStr=""
complBroken=0
for passwordList in masterlist:
    hashCollection = {}     # for each "file" gen a new dictionary
    for randWord in passwordList:
        while not complBroken:
            complBroken=1   # test
            m.update(randWord.encode('utf-8'))
            hashedStr=m.hexdigest()
            if( hashedStr in hashCollection):
                print("found")
            hashCollection[randWord] = hashedStr
        complBroken = 0

    ## SJEKKE
        ## CONatins eller noe


## Attack using dictonary
print(hashCollection)

## Attack using arrylist
# print(rand_pass_hashed)






endHash = time.time()
##
# Display -- Random for the display
###
for i in rand_pass:
    rand_pass_hashed.append(m.hexdigest())  # Random line for the display, nevermind this

newList = [rand_pass, rand_pass_hashed]
print("		Hased to MD5")
lineText = "-------------------------------------------------"
print(lineText)
for i in range(sizeof_list):
    print("|   " + rand_pass[i] + " --> " + rand_pass_hashed[i] + "    |")
print(lineText)

print("		Permuations:")
print(lineText)
print("|   ", end='')
permutat = itertools.product(range(4), repeat=3)
counter = 0
for line in permutat:
    counter = counter + 1
    print("   " + chr(65 + line[0]) + chr(65 + line[1]) + chr(65 + line[2]) + "  ", end='')
    if (0 == (counter % 5)):
        print("    |")
        print("|   ", end='')
print()
print(lineText)

print("Time elapced liste :" + str(endListe - start) + "\n\n")
print("Time elapced hash:" + str(endHash - endListe) + "\n\n")
