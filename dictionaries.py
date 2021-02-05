# Using dictionaries
# Question: How many times does a vowel appear in a word?

avowel = ('a,e,i,o,u')
adictionary = {}
aword = input("Enter any word ")

for letter in aword:
    if letter in avowel:
        if letter not in adictionary:
            adictionary[letter] = 0
    adictionary[letter] += 1
for key, result in sorted(adictionary.items()):
    if result != 0:
        print(key, " appears ", result, " times")
