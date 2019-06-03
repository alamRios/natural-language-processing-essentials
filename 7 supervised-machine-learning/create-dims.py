import utils

from bs4 import BeautifulSoup as Soup
from _pickle import dump
import numpy as np

ruta_archivos = "..\\corpus\\corpusCine\\corpusCriticasCine"

y = []
reviews_content = []
errs = 0

for xml_file_name in utils.find_all_files_in_path('*.xml',ruta_archivos):
    try:
        handler = open(xml_file_name).read()
        soup = Soup(handler)
        review = soup.find('review')
        review_rank = int(review.attrs['rank']) - 1
        review_body = review.get_text()
        review_body = utils.normalize_text(review_body)
        y.append(review_rank)
        reviews_content.append(' '.join(review_body))
    except:
        errs += 1
        
print('>>> reviews done',errs,'errors.')

y = np.array(y)

output = open("dim-y_list.pk1","wb")
dump(y, output, -1)
output.close()

output = open("dim-x_list.pk1","wb")
dump(reviews_content, output, -1)
output.close()