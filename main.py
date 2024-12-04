def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    book_word_count = get_word_count(book_contents)
    print(book_word_count)

    book_char_count = get_char_count(book_contents)
    print(book_char_count)


def get_book_contents(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_char_count(text):
    text = text.lower()
    chars = {}
    for char in text:
        chars[char] = chars.get(char, 0) + 1
    return chars


main()
