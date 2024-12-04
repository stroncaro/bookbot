def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    book_word_count = get_word_count(book_contents)
    print(book_word_count)


def get_book_contents(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


main()
