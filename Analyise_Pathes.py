import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
# import tflearn as tf
import numpy as np
# File_pathes=input("Enter PATH")
def analyise_path(File_pathes):
    ls_pathes=[]
    with open(File_pathes,mode="r") as f:
        data=f.read()   
    sentences=sent_tokenize(data)
    tokenizer = RegexpTokenizer(r'\w+')
    words = [tokenizer.tokenize(sentence) for sentence in sentences]
    words = [[word.lower() for word in sentence] for sentence in words]
    stemmer = PorterStemmer()
    stemmed_words = [[stemmer.stem(word) for word in sentence] 
                    for sentence in words]
    array=np.array(stemmed_words)
    array_MD=array.reshape(array.shape[1],)
    dictionary={}
    sum=0
    for i in range(len(array_MD)):
        dictionary.setdefault(array_MD[i],[])
    for i in range(len(array_MD)):
        x=array_MD[i]
        for j in range(len(array_MD)-1):
            if array_MD[i]==array_MD[j+1]:
                sum=sum+1
        dictionary[x].append(sum)
        sum=0 
    dictionary2={}
    for i in range(len(array_MD)):
        dictionary2.setdefault(array_MD[i],list(set(dictionary[array_MD[i]])))
    return dictionary2
def Anlyise_Mltiable_Path(File_number):
    ls=[]
    for i in range(File_Number):
        path=input("Enter Path number")
        x=analyise_path(path)
        ls.append(x)
    for i in range(File_Number):
        print(ls[i])
File_Number=int(input("Enter File Number"))
Anlyise_Mltiable_Path(File_Number)


    
       

       



