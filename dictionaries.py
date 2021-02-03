# Using dictionaries
# Question: How many times does a vowel appear in a word?

avowel = ('a,e,i,o,u')
adictionary = {}

adictionary['a'] = 0
adictionary['e'] = 0
adictionary['i'] = 0
adictionary['o'] = 0
adictionary['u'] = 0

aword = input("Enter any word ")

for letter in aword:
    if letter in avowel:
        adictionary[letter] += 1
for key, result in sorted(adictionary.items()):
    if result != 0:
        print(key, " appears ", result, " times")

