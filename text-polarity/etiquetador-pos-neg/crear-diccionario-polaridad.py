# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:07:59 2019

@author: Turing
"""

from _pickle import dump

diccionario_polaridad = {}
handler = open('fullStrengthLexicon.txt',encoding="utf-8")
for linea in handler.readlines():
    linea = linea.strip().split('\t')
    palabra = linea[0]
    polaridad = linea[-1]
    diccionario_polaridad[palabra] = polaridad
handler.close()

handler = open('mediumStrengthLexicon.txt',encoding="utf-8")
for linea in handler.readlines():
    linea = linea.strip().split('\t')
    palabra = linea[0]
    polaridad = linea[-1]
    diccionario_polaridad[palabra] = polaridad
handler.close()

output = open("diccionario_polaridades.pk1","wb")
dump(diccionario_polaridad, output, -1)
output.close()