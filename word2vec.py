from gensim.models import Word2Vec  # Import class 'Word2Vec' to access word vectors and perform operations
from scipy import spatial   # To utlize Cosine Similarity by using 'spatial.distance' module

# Example sentences
sentences = [["cat", "kitten", "meow"], ["dog", "puppy", "bark"]]   # Training Dataset. Accuracy will be lower since it is very small.

# Train Word2Vec model
model = Word2Vec(sentences, min_count=1)    # Vector formed based on the semantic meanings of provided words.

vector_cat = model.wv['cat']    # Code obtains the word vectors for 'cat' and 'dog' using
vector_dog = model.wv['dog']    # the trained Word2Vec model 'model'.

# print(vector_cat)     # This will print the entire dense vectors for both words.
# print(vector_dog)

similarity = 1 - spatial.distance.cosine(vector_cat, vector_dog)   # Similarity calc. by using: cosine similarity: calc. angle of cos between both vectors.
print(similarity)
