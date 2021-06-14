import pandas as pd

from Character import Characters
from Mistake import gcheck
from Word import Words
from Part_of_speech import POS
#from Paragraph import Paragraph
from Uniqueword import Unique_words

df = pd.read_csv("../Dataset/Dataset2.csv")

grammer_check = gcheck()
Characters = Characters()
Words = Words()
#Paragraph = Paragraph()
Unique_words = Unique_words()
POS = POS()
for i in range(len(df)) :
	df.loc[i,"Grammer mistakes"] = grammer_check.check(df.loc[i,"essay"])
	print(df.loc[i,"Grammer mistakes"])
	df.loc[i, "No. of Characters"] = Characters.Get_No_of_char(df.loc[i,"essay"])
	df.loc[i,"No. of Words"] = Words.Get_words(df.loc[i,"essay"])
	df.loc[i,"No. of Paragraphs"] = 1
	df.loc[i,"No. of Unique words"] = Unique_words.Get_UniqueWords(df.loc[i,"essay"])
	df.loc[i, "No. of Noun"], df.loc[i, "No. of Adv"], df.loc[i, "No. of Verb"], df.loc[i, "No. of Adverb"] = POS.Part_of_speech(df.loc[i,"essay"])
df.to_csv("../Dataset/Dataset2.csv")
#print(df)