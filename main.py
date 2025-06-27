from stats import get_num_words, get_character_counts

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main():
  file_contents = get_book_text("books/frankenstein.txt")
  num_words = get_num_words(file_contents)
  print(f"{num_words} words found in the document")
  chars = get_character_counts(file_contents)
  print(chars)

main()