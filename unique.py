file = open('F:/education/7thsem/ED/sept 11/Ram.txt','r+')
lines = file.readlines()
words = []
unique = []
for i in lines:
	words.append(i)
for j in words:
	if j not in unique:
		unique.append(j)
count = 0
for k in unique:
	count+=1
print('the number of unique words are',count)