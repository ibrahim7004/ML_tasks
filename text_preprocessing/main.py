# Defining file paths:   
stopwords_file_path = r'C:/Users/hp/Desktop/stopwords.txt'
main_file_path = r'C:/Users/hp/Desktop/urdu.txt'
frequencies_file_path = r'C:/Users/hp/Desktop/frequencies.txt'

# Function to open and read both txt files, and remove stopwords from file named urdu.txt:
def remove_stopwords(): 
    # Read stopwords from the stopwords file:
    with open(stopwords_file_path, 'r', encoding='utf-8') as stopwords_file:    # Specifying encoding='utf-8' to ensure the files are read/written using UTF-8 encoding.
        stopwords = stopwords_file.read().split(':') # Split using ':' as the delimiter.

    # Read the main Urdu file:
    with open(main_file_path, 'r', encoding='utf-8') as main_file:
        content = main_file.read()

    # Remove stopwords from the main file:
    for word in stopwords:
        content = content.replace(word, '')     # Replace any word that is a stopword with an empty space (' ').

    # Write the modified content back to the main file
    with open(main_file_path, 'w', encoding='utf-8') as main_file:
        main_file.write(content)    # Update the original file with removed stopwords.

def count_and_store():
    # Read the modified Urdu file:
    with open(main_file_path, 'r', encoding='utf-8') as main_file:
        content = main_file.read()

    words = content.split()
    """ Tokenize the content into words: 
            1) 'content' contains all urdu words, 
            2) .split uses space/whitespace as delimiter, 
            3) 'words' is the final list of all urdu words stored as separate elements in the list. """
    
    word_frequencies = {}   # Dictionary to store frequencies with their corresponding words.

    # Count the frequency of each word:
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1     # Increment if reapeated.
        else:
            word_frequencies[word] = 1      # Set freq. to 1 if word encountered for the first time in file.

    sorted_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    # Sort the word frequencies in descending order:
    """  1) 'word_frequencies.items()' returns tuples of key-value pairs from the dictionary.
         2) 'sorted()' used to sort the tuples based on second element of each tuple, i.e frequency.
             2.1) 'lambda x: x[1]' takes a tuple x and returns its second element (x[1]), which corresponds to freq.
         3) 'reverse=True' parameter is used to sort the tuples in descending order.    """

    # Write the word frequencies to the frequencies file:
    with open(frequencies_file_path, 'w', encoding='utf-8') as frequencies_file:
        for word, frequency in sorted_frequencies:
            frequencies_file.write(f"{word} : {frequency}\n")   
    """      1) tuple elements are unpacked into the variables word and frequency.
             2) f-string formatting used, '{word} : {frequency}' part formats word and freq. values.
             3) Separated with a ':' in between, and '\n' used to store each pair on one line.      """
    
    return sorted_frequencies

# Function to find unique words (which I've defined as words with freq. of 1):
def find_unique_words():
    remove_stopwords()
    sorted_frequencies = count_and_store()
    unique_words = []

    # Iterate over the sorted word frequencies:
    for word, frequency in sorted_frequencies:
        if frequency == 1:
            unique_words.append(word)   # If freq. is 1, add the word to the list: 'unique_words'.
    print(unique_words)


# find_unique_words()