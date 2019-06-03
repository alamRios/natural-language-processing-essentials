# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:58:15 2019

@author: Turing
"""
import utils
import nltk
from _pickle import load
from nltk.probability import FreqDist
from bs4 import BeautifulSoup as Soup

ruta_archivos = "..\\corpus\\corpusCine\\corpusCriticasCine"
sustantivos = []
inputt = open('UnigramTagger_cess_esp.pkl','rb')
unigram_tagger = load(inputt)
inputt.close()
errs = 0

for xml_file_name in utils.find_all_files_in_path('*.xml',ruta_archivos):
    try:
        handler = open(xml_file_name).read()
        soup = Soup(handler,'lxml')
        review = soup.find('review')
        review_body = review.get_text()
        palabras_etiquetas = []
        for oracion in nltk.sent_tokenize(review_body):
            palabras_etiquetas += unigram_tagger.tag(nltk.word_tokenize(oracion))
        sustantivos_archivo = [sustantivo for sustantivo,tag in palabras_etiquetas
                           if tag.startswith('n')]
        sustantivos += sustantivos_archivo
    except:
        errs += 1
        
#print(sustantivos)
fd = FreqDist(sustantivos)
print([word for word,freq in fd.most_common(20)])