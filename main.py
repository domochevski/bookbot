from stats import count_words, count_chars, sorted_list_of_dictionaries
import sys

def get_book_text(book):
    with open(book, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    book_to_analyze = sys.argv[1]
    text = get_book_text(book_to_analyze)
    words_in_book = count_words(text)
    charachters_in_book = count_chars(text)
    sorted_list = sorted_list_of_dictionaries(charachters_in_book)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_to_analyze}...')
    print("----------- Word Count ----------")
    print(f'Found {words_in_book} total words')
    print("--------- Character Count -------")
    for char in sorted_list:
        if char["char"].isalpha():
            print(f'{char["char"]}: {char["num"]}')
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main()
    