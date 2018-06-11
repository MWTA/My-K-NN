#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Software: Dictionary
    Tutorial: <http://excript.com/python/funcoes-dicionarios.html>
    Data: 11/06/2018
    Athor: RodriguesFAS
    Email: franciscosouzaacer@gmail.com
"""

import re
import sys
import nltk
import numpy as np
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')

path_root = '/home/rodriguesfas/Workspace/My-K-NN/data/out/'
path_dataset_input = path_root + 'generated-polarity-data.csv'
path_stop_list = path_root + '../stopwords/stopwords.txt'


"""
    Debug Console
    Flag
        True 
        False
"""
TEST = True


def LOG(text):
    if TEST is True:
        print(text)


def remove_stopword_nltk(dataset):
    cachedStopWords = stopwords.words("english")
    dataset = ' '.join(
        [word for word in dataset.lower().split() if word not in cachedStopWords])
    return dataset.strip().strip()


def remove_stopword_list(dataset):
    stop_list = open(path_stop_list).read()
    words_filtered = dataset[:]
    words_filtered = [i for i in dataset.split() if not i in stop_list]
    return (" ".join(words_filtered)).strip()


def stemmer(dataset):
    stemmer = nltk.stem.RSLPStemmer()
    words = []
    for word in dataset.split():
        words.append(stemmer.stem(word))
    return (" ".join(words)).strip()


def remove_very_small_words(dataset):
    dataset = re.sub(r'\b\w{1,3}\b', '', dataset)
    return dataset.strip()


def load_dataset(path_dataset):
    LOG('Loading data..')
    with open(path_dataset) as documents:
        data = []
        index = 0
        for document in documents:
            temp = [document.split(",")[0], document.split(",")[1].strip()]
            data.append(temp)
            index += 1
        print data


def main():
    load_dataset(path_dataset_input)


if __name__ == '__main__':
    main()
