# Practical 29: Count the words in a sentence using a custom function


def count_words(sentence):
    """Return the number of words in the sentence."""
    words = sentence.split()      # split() ignores extra spaces
    return len(words)


text = input("Enter a sentence: ")
print("Number of words:", count_words(text))
