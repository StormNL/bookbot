def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    text_split = text.split()
    word_count = len(text_split)
    return word_count

def count_characters(text):
    characters = []
    lower_characters = text.lower()
    
    

main()


    