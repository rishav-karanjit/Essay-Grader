file = open("F:/education/7thsem/ED/sept 11/Ram.txt", "r")


data = file.read().replace(" ","")


number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)