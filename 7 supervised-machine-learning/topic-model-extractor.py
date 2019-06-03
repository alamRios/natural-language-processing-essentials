# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:58:15 2019

@author: Turing

    lda gensim
"""
import utils
from _pickle import load
from bs4 import BeautifulSoup as Soup
import gensim
import gensim.corpora as corpora

ruta_archivos = "..\\corpus\\corpusCine\\corpusCriticasCine"
sustantivos = []
inputt = open('UnigramTagger_cess_esp.pkl','rb')
unigram_tagger = load(inputt)
inputt.close()
errs = 0

data_lemmatized = []
for xml_file_name in utils.find_all_files_in_path('*.xml',ruta_archivos):
    try:
        handler = open(xml_file_name).read()
        soup = Soup(handler,'lxml')
        review = soup.find('review')
        data_lemmatized.append(utils.normalize_text(review.get_text()))
    except:
        errs += 1

id2word = corpora.Dictionary(data_lemmatized)
corpus = [id2word.doc2bow(text) for text in data_lemmatized]

    # Build LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=8, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)
        
print(lda_model.print_topics())