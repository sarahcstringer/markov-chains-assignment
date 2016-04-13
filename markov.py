from random import choice
import sys

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

    return text

    # return "This should be a variable that contains your file text as one long string"


def make_chains(text_string, n=2):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    text = text_string.split()
    
    chains = {}

# n-grams
    for i in range(len(text) - n):
        words = []
        for j in range(n):
            words.append(text[i + j])
        words = tuple(words)
        chains[words] = chains.get(words, []) + [text[i + n]]


# bi-grams:
    # for i in range(len(text) - 2):
    #     word_pair = (text[i], text[i + 1])
    #     chains[word_pair] = chains.get(word_pair, []) + [text[i + 2]]


        # word_pair = (text[i], text[i + 1])
        # value = chains.get(word_pair, [])
        # value.append(text[i + 2])
        # chains[word_pair] = value


        # if value == []:
        #     print ("found an empty value for tuple", word_tuple)
        #     chains[word_tuple] = [add_value]
        # else:
        #     print ("found a non-empty value for tuple", word_tuple, ":", value)            
        #     new_value = chains[word_tuple].append(add_value)
        #     print ("adding value", new_value, "for key", word_tuple)            
        #     chains[word_tuple] = new_value
            
    print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    
    current_key = choice(chains.keys())
    text = " ".join(current_key)


    while True:
        if current_key in chains:
            string = choice(chains[current_key])
            text = "{} {}".format(text, string)
            current_key = (current_key[1], string)

        else:
            return text

    # while len(text) < 20:

    #     string = choice(chains[current_key])
    #     text = "{} {}".format(text, string)
    #     current_key = (current_key[1], string)

    # return text



        # if current_key not in chains:
        #     return text

        # string = choice(chains[current_key])
        # text = "{} {}".format(text, string)
        # current_key = (current_key[1], string)
      

# input_path = "hello.txt"
input_path = sys.argv[1]
n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains)

print random_text
