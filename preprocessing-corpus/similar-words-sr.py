from _pickle import load
import numpy as np
import functools 

palabra_buscar = "priísta"

inputt = open('rfv-dict.pkl','rb')
rfv = load(inputt)
inputt.close()

inputt = open('contexts-dict.pkl','rb')
contexts = load(inputt)
inputt.close()

total_docs_n = len(rfv[palabra_buscar])
docs_number_for_word = []
vocabulary = contexts[palabra_buscar]

for word in vocabulary:
    docs_number = 0
    for context in contexts:
        if word in context:
            docs_number += 1
    docs_number_for_word.append(docs_number)

n = np.array(docs_number_for_word)
idf_vector = np.log((total_docs_n+1)/n)

bm25_vectors = []
bm25t = 0
k = 1.2
for context in contexts.keys():
	words = contexts[context]
	vector = []
	for voc in vocabulary:
		vector.append(words.count(voc))
	counts = np.array(vector)
	x = counts*(k+1)
	y = counts+k
	bm25 = np.divide(x,y)
	bm25_vector = np.multiply(bm25, idf_vector)
	bm25_vectors.append([context,functools.reduce(lambda x,y: x+y, bm25_vector)])
	if context == palabra_buscar: 
		bm25t = functools.reduce(lambda x,y: x+y, bm25_vector)

for i in range(len(bm25_vectors)): 
	bm25_vectors[i][1] = bm25_vectors[i][1] / bm25t

bm25_vectors.sort(key=lambda tup: tup[1], reverse=True)
file = open("similar-words-tests\\sr-similar-to-"+palabra_buscar+".txt","w",encoding="utf-8")

for tp in bm25_vectors:
    file.write(tp[0]+" "+str(tp[1])+"\n")

file.close()

