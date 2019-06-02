# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:27:02 2019

@author: Turing
"""
import utils

from bs4 import BeautifulSoup as Soup
from _pickle import dump

ruta_archivos = "..\\corpus\\corpusCine\\corpusCriticasCine"
resenhas_por_rank = {1:[],2:[],3:[],4:[],5:[]}
errs = 0
for xml_file_name in utils.find_all_files_in_path('*.xml',ruta_archivos):
    try:
        handler = open(xml_file_name).read()
        soup = Soup(handler,'lxml')
        review = soup.find('review')
        review_rank = int(review.attrs['rank'])
        review_body = review.get_text()
        review_body = utils.normalize_text(review_body)
        resenhas_por_rank[review_rank].append(review_body))
    except:
        errs += 1
print(resenhas_por_rank[5])
output = open("resenhas_por_polaridad_dict.pk1","wb")
dump(resenhas_por_rank, output, -1)
output.close()