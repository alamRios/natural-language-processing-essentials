# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:15:26 2019

@author: Turing
"""
from _pickle import load
from nltk import word_tokenize
import os, fnmatch
#from nltk.stem.snowball import SpanishStemmer

lemmas = {}
inputt = open('lemma_dict.pk1','rb')
lemmas = load(inputt)
inputt.close()

stopwords = []
inputt = open('stopwords_list.pk1','rb')
stopwords = load(inputt)
inputt.close()

def normalize_text(string_text):
    tokenized_text = word_tokenize_text(string_text)
    tokenized_text = lemmatize_text(tokenized_text)
    tokenized_text = remove_stopwords(tokenized_text)
    tokenized_text = remove_unalphabetic_words(tokenized_text)
    return tokenized_text

def lemmatize_text(tokenized_text):
    global lemmas
    for tok_i in range(len(tokenized_text)):
        if lemmas.get(tokenized_text[tok_i]):
            tokenized_text[tok_i] = lemmas[tokenized_text[tok_i]]
    return tokenized_text

def word_tokenize_text(string_text):
    return word_tokenize(string_text)

def remove_stopwords(tokenized_text):
    global stopwords
    return [tok for tok in tokenized_text if tok not in stopwords]

def remove_unalphabetic_words(tokenized_text):
    clean_text = []
    for word in tokenized_text:
        word = word.lower()
        clean_word = []
        for char in word:
            if char.isalpha():
                if char in ['ñ','á','é','í','ó','ú']:
                    if char == 'ñ':
                        char = 'n'
                    elif char == 'á':
                        char = 'a'
                    elif char == 'é':
                        char = 'e'
                    elif char == 'í':
                        char = 'i'
                    elif char == 'ó':
                        char = 'o'
                    elif char == 'ú':
                        char = 'u'
                clean_word.append(char)
        if len(clean_word) > 0:
            clean_text.append(''.join(clean_word))
    return clean_text

def find_all_files_in_path(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
