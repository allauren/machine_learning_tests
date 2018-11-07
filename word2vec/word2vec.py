import gensim
import matplotlib.pyplot as plt

model = gensim.models.Word2Vec.load("word2vec.model")
print(model.wv.most_similar (positive='fun', topn=30))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

