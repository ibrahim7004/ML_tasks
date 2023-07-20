from nltk.stem import WordNetLemmatizer     # Using WordNetLemmatizer in nltk for lemmatization.
from nltk.stem import PorterStemmer         # Using PorterStemmer in nltk for stemming.
from nltk.tokenize import word_tokenize     # Using tokenization for separation of sentences into words.

def stemming(content):      # Function to perform stemming on the content we pass to it.
    ps = PorterStemmer()    # Creating an instance 'ps' of the nltk class PorterStemmer. 

    print("Stemming:\n")

    for word in content:
        print(word, " : ", ps.stem(word))   # Prints original word and its stemmed form.
    print('\n')


def lemmatizer(content):    # Function to perform lemmatization on the content we pass to it.
    lemmatizer_object = WordNetLemmatizer()   # Creating wordnet lemmatizer object.

    print("Lemmztization:\n")

    for word in content:      # For loop to iterate over each word and lemmatize it.
        print(word, " : ", lemmatizer_object.lemmatize(word))   # Prints original word and its lemmatized form.
    print('\n')


# Some English content to lemmatize, in a list:
sentence = "programming to program different programs helps programmers practice"

words = word_tokenize(sentence)     # Tokenize, to separate sentence into words.

print("\nUSING NLTK\n------------------\n")

# Function calls:
stemming(words)
lemmatizer(words)


