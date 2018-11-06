import gensim


model = gensim.load("word2vec.model")
model.wv.most_similar (positive='nice')

