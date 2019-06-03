import nltk
from bs4 import BeautifulSoup
from nltk import FreqDist
from _pickle import dump
import utils

file_path = '..\\corpus\\Excelsior_1999\\e990112.htm'
print("Reading file...",file_path)
f = open(file_path,'r')
t = f.read()
f.close()

print("Normalize text...")
soup = BeautifulSoup(t, 'lxml')
text = soup.get_text()
tokens = utils.normalize_text(text, remove_acents=False)

print(' '.join(tokens))

window_s = 8
contexts = {}

print("Generating contexts...")
fd = FreqDist(tokens)
vocabulary = fd.keys()
for w in vocabulary:
    context = []
    for i in range(len(tokens)):
        if tokens[i] == w:
            for j in range (i - int(window_s/2), i):
                if j >= 0:
                    context.append(tokens[j])
            try:
                for j in range(i+1, i+int(window_s/2)):
                    context.append(tokens[j])
            except IndexError:
                pass
    contexts[w] = context
    
output = open('contexts-dict.pkl','wb')
dump(contexts, output, -1)
output.close()
print("Generating raw frequency vector...")
rfv = {}
for w in vocabulary:
    row = []
    for vv in vocabulary:
        if vv in contexts[w]:
            row.append(contexts[w].count(vv))
        else:
            row.append(0)
    rfv[w] = row
    
output = open('rfv-dict.pkl','wb')
dump(rfv, output, -1)
output.close()