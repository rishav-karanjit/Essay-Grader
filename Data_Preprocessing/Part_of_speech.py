import nltk, re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class POS():
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
    def Part_of_speech(self,essay):
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
                
        return noun_count, adj_count, verb_count, adv_count