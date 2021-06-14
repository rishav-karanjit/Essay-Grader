import nltk, re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import pandas as pd

class WordDetails():    
	def Get_No_of_char(self):
		df = pd.read_csv("Backend/essay.csv")

		file = open("Backend/essay.txt", "r")
		data = file.read().replace(" ","")
		number_of_characters = len(data)

		df.loc[0,"Number of Char"] = number_of_characters
		df.to_csv("Backend/essay.csv",index=False)

		return(str(number_of_characters))

	def Get_No_of_words(self):
		df = pd.read_csv("Backend/essay.csv")

		file = open("Backend/essay.txt", "r")
		data = file.read()
		words = data.split()

		df.loc[0,"No. of words"] = len(words)
		df.to_csv("Backend/essay.csv",index=False)

		return(str(len(words)))

	def Get_No_of_unique_words(self):
		df = pd.read_csv("Backend/essay.csv")

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

		df.loc[0,"No. of unique"] = count
		df.to_csv("Backend/essay.csv",index=False)

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

    # Tokenize a sentence into words

	def sentence_to_wordlist(self,raw_sentence):
        
		clean_sentence = re.sub("[^a-zA-Z0-9]"," ", raw_sentence)
		tokens = nltk.word_tokenize(clean_sentence)

		return tokens

	def tokenize(self,essay):
		stripped_essay = essay.strip()

		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
		raw_sentences = tokenizer.tokenize(stripped_essay)

		tokenized_sentences = []
		for raw_sentence in raw_sentences:
			if len(raw_sentence) > 0:
				tokenized_sentences.append(self.sentence_to_wordlist(raw_sentence))

		return tokenized_sentences
	def Part_of_speech(self):
		df = pd.read_csv("Backend/essay.csv")


		file = open("Backend/essay.txt", "r")
		essay = file.read()
		tokenized_sentences = self.tokenize(essay)

		noun_count = 0
		adj_count = 0
		verb_count = 0
		adv_count = 0

		for sentence in tokenized_sentences:
			tagged_tokens = nltk.pos_tag(sentence)

			for token_tuple in tagged_tokens:
				pos_tag = token_tuple[1]

				if pos_tag.startswith('N'): 
					noun_count += 1
				elif pos_tag.startswith('J'):
					adj_count += 1
				elif pos_tag.startswith('V'):
					verb_count += 1
				elif pos_tag.startswith('R'):
					adv_count += 1

		df.loc[0,"POS"] = (noun_count+adj_count+verb_count+adv_count)
		df.to_csv("Backend/essay.csv",index=False)

		return noun_count, adj_count, verb_count, adv_count
        
# Word = WordDetails()
# print(Word.Get_No_of_char())
# print(Word.Get_No_of_words())
# print(Word.Get_No_of_unique_words())
# print(Word.GetMostCommonWords())
# print(Word.Get_No_of_Noun())
