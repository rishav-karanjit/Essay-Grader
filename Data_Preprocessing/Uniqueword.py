class Unique_words():
    def Get_UniqueWords(self,lines):
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