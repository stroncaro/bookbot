def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    word_count = get_word_count(book_contents)
    char_dict = get_char_dict(book_contents)
    char_list = get_char_list(char_dict)
    char_list.sort(reverse=True, key=lambda char: char["count"])

    print(f"*** Report of {book_path} ***")
    print()
    print(f"The book has {word_count} words.")
    print()
    print(f"Character usage data:")
    for char_data in char_list:
        print(f"  {char_data["char"]}: {char_data["count"]}")
    print("*** End of report ***")
    print()
    print("Thank you for using BookBot.")
    print("Beep Bop!")


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
