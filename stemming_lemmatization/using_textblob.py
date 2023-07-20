from textblob import Word   # Using Word in textblob.

def lemmatize(list_of_words):
    print("\nLemmatization: \n")
    for element in list_of_words:
        # Creating a Word object.
        u = Word(element)

        # Applying lemmatization:
        print("{}: {}".format(element, u.lemmatize()))

def stem(list_of_words):
    print("\n\nStemming: \n")
    for element in list_of_words:
        # Creating a Word object.
        w = Word(element)

        # Applying stemming:
        print("{}: {}".format(element, w.stem()))


list_of_words = ["rocks", "geese", "loaves", "children", "tomatoes", "wolves"]

print("\nUSING TEXTBLOB\n------------------\n")

# Function calls:
lemmatize(list_of_words)
stem(list_of_words)