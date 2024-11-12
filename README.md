# ESTR2018 Course Project (Group YKL&TYH)

### What is this project?
This is a project for the [CUHK](https://cuhk.edu.hk) [ESTR2018/ENGG2760A course](https://www.cse.cuhk.edu.hk/wp-content/uploads/academics/ug/Courses/ENGG2760.pdf).
#### Topic
A peek into word embeddings using word2vec
#### Goal
1. To explore the use of probability in word2vec models.
2. To find out the relationship between the conditional probability of a word appear given other words and similarity of words.
#### Findings
##### Softmax function

##### Cosine similarity


### How to run the Python scripts?
1. Install the required libraries.
  - Install NumPy: `pip install numpy`
  - Install Gensim: `pip install gensim`
  - Install NLTK: `pip install nltk`
2. Clone this GitHub repository or directly download the files.
  - `git clone https://github.com/yueagar/ESTR2018-project.git`
3. Modify and run the scripts.
  - Testing the pre-trained Google News Word2Vec model:
    - [Download the model](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM) and modify modelPath in the script to load it properly.
    - Run the script: `python word2vec-google-news-pre-trained.py`
  - Training a Skip-Gram model:
    - Modify the filename of the train data and the target word for testing.
    - Run the script: `python word2vec-sg.py`

### References
1. Google Code - Word2Vec: https://code.google.com/archive/p/word2vec/
2. Geeks4Geeks - Implement your own word2vec(skip-gram) model in Python: https://www.geeksforgeeks.org/implement-your-own-word2vecskip-gram-model-in-python/
<hr>

#### Project Progress

- [x] Proposal
  - [x] Project subject, description and activities
- [x] Presentation powerpoint slides
  - [x] Brief introduction to word embeddings and word2vec
  - [x] Probability inside word2vec models
  - [ ] Demonstration of the code implementation
- [x] Code implementation
  - [x] Use of the pre-trained Google News word2vec model
  - [x] Training of a Skip-Gram model
- [ ] Final Report
  - [ ] Draft
  - [ ] Final LaTeX or Word file