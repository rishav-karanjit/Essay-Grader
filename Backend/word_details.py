import nltk, re
class WordDetails():    
    def Get_No_of_char(self):
        file = open("Backend/essay.txt", "r")
        data = file.read().replace(" ","")
        number_of_characters = len(data)
        return(str(number_of_characters))

    def Get_No_of_words(self):
        file = open("Backend/essay.txt", "r")
        data = file.read()
        words = data.split()
        return(str(len(words)))

    def Get_No_of_unique_words(self):
        file = open("Backend/essay.txt", "r")
        lines = file.read()
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
        return(str(count))

    def GetMostCommonWords(self):
        file = open("Backend/essay.txt", "r")
        data = file.read()
        data = re.sub(r'[^\w\s]', '', data) 
        data_tokens = nltk.word_tokenize(data)

        stop_words = set(nltk.corpus.stopwords.words('english'))  
        filtered_sentence = [w for w in data_tokens if not w in stop_words]        
        filtered_sentence = []  
        for w in data_tokens:  
            if w not in stop_words:  
                filtered_sentence.append(w)  
        freq = nltk.FreqDist(filtered_sentence)
        word = ""
        for i in freq.most_common(5):
            word += i[0]
            word += "\n"
        return(word)
    def Get_No_of_para(self):
        file = open("Backend/essay.txt", "r")
        corpusReader = nltk.corpus.reader.plaintext.PlaintextCorpusReader("Backend", "essay.txt")
        return(str(len(corpusReader.paras())))

# Word = WordDetails()
# print(Word.Get_No_of_char())
# print(Word.Get_No_of_words())
# print(Word.Get_No_of_unique_words())
# print(Word.GetMostCommonWords())
