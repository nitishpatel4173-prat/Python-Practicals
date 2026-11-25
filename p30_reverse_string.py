# Practical 30: Reverse a string using a function


def reverse_string(text):
    """Return the reverse of text using a loop."""
    reversed_text = ""
    for character in text:
        reversed_text = character + reversed_text   # add each character at the front
    return reversed_text


word = input("Enter a string: ")
print("Reversed (loop)   :", reverse_string(word))
print("Reversed (slicing):", word[::-1])
