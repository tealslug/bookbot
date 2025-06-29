import sys
from stats import get_num_words, get_character_counts, sort_character_counts

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  print("============ BOOKBOT ============")

  book_path = sys.argv[1]
  print(f"Analyzing book found at {book_path}...")
  file_contents = get_book_text(book_path)

  num_words = get_num_words(file_contents)
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")

  print("--------- Character Count -------")
  chars = get_character_counts(file_contents)
  for k, v in sort_character_counts(chars):
    if k.isalpha():
      print(f"{k}: {v}")

main()