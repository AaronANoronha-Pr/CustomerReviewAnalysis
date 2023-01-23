import pandas as pd

dataset = pd.read_csv('https://www.amazon.in/product-reviews/B08FB2LNSZ/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8'
                      '&filterByStar=all_stars&reviewerType=all_reviews&pageNumber=', delimiter='\t', quoting=3)
dataset.shape
dataset.head()

import re
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

all_stopwords = stopwords.words('english')
all_stopwords.remove('not')

corpus = []

for i in range(0, 900):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)
