# Challenge: Transform the string "Don't Panic" to the string "On tap" using list methods

phrase = "Don't Panic!"
plist = list(phrase)

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
thirdlist = plist[1:4:1]
print(thirdlist)
