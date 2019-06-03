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

aspects = ['manos libres','bateria','pantalla','precio','color','camara','radio']
#aspects = ['bateria','pantalla','foto','calidad','tiempo']
files_path = "..\\corpus\\SFU_Spanish_Review_Corpus\\moviles"
errs = 0

pol_dict = {}
inputt = open('diccionario_polaridades.pk1','rb')
pol_dict = load(inputt)
inputt.close()


def lemmatize_sent(sent):
    return utils.lemmatize_text(utils.remove_unalphabetic_words(nltk.word_tokenize(sent)))

sents = []
for file_name in utils.find_all_files_in_path('*.txt',files_path):
    sents += nltk.sent_tokenize(open(file_name).read().replace('\n\n','.').replace('\n','.'))

print('aspect','pos','neg')
for aspect in aspects:
    aspect_sent_avg_pos_count = 0
    aspect_sent_avg_neg_count = 0
    sents_of_aspect_count = 0
    for sent in sents:
        lemmatized_sent = lemmatize_sent(sent)
        if (aspect in sent) or (aspect in lemmatized_sent):
            sent_pos_count = 0
            sent_neg_count = 0
            sents_of_aspect_count += 1
            for word in lemmatized_sent:
                if pol_dict.get(word):
                    if pol_dict[word] == 'pos':
                        sent_pos_count += 1
                    else:
                        sent_neg_count += 1
            if sent_pos_count + sent_neg_count > 0:
                aspect_sent_avg_pos_count += sent_pos_count / (sent_pos_count + sent_neg_count)
                aspect_sent_avg_neg_count += sent_neg_count / (sent_pos_count + sent_neg_count)
    if sents_of_aspect_count > 0:
        aspect_sent_avg_pos_count = aspect_sent_avg_pos_count / sents_of_aspect_count
        aspect_sent_avg_neg_count = aspect_sent_avg_neg_count / sents_of_aspect_count
        print(aspect, aspect_sent_avg_pos_count, aspect_sent_avg_neg_count)
    else:
        print(aspect, 0, 0)




