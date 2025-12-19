import sys
from stats import word_count, char_count, dict_to_list, sort_counts, print_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as file:
        return file.read()

def main():
    text = get_book_text(sys.argv[1])
    char_counts = char_count(text)
    count_list = dict_to_list(char_counts)
    sort_counts(count_list)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")
    print_list(count_list)
    print("============= END ===============")

if __name__ == "__main__":
    main()
