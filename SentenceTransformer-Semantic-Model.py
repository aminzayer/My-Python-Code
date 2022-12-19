import torch,nltk
import numpy as np
from hazm import *
from sentence_transformers import SentenceTransformer,util
import warnings
warnings.filterwarnings('ignore')

class Semantic:

    def __init__(self):
        self.model= SentenceTransformer('distiluse-base-multilingual-cased-v1')
    
    def CorpusEmbedding(self, corpus):
        if torch.cuda.is_available():
            embeddings = self.model.encode(corpus, device='cuda')  # CPU = cpu & GPU = cuda
        else:
            embeddings = self.model.encode(corpus, device='cpu')  # CPU = cpu & GPU = cuda
        return embeddings
    
    def SentenceEmbedding(self, sentence):
        if torch.cuda.is_available():
            embeddings = self.model.encode(sentence, device='cuda')  # CPU = cpu & GPU = cuda
        else:
            embeddings = self.model.encode(sentence, device='cpu')  # CPU = cpu & GPU = cuda
        return embeddings
    
    def English_Text_Convert_To_Sentences(self, text):
        # Download nltk dictionary punkt English Language
        nltk.download('punkt', quiet=True)  # Download nltk dictionary punkt English Language for first time
        nltk.download('averaged_perceptron_tagger', quiet=True)  # Download nltk dictionary averaged_perceptron_tagger for first time
        # Convert Text to Sentences
        sentences = nltk.text.sent_tokenize(text)
        return sentences

    def Farsi_Text_Convert_To_Sentences(self, text):
        normalizer = Normalizer()
        text = normalizer.normalize(text)
        return sent_tokenize(text)
    
    def Calculate_Semantic_Two_Sentences(self,sentence1,sentence2):
        SentEmbed1= self.SentenceEmbedding(sentence=sentence1)
        SentEmbed2= self.SentenceEmbedding(sentence=sentence2)
        return util.cos_sim(SentEmbed1, SentEmbed2).numpy()[0][0]

    def Calculate_Semantic_Two_Corpus(self,corpus1,corpus2):
        CorpusEmbed1 = self.SentenceEmbedding(sentence=corpus1)
        CorpusEmbed2 = self.SentenceEmbedding(sentence=corpus2)
        return util.cos_sim(CorpusEmbed1, CorpusEmbed2).numpy()[0][0]
    

Semantic_Model = Semantic()
emtiyaz = Semantic_Model.Calculate_Semantic_Two_Sentences(sentence1='من خوردن پیتزا را دوست دارم', sentence2='من شام خوردم')
print(emtiyaz)



    