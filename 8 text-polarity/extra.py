# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:20:12 2019

@author: Turing
"""

import nltk
from bs4 import BeautifulSoup
import utils
from _pickle import load
from nltk.stem.snowball import SpanishStemmer
ss = SpanishStemmer()

f = open('..\\corpus\\Excelsior_1999\\e990112.htm','r')
t = f.read()
text = t.lower()
f.close()

lista_articulos = text.split("<h3>")
lista_articulos_tokens = []

for articulo in lista_articulos:
    soup = BeautifulSoup(articulo, 'lxml')
    articulo_texto = soup.get_text()
    articulo_texto = articulo_texto.lower()
    articulo_tokenizado = utils.normalize_text(articulo_texto)
    lista_articulos_tokens.append(articulo_tokenizado)

for articulo in lista_articulos_tokens:
    print()
    print(' '.join(articulo))
    
pol_dict = {}
inputt = open('diccionario_polaridades_senticon.pkl','rb')
pol_dict = load(inputt)
inputt.close()

def lemmatize_sent(sent):
    return utils.lemmatize_text(utils.remove_unalphabetic_words(nltk.word_tokenize(sent)))

print('article','\t\t','polarity')
for aspect_i in range(len(lista_articulos_tokens)):
    aspect_value = 0
    finded_words = 0
    for word in lista_articulos_tokens[aspect_i]:
        if pol_dict.get(ss.stem(word)):
            finded_words += 1
            aspect_value += pol_dict[ss.stem(word)]
    if finded_words > 0:
        aspect_value = aspect_value / finded_words
        print(aspect_i, '\t',aspect_value)
    else:
        print(aspect_i, 0, 0)

