from nltk.corpus import wordnet     # WordNet is a lexical database that organizes words into synsets.

# Get synsets (word senses) for "cat" and "dog": synsets are the 'word senses'.
synsets_cat = wordnet.synsets('cat')        
synsets_dog = wordnet.synsets('dog')

similarity_scores = []     # Initialise empty list to later store similarity scores

# Calculate similarity between each pair of synsets:      
for synset_cat in synsets_cat:      # iterates through each synset of "cat" and "dog"                  
    for synset_dog in synsets_dog:
        similarity = synset_cat.path_similarity(synset_dog)     # computes the path similarity (based on 
        if similarity is not None:                              # distance and hierarchical relationships)
            similarity_scores.append(similarity)        # If there is some similarity then add to the list 'similarity_scores'.

# Calculate average similarity
if similarity_scores:      
    average_similarity = sum(similarity_scores) / len(similarity_scores)     # calculates the average similarity by summing the
    print(average_similarity)                                                # obtained similarity and dividing by the number of scores
else:
    print("No similarity found.")
