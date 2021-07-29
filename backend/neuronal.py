from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection         import train_test_split
from sklearn.svm                     import LinearSVC
from sklearn.metrics                 import accuracy_score
import csv
import pandas as pd
import numpy as np
import string

def Neuronal(key):
    def readCv():
        spam_or_ham = pd.read_csv("data.csv", encoding='uft-8')[["v1", "v2"]]
        spam_or_ham.columns = ["label", "text"]
        spam_or_ham.head()
        spam_or_ham["label"].value_counts()

    def tokenize(sentence):
        tokens = []
        for token in sentence.split():
            new_token = []
            for character in token:
                if character not in punctuation:
                    new_token.append(character.lower())
            if new_token:
                tokens.append(" ".join(new_token))
        return tokens

        spam_or_ham.head()["text"].apply(tokenize)

    def Predic(test_X, test_labels):
        predicciones = classifier.predict(test_X)
        accuracy = accuracy_score(test_labels, predicciones)
        print(f"Accuracy: {accuracy:.4%}")

        frases = [
        'Hi Wordl',
        'Programing',
        'C++',
        'C#'
        ]
        frases_X = real_vectorizer.transform(frases)
        predicciones = classifier.predict(frases_X)

        frases_X = real_vectorizer.transform(frases)
        predicciones = classifier.predict(frases_X)

    readCv()
    Predic()
    tokenize()