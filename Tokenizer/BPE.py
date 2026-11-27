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


#print(initialize_corpus(corpus))


def count_pairs(corpus):
    # Your implementation
    

    pair_freq = {}
    # Iterate through every word's character sequence.
    for tokens in corpus:
        pairs = zip(tokens, tokens[1:])

        for pair in pairs:
            if pair in pair_freq:
                pair_freq[pair] += 1
            else:
                pair_freq[pair] = 1

        
    return pair_freq



def get_most_frequent_pair(corpus):
    # Your implementation
    pair_freq = count_pairs(corpus)
    return max(pair_freq, key=pair_freq.get)

      
#print(get_most_frequent_pair(corpus))


def merge_tokens(tokens, pair):
    merged_tokens = []
    i = 0

    while i < len(tokens):

        # Check whether the current and next tokens match.
        if (
            i < len(tokens) - 1
            and (tokens[i], tokens[i + 1]) == pair
        ):
            # Combine the two tokens.
            merged_token = tokens[i] + tokens[i + 1]

            merged_tokens.append(merged_token)

            # Skip both original tokens.
            i += 2

        else:
            # Keep the current token unchanged.
            merged_tokens.append(tokens[i])

            i += 1

    return merged_tokens

def merge_pair(corpus, pair):
    merged_corpus = []

    for tokens in corpus:
        merged_tokens = merge_tokens(tokens, pair)

        merged_corpus.append(merged_tokens)

    return merged_corpus



#print(merge_pair(initialize_corpus(corpus), get_most_frequent_pair(corpus)))



def train_bpe(corpus, num_merges):
    # Initialize the corpus.
    initialized_corpus = initialize_corpus(corpus)

    merge_pairs = []

    for _ in range(num_merges):
        # Count the frequency of pairs.
        pair_freq = count_pairs(initialized_corpus)

        # Get the most frequent pair.
        most_frequent_pair = get_most_frequent_pair(initialized_corpus)

        # Merge the most frequent pair in the corpus.
        initialized_corpus = merge_pair(initialized_corpus, most_frequent_pair)

        merge_pairs.append(most_frequent_pair)
        
    return initialized_corpus, merge_pairs


final_corpus, merge_rules = train_bpe(
    corpus,
    num_merges=5
)

print("Final Corpus:", final_corpus)
print("Merge Rules:", merge_rules)