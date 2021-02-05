# Using dictionaries
# Question: How many times does a vowel appear in a word?

avowel = ('a,e,i,o,u')
adictionary = {}
adictionary['e']=5
aword = input("Enter any word ")

for letter in aword:
    if letter in avowel:
        #ensures dictionary is always populated. No Key error exception. Using setdefault method
        adictionary.setdefault(letter, 0)

        adictionary[letter] += 1
        #using sorted and items method
for key, result in sorted(adictionary.items()):
    if result != 0:
        print(key, " appears ", result, " times")
