from nltk.stem import PorterStemmer
import nltk.classify.util
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

sentenceList = []
sentenceListEn = []

"""
Allowed POS Tagging
"""
allowedPOS=['J','V','R','N']


"""
    Porter Stemmer
"""
def word_stemming(word):
     return ps.stem(word)


"""
    Function for Punctuation Removal
"""
def punctuation_remove(word):
    punctuations = '''!()-[]{};:'"\,<>./?@#+=$%^&*_~'''
    # remove punctuation from the string
    no_punct = ""
    for char in word:
        if char not in punctuations and not char.isdigit():
            no_punct = no_punct + char
    return no_punct


"""
    Preprocessing omn Input Sentence 
"""

def wordtokenize(inputSentenceList, outSentenceList):
    
    for inptemp in queryList:
        inp = []
        inp = inptemp.split()
        itemListNew = []
        item = []
        itemList = ''
        """POS Tagging"""
        posTagged= nltk.pos_tag(inp)
        for word in posTagged:
            if word[1][0] in allowedPOS:
                item.append(word[0].lower())
        for word in item:
            ## Call to punctuation removal ##
            word = punctuation_remove(word)
            if word != '' and word.lower() not in stops:
                wordNew  = word_stemming(word)                
                itemListNew.append(wordNew.lower())
        itemList = ' '.join(itemListNew)
        queryListEnh.append(itemList)
    


"""
Building feature matrix
"""
def feature_matrix(documents, feature_type='frequency'):

    feature_type = feature_type.lower().strip()  

    elif feature_type == 'frequency':
        vectorizer = CountVectorizer(binary=False, min_df=1, 
                                     ngram_range=(1, 1))
    elif feature_type == 'tfidf':
        vectorizer = TfidfVectorizer(min_df=1, 
                                     ngram_range=(1, 1))
    feature_matrix = vectorizer.fit_transform(documents).astype(float)
    
    return vectorizer, feature_matrix

"""
 Reading StopWords 
"""
with open('stopwords.txt', 'r') as stopFile:
    stops = stopFile.read().split('\n')
        
ps = PorterStemmer() 


"""
    Converting Input in Sentence Vector
"""
with open('001.txt', 'r') as inpFile:
    FIleInp = inpFile.read().split('\n')
    for item in FIleInp:
        if item != "":
            sentenceList.append(item)
        
wordtokenize(sentenceList, sentenceListEn)
#a, b = build_feature_matrix(sentenceListEn, 'frequency')