from nltk.stem import PorterStemmer
import nltk.classify.util
import glob
import os

sentenceList = []
sentenceListEn = []
fileList = []
wordslistDoc = []


path = 'BBC News Summary/News Articles/business/*'
files = glob.glob(path)


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

def wordtokenize(queryList, queryListEnh):
    
    for inp in queryList:
        itemListNew = []
        item = []
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
        queryListEnh.append(itemListNew)
    

"""
 Reading StopWords 
"""
with open('stopwords.txt', 'r') as stopFile:
    stops = stopFile.read().split('\n')
        
ps = PorterStemmer() 


"""
    Converting Input in Sentence Vector
"""
for paths in files:
    with open(os.path.join(os.path.dirname(__file__), paths)) as file:
        fileList.append(paths)
        strInp = ""
        text = file.read()
        #soup = BeautifulSoup(text, 'html.parser')
        #span = soup.findAll(['title','text'])
        #for th in span:
            #strInp += th.text
        wordslistDoc.append(text.split())
        
#with open('001.txt', 'r') as inpFile:
    #FIleInp = inpFile.read().split('\n')
    #for item in FIleInp:
        #if item != "":
            #sentenceList.append(item.split())
        
wordtokenize(wordslistDoc, sentenceListEn)