def get_contents(book_path):
    with open(book_path, 'r') as f:
        return f.read()


def count_words(book_string):
    words = book_string.split()
    return len(words)


book_path = 'books/frankenstein.txt'
contents = get_contents(book_path)
word_count = count_words(contents)
print(f"{book_path} is {word_count} words long")
