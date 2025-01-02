def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    characters_count =count_characters(text)
    print(characters_count)
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




    

main()



    