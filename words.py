# For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

def print_in_uppercase(words):
    """takes a list of words and prints each word in uppercase"""
    for word in words:
        print(word.upper())

print_in_uppercase(['hello', 'my', 'dear'])

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)  DONE

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
def print_e_words(words):
    """accepts a list of words and prints only the words starting with the letter e """
    for word in words:
        if word.startswith('e') == True:
            print(word)

print_e_words(['hello', 'my', 'everything'])

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.


def print_specific_words(words, letters):
    """accepts a list of words and prints only the words starting with any of the letters in the letters list """
    for letter in letters:
        for word in words:
            if word.startswith(letter) == True:
                print(word)


print_specific_words(['the', 'quick', 'brown', 'fox'], ['q', 'f'])