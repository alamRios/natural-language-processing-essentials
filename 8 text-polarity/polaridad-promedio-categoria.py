# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:27:02 2019

@author: Turing
"""
from _pickle import load
from nltk.stem.snowball import SpanishStemmer

diccionario_polaridad = {}
inputt = open('diccionario_polaridades.pk1','rb')
diccionario_polaridad = load(inputt)
inputt.close()

resenhas_categoria = {}
inputt = open('resenhas_por_categoria_dict.pk1','rb')
resenhas_categoria = load(inputt)
inputt.close()

categoria_polaridad = []

palabras_no_encontradas = 0
total_palabras_encontradas = 0
ss = SpanishStemmer()

for categoria in resenhas_categoria:
    valor_categoria = 0
    palabras_encontradas = 0
    for resenha in resenhas_categoria[categoria]:
        for word in resenha[0].split():
            if diccionario_polaridad.get(ss.stem(word).lower()):
                palabras_encontradas += 1
                valor_categoria += diccionario_polaridad[ss.stem(word).lower()]
            else:
                palabras_no_encontradas += 1
    
    total_palabras_encontradas += palabras_encontradas
    polaridad_promedio = valor_categoria / len(resenhas_categoria[categoria])
    categoria_polaridad.append((categoria, polaridad_promedio))
print()
for cp in categoria_polaridad: 
    print(cp)
print()
print('>>>',total_palabras_encontradas,' palabras encontradas.')
print('>>>',palabras_no_encontradas,' palabras no encontradas.')