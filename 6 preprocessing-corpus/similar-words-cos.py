# -*- coding: utf-8 -*-
from _pickle import load
import math

palabra_buscar = "presidente"

inputt = open('rfv-dict.pkl','rb')
rfv = load(inputt)
inputt.close()

def coseno_vectores(x,y):
    numerador = 0.0
    for i in range(len(x)):
        numerador += x[i] * y[i]
    deno = 0.0
    denominador = 0.0
    for xi in x:
        deno += xi**2
    deno = math.sqrt(deno)
    denominador = deno
    deno = 0.0
    for yi in y:
        deno += yi**2
    deno = math.sqrt(deno)
    denominador *= deno
    return numerador/denominador

file = open("similar-words-tests\\cos-similar-to-"+palabra_buscar+".txt","w",encoding="utf-8")
cosenos = []
vector_c = rfv[palabra_buscar]
for w in rfv.keys():
    cosenos.append((w,coseno_vectores(vector_c,rfv[w])))

cosenos.sort(key=lambda tup: tup[1], reverse=True)

for cos in cosenos:
    file.write(cos[0]+" "+str(cos[1])+"\n")

file.close()