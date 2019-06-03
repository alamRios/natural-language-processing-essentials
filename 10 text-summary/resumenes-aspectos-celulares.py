# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:21:22 2019

@author: Turing
"""

import localutils
import nltk

from gensim.summarization import summarize

def text_summarization_gensim(text, summary_ratio=0.5):
    summary = summarize(text, split=True, ratio=summary_ratio)
    for sentence in summary:
        print()
        print(sentence)


aspects = ['servicio técnico','ropa','precio','marca','lavado']
#aspects = ['bateria','pantalla','foto','calidad','tiempo']
files_path = "..\\corpus\\SFU_Spanish_Review_Corpus\\lavadoras"

def lemmatize_sent(sent):
    return localutils.lemmatize_text(localutils.remove_unalphabetic_words(localutils.remove_stopwords(nltk.word_tokenize(sent))))

sents = []
for file_name in localutils.find_all_files_in_path('*.txt',files_path):
    oracion = open(file_name).read()
    oracion = oracion.replace('\n\n.','. ').replace('\n.','. ')
    oracion = oracion.replace('..','. ')
    
    sents += nltk.sent_tokenize(oracion)

for aspect in aspects:
    aspect_sents = []
    for sent in sents:
        lemmatized_sent = lemmatize_sent(sent)
        if (aspect in sent) or (aspect in lemmatized_sent):
            aspect_sents.append(sent)
    text_aspect_sents = ' '.join(aspect_sents)
    print()
    print('<<<<<<<<<<<<<<<',aspect,'>>>>>>>>>>>>>>>>>')
    text_summarization_gensim(text_aspect_sents, 0.05)  
