def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def count_words(text):
  return len(text.split())

def main():
  file_contents = get_book_text("books/frankenstein.txt")
  num_words = count_words(file_contents)
  print(f"{num_words} words found in the document")

main()