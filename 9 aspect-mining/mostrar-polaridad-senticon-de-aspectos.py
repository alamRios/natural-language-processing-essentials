# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:22:22 2019

@author: Turing
    aspectos:
        *manos libres
        bateria
        pantalla
        precio
        color
        camara
        radio
        
    Generar tabla de aspecto-polaridad
        aspecto porcentaje-pos porcentaje-neg
    Con ambos diccionarios de polaridad
    
"""
import nltk
import utils
from _pickle import load

from nltk.stem.snowball import SpanishStemmer
ss = SpanishStemmer()

aspects = ['manos libres','bateria','pantalla','precio','color','camara','radio']
#aspects = ['bateria','pantalla','foto','calidad','tiempo']
files_path = "..\\corpus\\SFU_Spanish_Review_Corpus\\moviles"
errs = 0

pol_dict = {}
inputt = open('diccionario_polaridades_senticon.pkl','rb')
pol_dict = load(inputt)
inputt.close()

def lemmatize_sent(sent):
    return utils.lemmatize_text(utils.remove_unalphabetic_words(nltk.word_tokenize(sent)))

sents = []
for file_name in utils.find_all_files_in_path('*.txt',files_path):
    sents += nltk.sent_tokenize(open(file_name).read().replace('\n\n','.').replace('\n','.'))

print('aspect','\t\t','polarity')
for aspect in aspects:
    aspect_sent_avg_val = 0
    sents_of_aspect_count = 0
    for sent in sents:
        lemmatized_sent = lemmatize_sent(sent)
        if (aspect in sent) or (aspect in lemmatized_sent):
            sent_value = 0
            sents_of_aspect_count += 1
            finded_words = 0
            for word in lemmatized_sent:
                if pol_dict.get(ss.stem(word)):
                    finded_words += 1
                    sent_value += pol_dict[ss.stem(word)]
            if finded_words > 0:
                aspect_sent_avg_val += sent_value #/ finded_words
    if sents_of_aspect_count > 0:
        aspect_sent_avg_val = aspect_sent_avg_val / sents_of_aspect_count
        print(aspect, '\t',aspect_sent_avg_val)
    else:
        print(aspect, 0, 0)




