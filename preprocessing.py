import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import string

try:
    stopwords = set(nltk.corpus.stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stopwords = set(nltk.corpus.stopwords.words("english"))


LOWERCASE = "Lowercase"
NUMBER_REMOVAL = "Number removal"
PUNCTUATION_REMOVAL = "Punctuation removal"
TOKENIZATION = "Tokenization"
STOPWORD_REMOVAL = "Stopword removal"
STEMMING = "Stemming"


def lowercase(text: str or list) -> str or list:
    if type(text) == str:
        return text.lower()
    elif type(text) == list:
        return [s.lower() for s in text]


def number_removal(text: str or list) -> str or list:
    if type(text) == str:
        temp = re.sub(r'\d+', '', text)
        return " ".join(temp.split())
    elif type(text) == list:
        temp = [re.sub(r'\d+', '', s) for s in text]
        temp = " ".join(temp).split()
        return temp


def punctuation_removal(text: str or list) -> str or list:
    if type(text) == str:
        return text.translate(str.maketrans('', '', string.punctuation))
    elif type(text) == list:
        return [s.translate(str.maketrans('', '', string.punctuation)) for s in text]


def tokenization(text: str or list) -> list:
    if type(text) == str:
        return text.split()
    elif type(text) == list:
        return text


def stopword_removal(text: str or list) -> str or list:
    stopwords = set(nltk.corpus.stopwords.words("english"))
    if type(text) == str:
        return " ".join([word for word in text.split() if word not in stopwords])
    elif type(text) == list:
        return [word for word in text if word not in stopwords]


def stemming(text: str or list) -> str or list:
    stemmer = PorterStemmer()
    if type(text) == str:
        temp = [stemmer.stem(word) for word in word_tokenize(text)]
        if temp[-1] == ".":
            result = ""
            for i in range(len(temp)):
                result += temp[i]
                if i < len(temp)-1 and temp[i+1] != ".":
                    result += " "
            return result
        return temp
    elif type(text) == list:
        return [stemmer.stem(s) for s in text]


def preprocess(options: list, text: str) -> str or list:
    for process in options:
        if process == LOWERCASE:
            text = lowercase(text)
        if process == PUNCTUATION_REMOVAL:
            text = punctuation_removal(text)
        if process == NUMBER_REMOVAL:
            text = number_removal(text)
        if process == TOKENIZATION:
            text = tokenization(text)
        if process == STOPWORD_REMOVAL:
            text = stopword_removal(text)
        if process == STEMMING:
            text = stemming(text)
    return text


print(lowercase(["Hello World!", "Hello World!"]))
