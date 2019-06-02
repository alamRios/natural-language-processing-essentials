# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:07:59 2019

@author: Turing
"""

from bs4 import BeautifulSoup as Soup
from _pickle import dump
from nltk.stem.snowball import SpanishStemmer

handler = open('senticon.es.xml',encoding="utf-8").read()
soup = Soup(handler,'lxml')
diccionario_polaridad = {}
ss = SpanishStemmer()
for lemma in soup.find_all('lemma'):
    palabra = lemma.get_text()
    polaridad = float(lemma.attrs["pol"])
    diccionario_polaridad[ss.stem(palabra.replace(' ','')).lower()] = polaridad

output = open("diccionario_polaridades.pk1","wb")
dump(diccionario_polaridad, output, -1)
output.close()