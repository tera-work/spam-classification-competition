import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

stop_words = stopwords.words('english')
stemmer = SnowballStemmer("english", True)

def remove_stopwords(text):
    return " ".join([re.sub('[^a-zA-Z]+', '', w) for w in text.split() if w not in stop_words])

def stemmed_words(text):
    words = word_tokenize(text)
    stemmed = [stemmer.stem(w) for w in words]
    return " ".join(stemmed)

def preprocess_text(df, text_col="text"):
    df[text_col] = df[text_col].str.lower()
    df["text_clean"] = df[text_col].apply(remove_stopwords).apply(stemmed_words)
    return df
