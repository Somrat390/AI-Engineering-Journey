corpus = [
    "low",
    "lower",
    "lowest"
]

# for word in corpus:
#     characters = list(word)
#     print(characters) 


def initialize_corpus(corpus):
    # Your implementation
    # Accept a list of words.
    # Convert each word into a list of individual characters.
    character_lists = [list(word) for word in corpus]

    #Return the converted corpus.
    return character_lists


print(initialize_corpus(corpus))


    