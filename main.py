def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    characters_count = count_characters(text)
    char_list = only_alphabet(characters_count)
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    text_split = text.split()
    word_count = len(text_split)
    return word_count

def count_characters(text):
    characters = {}
    lower_characters = text.lower()
    for character in lower_characters:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def only_alphabet(characters_count):
    chars_list =[]
    for char, count in characters_count.items():
        if char.isalpha():
            chars_list.append({"char": char, "num":count})
    return chars_list
    
main()