textfile = open('textfile.txt', 'a')

print('Test data ', file=textfile)
ans = input('Enter anything ')
print(ans, file=textfile)
textfile.close()

readfile = open('textfile.txt')

for data in readfile:
    print(data,end='')
readfile.close()

#Using the with statement to write data is more effecient

with open('textfile.txt','w') as textfile2:
    print('New way', file=textfile2)
