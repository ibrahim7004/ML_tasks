"""     Basic manual way of doing same task using Jaccard similarity coefficient.
Not practical for actual data because of Lack of Semantic Understanding, 
Sensitivity to Vocabulary Size and Limited Contextual Understanding         """

from nltk.tokenize import word_tokenize   # To automate the process of tokenization of words.

# Example sentences:
sentences = ["cat is a domestic animal", "dog is a loyal companion"]

# Tokenization:
tokens_cat = [token.lower() for token in word_tokenize(sentences[0])]   # Tokenize first sentence (first element in list)
tokens_dog = [token.lower() for token in word_tokenize(sentences[1])]   # Tokenize second sentence (second element in list)

# Easy way to create vocabulary (store only the unique words by converting to set):
word_set_cat = set(tokens_cat)
word_set_dog = set(tokens_dog)

# Calculate Jaccard similarity between word sets:
intersection = word_set_cat.intersection(word_set_dog)  # Calc. intersection of the word sets.
union = word_set_cat.union(word_set_dog)                # Calc. union of the word sets.

similarity = len(intersection) / len(union)     # Apply basic Jaccard similarity formula.
print(similarity)
