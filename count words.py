file = open("F:/education/7thsem/ED/sept 11/Ram.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))
