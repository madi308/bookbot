import sys

from stats import get_num_words, get_num_characters, sort_character_frequencies

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_frequencies = sort_character_frequencies(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for el in sorted_frequencies:
        print(el["char"] + ": " + str(el["num"]))
    print("============= END ===============")

if __name__=="__main__":
    main()