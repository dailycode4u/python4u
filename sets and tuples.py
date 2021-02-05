#SETS
# key characteristics of sets is duplicate values are forbidden

sampleset = {'a', 'e', 'i', 'o', 'u', '5', '3', '3', '5', 'a'}
print(sorted(sampleset))  # notice the lack of duplicates in the output

word = "dawn48qwer123"

# Find items in the sampleset that are missing in the word
d = sampleset.difference(set(word))
print(d)

# join two sets
e = sampleset.union(set(word))
print(e)

# Find vowel in word
f = sampleset.intersection(set(word))
print(f)

#TUPLES
# Tuples are just immutable lists that are represented by parenthesis

mytuple = ('a', 'b', 'c')
mylist = ['a', 'b', 'c']
print(type(mytuple))
print(type(mylist))
# remember: every tuple needs to include at least one comma between the parenthesis
mytuple2 = ('tuple',)
notatuple = ('string')
print(type(mytuple2))
print(type(notatuple))
