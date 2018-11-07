import gensim

model = gensim.models.Word2Vec.load("word2vec.model")
print(model.wv.most_similar (positive='reliable', topn=30))

