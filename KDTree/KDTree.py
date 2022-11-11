import scipy as sp
from scipy import spatial
import sklearn as sl
from sklearn import neighbors
import numpy as np
import pandas as pd
import fasttext

data_frame = pd.read_pickle('D:/saveeeee/tenderhack/common/samples/СТЕ_vectorized.pickle')
df = pd.read_pickle('D:/saveeeee/tenderhack/common/samples/СТЕ_База.pickle')
data_array = data_frame['Название СТЕ'].to_numpy()
arr = np.vstack(data_array)
tree = spatial.KDTree(arr)

model = fasttext.load_model('ft_native_300_ru_wiki_lenta_lemmatize.bin')


def find(text: str):
    final = (model.get_sentence_vector(text))
    return df['Название СТЕ'][tree.query(final, 10)[1]]