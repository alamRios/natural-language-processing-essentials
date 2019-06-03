# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:21:22 2019

@author: Turing
"""

import localutils
import nltk

from utils import build_feature_matrix, low_rank_svd
import numpy as np

def lsa_text_summarizer(documents, num_sentences=2,
                        num_topics=2, feature_type='frequency',
                        sv_threshold=0.5):
                            
    vec, dt_matrix = build_feature_matrix(documents, 
                                          feature_type=feature_type)

    td_matrix = dt_matrix.transpose()
    td_matrix = td_matrix.multiply(td_matrix > 0)

    u, s, vt = low_rank_svd(td_matrix, singular_count=num_topics)  
    min_sigma_value = max(s) * sv_threshold
    s[s < min_sigma_value] = 0
    
    salience_scores = np.sqrt(np.dot(np.square(s), np.square(vt)))
    top_sentence_indices = salience_scores.argsort()[-num_sentences:][::-1]
    top_sentence_indices.sort()
    
    for index in top_sentence_indices:
        print(documents[index])


aspects = ['manos libres','bateria','pantalla','precio','color','camara','radio']
#aspects = ['bateria','pantalla','foto','calidad','tiempo']
files_path = "..\\corpus\\SFU_Spanish_Review_Corpus\\moviles"

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
    lsa_text_summarizer(aspect_sents, num_sentences=1,
                    num_topics=5, feature_type='frequency',
                    sv_threshold=0.5)  
