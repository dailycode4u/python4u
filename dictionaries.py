# Using dictionaries
# Question: How many times does a vowel appear in a word?

avowel = ('a,e,i,o,u')
adictionary = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
aword = input("Enter any word ")

for letter in aword:
    if letter in avowel:
        adictionary[letter] += 1
for key,result in sorted(adictionary.items()):
    print(key, " appears ", result , " times")


