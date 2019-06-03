# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:54:55 2019

@author: Turing

>> PARTE 1
    Quitar acentos para este caso ñ->n al quitar signos
    Hay que juntar los full y medium
    Considerar como etiqueta valida la segunda

    1. Para cada resenha hay que calcular polaridad 
        - democracia (mas pos o mas neg)
    2. Promedio por categoria
        - democracia
        
    Para cada categoria, numero de etiquetas positivas y numero de negativas

"""

from _pickle import load

diccionario_polaridad = {}
inputt = open('diccionario_polaridades.pk1','rb')
diccionario_polaridad = load(inputt)
inputt.close()

resenhas_categoria = {}
inputt = open('resenhas_por_categoria_dict.pk1','rb')
resenhas_categoria = load(inputt)
inputt.close()

palabras_no_encontradas = 0
total_palabras_encontradas = 0

categoria_polaridad = []

for categoria in resenhas_categoria:
    cuenta_pos = 0
    cuenta_neg = 0
    palabras_encontradas = 0
    for resenha in resenhas_categoria[categoria]:
        for word in resenha[0].split():
            if diccionario_polaridad.get(word):
                palabras_encontradas += 1
                if diccionario_polaridad[word] == 'pos':
                    cuenta_pos += 1
                else:
                    cuenta_neg += 1
            else:
                palabras_no_encontradas += 1
                
    total_palabras_encontradas += palabras_encontradas
    categoria_polaridad.append((str(categoria), 
                                str(int(cuenta_pos / len(resenhas_categoria[categoria]))), 
                                str(int(cuenta_neg / len(resenhas_categoria[categoria])))))
print()
print('cat\tpos\tneg')
print()
for cp in categoria_polaridad: 
    print('\t'.join(cp))
print()
#print('>>>',total_palabras_encontradas,' palabras encontradas.')
#print('>>>',palabras_no_encontradas,' palabras no encontradas.')