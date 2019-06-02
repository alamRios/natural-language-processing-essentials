# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:58:15 2019

@author: Turing
"""
import utils
import nltk
from _pickle import load
from nltk.probability import FreqDist

ruta_archivos = "..\\corpus\\SFU_Spanish_Review_Corpus\\moviles"
sustantivos = []
inputt = open('UnigramTagger_cess_esp.pkl','rb')
unigram_tagger = load(inputt)
inputt.close()

for file_name in utils.find_all_files_in_path('*.txt',ruta_archivos):
    oraciones = nltk.sent_tokenize(open(file_name).read().replace('\n','.'))
    palabras_etiquetas = unigram_tagger.tag(nltk.word_tokenize(oraciones[-1]))
    sustantivos_archivo = [sustantivo for sustantivo,tag in palabras_etiquetas
                           if tag.startswith('n')]
    sustantivos_archivo = utils.remove_unalphabetic_words(utils.lemmatize_text(sustantivos_archivo))
    sustantivos += sustantivos_archivo
        
#print(sustantivos)
fd = FreqDist(sustantivos)
print([word for word,freq in fd.most_common(20)])