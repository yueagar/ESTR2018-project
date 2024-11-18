# Developers: Yue Ka Leung, Tang Yu Hin
# This script is used to demonstrate Google Word2Vec's Skip-Gram model of Word2Vec using Gensim library.

# Importing the required libraries
import gensim
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load Google's pre-trained Word2Vec model.
# Google Word2Vec: https://code.google.com/archive/p/word2vec
# Model download link: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM
# You have to modify modelPath to the path of the downloaded model.
modelPath = "C:/Users/kelvi/Downloads/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(modelPath, binary=True)

# Get the vector of the word computer and print it
vec_computer = model["computer"]
#Uncomment the following lines to see the vector of the word computer. It is pretty long and hinders reading other logs.
#print("Vector of the word \"computer\": ")
#print(vec_computer)

# Get the most similar words to the word computer and print them
similar_computer = model.most_similar("computer")
print("Most similar words to the word \"computer\": ")
for word, similarity in similar_computer:
    print(word, similarity)

# Get the similarity between the words computer and phone and print it
similarity_computer_phone = model.similarity("computer", "phone")
print("Similarity between the words \"computer\" and \"phone\": ")
print(similarity_computer_phone)

# x1 is to x2 as y1 is to ?
def analogy(x1, x2, y1):
    result = model.most_similar(positive=[y1, x2], negative=[x1])
    return result[0][0]

# Get the analogy
print("Man is to king as woman is to", analogy("man", "king", "woman")) # queen

# Plot the word vectors using PCA
# Reference: https://www.kaggle.com/code/chmasgun/word2vec-and-visualization-with-pca
def plot_word_vectors(words):
    word_vectors = [model[word] for word in words]
    pca = PCA(n_components=2)
    result = pca.fit_transform(word_vectors)
    plt.scatter(result[:, 0], result[:, 1])
    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))
    plt.show()

# Plot the word vectors of the electronic devices using PCA
plot_word_vectors(["computer", "phone", "keyboard", "mouse", "monitor", "printer", "laptop", "tablet", "smartphone"])

# Plot the word vectors of some random words using PCA
plot_word_vectors(["great", "cool", "brilliant", "wonderful", "well", "amazing", "worth", "sweet", "enjoyable", "boring", "excellent", "good", "bad", "dumb", "annoying", "female", "male", "queen", "king", "man", "woman", "rain", "snow", "hail", "coffee", "tea"])