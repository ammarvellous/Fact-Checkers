import pandas as pd
import numpy as np
import re
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

def tokenize_text(text):
    return nltk.word_tokenize(text)

def preprocess_data(dataframe):
    dataframe['cleaned_text'] = dataframe['text'].apply(clean_text)
    dataframe['tokens'] = dataframe['cleaned_text'].apply(tokenize_text)
    return dataframe

def split_data(dataframe, test_size=0.2, random_state=42):
    X = dataframe['cleaned_text']
    y = dataframe['label']
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def vectorize_data(X_train, X_test):
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    return X_train_vec, X_test_vec, vectorizer