# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:21:22 2019

@author: Turing
"""

import localutils
import nltk

from gensim.summarization import summarize
from normalization import normalize_corpus, parse_document
from utils import build_feature_matrix, low_rank_svd
import networkx
import numpy as np

def textrank_text_summarizer(documents, num_sentences=2,
                             feature_type='frequency'):
    
    vec, dt_matrix = build_feature_matrix(documents, 
                                      feature_type='tfidf')
    similarity_matrix = (dt_matrix * dt_matrix.T)
        
    similarity_graph = networkx.from_scipy_sparse_matrix(similarity_matrix)
    scores = networkx.pagerank(similarity_graph)   
    
    ranked_sentences = sorted(((score, index) 
                                for index, score 
                                in scores.items()), 
                              reverse=True)

    top_sentence_indices = [ranked_sentences[index][1] 
                            for index in range(num_sentences)]
    top_sentence_indices.sort()
    
    for index in top_sentence_indices:
        print(documents[index])


aspects = ['servicio técnico','ropa','precio','marca','lavado']
#aspects = ['bateria','pantalla','foto','calidad','tiempo']
files_path = "..\\corpus\\SFU_Spanish_Review_Corpus\\lavadoras"

def lemmatize_sent(sent):
    return localutils.lemmatize_text(localutils.remove_unalphabetic_words(localutils.remove_stopwords(nltk.word_tokenize(sent))))

sents = []
for file_name in localutils.find_all_files_in_path('*.txt',files_path):
    oracion = open(file_name).read()
    oracion = oracion.replace('\n\n.','. ').replace('\n.','. ')
    oracion = oracion.replace('..','. ').replace('·       ','. ')
    
    sents += nltk.sent_tokenize(oracion)

for aspect in aspects:
    aspect_sents = []
    for sent in sents:
        lemmatized_sent = lemmatize_sent(sent)
        if (aspect in sent) or (aspect in lemmatized_sent):
            aspect_sents.append(sent)
    print()
    print('<<<<<<<<<<<<<<<',aspect,'>>>>>>>>>>>>>>>>>')
    textrank_text_summarizer(aspect_sents, num_sentences=1,
                     feature_type='frequency')  
