import sys
from stats import word_count, character_count, dict_to_list


def get_book_text(file_path):
    file_content = None
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    path = None
    try:
        path = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(path)
    num_words = word_count(book_text)
    character_map = character_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in dict_to_list(character_map):
        if False == i["char"].isalpha():
            continue
        else:
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()