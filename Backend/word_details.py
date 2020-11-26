import nltk
class WordDetails():    
    def Get_No_of_char(self):
        file = open("essay.txt", "r")
        data = file.read().replace(" ","")
        number_of_characters = len(data)
        return(number_of_characters)

    def Get_No_of_words(self):
        file = open("essay.txt", "r")
        data = file.read()
        words = data.split()
        return(len(words))

    def Get_No_of_unique_words(self):
        file = open("essay.txt", "r")
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
        return(count)

    def GetMostCommonWords(self):
        file = open("essay.txt", "r")
        data = file.read().replace('\n', ' ')

        data = data.split(' ')
        data = [x for x in data if x != '']
        fdist1 = nltk.FreqDist(data)
        a=[]
        for i in fdist1.most_common(5):
            a+=[i[0]]

        return a

Word = WordDetails()
print(Word.Get_No_of_char())
print(Word.Get_No_of_words())
print(Word.Get_No_of_unique_words())
print(Word.GetMostCommonWords())
