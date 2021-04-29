import pandas as pd

from Character import Characters
from Word import Words
#from Paragraph import Paragraph
from Uniqueword import Unique_words

df = pd.read_csv("../Dataset/Dataset.csv")

Characters = Characters()
Words = Words()
#Paragraph = Paragraph()
Unique_words = Unique_words()
for i in range(len(df)) :
	df.loc[i, "No. of Characters"] = Characters.Get_No_of_char(df.loc[i,"essay"])
	df.loc[i,"No. of Words"] = Words.Get_words(df.loc[i,"essay"])
	df.loc[i,"No. of Paragraphs"] = 1
	df.loc[i,"No. of Unique words"] = Unique_words.Get_UniqueWords(df.loc[i,"essay"])
df.to_csv("../Dataset/Dataset.csv")
#print(df)