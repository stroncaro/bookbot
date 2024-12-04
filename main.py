def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    word_count = get_word_count(book_contents)
    char_dict = get_char_dict(book_contents)
    char_list = get_char_list(char_dict)
    char_list.sort(reverse=True, key=lambda char: char["count"])

    print_book_stats(book_path, word_count, char_list)
    print_footer()


def print_footer():
    print()
    print("Thank you for using BookBot.")
    print("Beep Bop!")


def print_book_stats(path, word_count, char_list):
    column_quantity = 3
    char_chunks = chunk_list(char_list, column_quantity)

    print(f"*** Report of {path} ***")
    print()
    print(f"The book has {word_count} words.")
    print()
    print(f"Character usage data:")

    col_padding = " " * 5
    col_size = len(str(char_chunks[0][0]["count"]))
    for chunk in char_chunks:
        print("  ", end="")
        for char_data in chunk:
            print(
                f"{char_data["char"]}: {char_data["count"]:>{col_size}}{col_padding}",
                end="",
            )
        print()
    print("*** End of report ***")


def chunk_list(lst, chunk_num):
    return [lst[i : i + chunk_num] for i in range(0, len(lst), chunk_num)]


def get_char_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    return char_list


def get_book_contents(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_char_dict(text):
    text = text.lower()
    chars = {}
    for char in text:
        chars[char] = chars.get(char, 0) + 1
    return chars


main()
