# Developers: Yue Ka Leung, Tang Yu Hin
# This script is used to demonstrate Google Word2Vec's Skip-Gram model of Word2Vec using Gensim library.

# Importing the required libraries
import gensim

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