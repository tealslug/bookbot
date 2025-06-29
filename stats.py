def get_num_words(text):
  return len(text.split())

def get_character_counts(text):
  chars = {}
  for c in [x.lower() for x in text]:
    if c not in chars:
      chars[c] = 1
    else:
      chars[c] += 1
  return chars

def sort_by_count(items):
  return items[1]

def sort_character_counts(chars):
  return sorted(chars.items(), key=sort_by_count, reverse=True)