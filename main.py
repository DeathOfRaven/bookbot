from stats import get_num_words
from stats import get_num_characters
from stats import sorting
import sys

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_characters(text)
    counted = sorting(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for words in counted:
        print(f"{words["char"]}: {words["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if len(sys.argv) != 2:
    print("'Usage: python3 main.py <path_to_book>'")
    sys.exit(1)

main()