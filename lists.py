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

#reversing a list (Remove the tags)
#newlist=list(input("enter anything "))
#newlist2=newlist[::-1]
#print(newlist2)

# Challenge: Transform the string "Don't Panic" to the string "On tap" using list methods using slices
phrase2="Don't Panic"
phrase3=list(phrase2)
print(phrase3)
phrase4 = ''.join(phrase3[1:3])
phrase4 = phrase4 +(''.join(phrase3[5:6]))+ (''.join(phrase3[4:5]))+(''.join(phrase3[7:8]))+(''.join(phrase3[6:7]))
print(phrase4)
