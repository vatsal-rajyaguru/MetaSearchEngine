import os
import re
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk import sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup


training_path = 'C:/Users/vatsal/Desktop/4305_datasets/train/course'
test_set = 'C:/Users/vatsal/Desktop/4305_datasets/test'


ready_text = []
stop_words = set(stopwords.words('english'))
stop_words_list = list(stop_words)


def remove_stopwords(raw_text):
    if str(stop_words_list) in raw_text:
        raw_text.replace(stop_words_list, '')
    return raw_text


def perform_lemmatization(raw_text):
    raw_text = str(raw_text)
    lemmatizer = WordNetLemmatizer()
    lemmatizer.lemmatize(raw_text)
    return raw_text


for filename in os.listdir(training_path):
    with open(os.path.join(training_path, filename), 'r') as f:
        raw_data = f.read()
        soup = BeautifulSoup(raw_data, 'html.parser')
        html_text = soup.get_text()

        # formatting text to lowercase
        lower_text = html_text.lower()

        # remove special characters
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', lower_text)

        # calling stop word remover function
        nonstop_text = remove_stopwords(cleaned_text)

        rich_text = nonstop_text.replace('\n', ' ')

        # calling the lemmatizer function
        lemm_text = perform_lemmatization(rich_text)

        # tokenizing the words
        tokenized_text = sent_tokenize(lemm_text)

        ready_text.append(lemm_text)
        # print(tokenized_text)


