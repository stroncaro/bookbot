def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    print(book_contents)


def get_book_contents(path):
    with open(path) as f:
        return f.read()


main()
