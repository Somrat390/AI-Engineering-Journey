from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "I love programming in Python!"

tokenized_text = tokenizer.tokenize(text)
tokenized_ids = tokenizer.encode(text)

print("Tokenized Text:", tokenized_text)
print("Tokenized IDs:", tokenized_ids)
print("Decoded Text:", tokenizer.decode(tokenized_ids))