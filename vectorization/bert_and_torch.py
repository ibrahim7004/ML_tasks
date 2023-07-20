from transformers import BertTokenizer, BertModel   # Makes use of BERT classes for contextualized representations of words and tokenization
import torch    # For calculation using cosine similarity

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')  # loads a pre-trained BERT tokenizer
model = BertModel.from_pretrained('bert-base-uncased')       # loads a pre-trained BERT model

# Encode input words
input_ids = tokenizer.encode("cat", "dog", add_special_tokens=True) # Tokenized to encode the words into token IDs (according to BERT model)
input_ids = torch.tensor([input_ids])   # PyTorch Tensor object created using torch.tensor, 
                                        # which expects input in a 2D tensor format(each row represents a sequence of token IDs.)

# Get word embeddings from BERT model
with torch.no_grad():       # context manager, which temporarily disables gradient calculation
    embeddings = model(input_ids)[0]    # passes the input_ids tensor to the BERT model, resulting in a tuple of outputs.

# Calculate cosine similarity between word embeddings of 'cat' and 'dog'
similarity = torch.cosine_similarity(embeddings[0][0], embeddings[0][1], dim=0) # Comparing word 1 and word 2 stored in embeddings
print(similarity.item())
