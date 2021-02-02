# Challenge: Transform the string "Don't Panic" to the string "On tap" using list methods
phrase = "Don't Panic!"
plist = list(phrase)
blist = plist.copy()

print(plist)

for i in range(4):
    # Using pop method. Removes items from list from right side default
    plist.pop()

print(plist)

plist.pop(0)
print(plist)

# using remove method to remove a specific character
plist.remove("'")
print(plist)

# using extend method to concatenate two lists.
plist.extend([plist.pop(), plist.pop()])
print(plist)

# using insert method to add from left
plist.insert(2, plist.pop(3))
print(plist)

# using copy method to duplicate a list.
secondlist = plist.copy()
print(secondlist)

# using start stop and step
thirdlist = plist[1:4:2]
print(thirdlist)

# reversing an array in place (Remove the hashes)
# newlist=list(input("enter anything "))
# newlist2=newlist[::-1]
# print(newlist2)

# Challenge: Transform the string "Don't Panic" to the string "On tap" using list methods using slices
phrase2 = "Don't Panic"
phrase3 = list(phrase2)
print(phrase3)
phrase4 = ''.join(phrase3[1:3])
phrase4 = phrase4 + (''.join(phrase3[5])) + (''.join(phrase3[4])) + (''.join(phrase3[7])) + (''.join(phrase3[6]))
print(phrase4)

# Function that finds the missing number in an unsorted array containing every one of the other 99 numbers ranging from 1-100
import random

lista = []
listab = []
count = 0
for i in range(1, 101):
    lista.append(i)
while count < 99:
    listac = random.randint(1, 100)
    if listac not in listab:
        listab.append(listac)
        count += 1
print(lista)
print(listab)
for k in lista:
    if k not in listab:
        print("Missing Value=> ", k , '\n')

#Function that finds duplicate number in an unsorted array containing every number from 1-100
listad = []
listaf=[]
count2 = 0
while count2 < 100:
    listae = random.randint(1, 100)
    if listae not in listad:
        listad.append(listae)
        count2 += 1
print(listad)

dup=random.randint(0,99)
dup2=listad[dup]
listad.append(dup2)
print(listad)
print(len(listad))
for l in listad:
    if l not in listaf:
        listaf.append(l)
    else:
        print("the imposter =>", l)