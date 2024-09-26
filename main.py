def get_contents(book_path):
    with open(book_path, 'r') as f:
        return f.read()


def count_words(book_string):
    words = book_string.split()
    return len(words)


def count_characters(book_string):
    char_counts = {}
    for letter in book_string:
        if letter.isalpha():
            letter = letter.lower()
            if letter in char_counts:
                char_counts[letter] += 1
            else:
                char_counts[letter] = 1

    return char_counts


def print_report(book_path, word_count, char_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    char_list = []
    for key in char_dict:
        char_list.append({"char": key, "num": char_dict[key]})
    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


book_path = 'books/frankenstein.txt'
contents = get_contents(book_path)
word_count = count_words(contents)
char_counts = count_characters(contents)
print_report(book_path, word_count, char_counts)
