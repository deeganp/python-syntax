def print_words_uppercase (words):
    """Print Words on each line changed to uppercase"""

    for word in words:
        print(word.upper())



def print_words_uppercase2(words):
     """Print each word on sep line, uppercased, if starts with E or e."""
     for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())




def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given"""
    for word in words:
        for letter in must_start_with:
             if word.startswith(letter):
                print(word.upper())
                break

