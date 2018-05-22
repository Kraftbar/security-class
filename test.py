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
print(m.hexdigest())

sizeof_list = 3

rand_pass = list()
rand_passHashed=list()


masterlist = [] * sizeof_list
masterlistHashed=[]*sizeof_list
counter = 0

# Generating random strings.
#  "Passwordlist of server"
# Setting them into the list
while counter < sizeof_list:
    counter = counter + 1
    rand_pass = list()
    rand_passHashed = list()
    for j in range(counter):
        word = myBib.randomString(3, 3)
        wordHashed=hashlib.md5(word.encode('utf-8')).hexdigest()

        rand_pass.append(word)
        rand_passHashed.append(wordHashed)

    masterlistHashed.append(rand_passHashed)
    masterlist.append(rand_pass)


pprint(masterlist)
pprint(masterlistHashed)

endListe = time.time()

rand_pass_hashed = list()


# Generating all the hashes
#   "of the passwordlist"
#
##     RUNNES TROUGH THE WHOLE MASTER LIST
#

### Calculating the perms before)


counter = 0




parmutations=myBib.findPerms(3,3)


tries=0
hashedStr=""
complBroken=0
found=0
hashesFound=0

counter=0
print(parmutations)
for passwordList in masterlistHashed:

    hashCollection = {}     # for each "file" gen a new dictionary
    passListLength = len(passwordList)
    print(" NEW LIST")
    counter=0
    for hashedPasw in passwordList:
        tries = 0
        while(1): # this is spinning while i dont want it
            print(counter)
            ## Check if it is in the dict
            ## else compute the hash and add it
            if( hashedPasw in hashCollection):
                print("found")
                found=1
                hashesFound=hashesFound+1

                if (found):
                    print(str(counter) + " Tries to find " + hashedPasw + "in" + str(passListLength))
                    break

            else:
                currentPermWord = parmutations[counter]  # out of boundes if the last perm is the correct
                currentPermWordHased=hashlib.md5(currentPermWord.encode('utf-8')).hexdigest()
                hashCollection[currentPermWordHased] = currentPermWord #kan hende de må bytte

            counter=counter+1
            tries=tries+1



        found = 0

    ## SJEKKE
        ## CONatins eller noe


## Attack using dictonary
print(hashCollection)

## Attack using arrylist
# print(rand_pass_hashed)


permutat = itertools.product(range(3), repeat=3)




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
permutat = itertools.product(range(3), repeat=3)
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
