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

sizeof_list=20

rand_pass = list()

masterlist=[]*sizeof_list

teller=0



# Generating random strings.
#  "SERVER SIDE"
# Setting them into the list
while teller<sizeof_list:
    teller=teller+1
    rand_pass=list()
    masterlist.append(rand_pass)
    for j in range(teller):
        a = [random.randint(65, 67), random.randint(65, 67), random.randint(65, 67)]
        b = chr(a[0]) + chr(a[1]) + chr(a[2])
        word=myBib.randomString(3,3)
        rand_pass.append(word)

pprint(masterlist)

print(type(m))
rand_pass_hashed = list()



#
for i in range(sizeof_list):
    m.update(rand_pass[i].encode('utf-8'))  # can move .encode('utf-8') to the rand_pass[i]=b line
    rand_pass_hashed.append(m.hexdigest())

newList = [rand_pass, rand_pass_hashed]


end = time.time()

# Display
print("		Hased to MD5")
lineText = "-------------------------------------------------"
print(lineText)
for i in range(sizeof_list):
    print("|   " + rand_pass[i] + " --> " + rand_pass_hashed[i] + "    |")
print(lineText)

print("Time elapced:"+str(end - start)+"\n\n")


print("		Permuations:")
print(lineText)
print("|   ",end='')
permutat=itertools.product(range(3), repeat=3)
counter=0
for line in permutat:
    counter=counter+1
    print("   " +  chr(65 + line[0]) + chr(65 + line[1]) + chr(65 + line[2])+"  ", end='')
    if(0==(counter%5)):
        print("    |")
        print("|   ",end='')
print()
print(lineText)




