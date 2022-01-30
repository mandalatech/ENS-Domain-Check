import json
import os
import re

if __name__ == '__main__':
    books = os.listdir('books')
    processed_words = {}

    for book in books:
        print(book)
        with open(f'books/{book}', 'r') as f:
            for line in f:
                words = str(line).split(' ')
                words = [
                    word.strip(' ').strip('\n').lower() for word in words
                    if re.match(r"^[A-Za-z]+$", word)
                ]
                for word in words:
                    if len(word) == 5:
                        if word in processed_words.keys():
                            processed_words[word] = processed_words[word] + 1
                        else:
                            processed_words[word] = 1
    processed_words = dict(
        sorted(processed_words.items(), key=lambda item: item[1],
               reverse=True))

    with open('word_summary.json', 'w') as f:
        json.dump(processed_words, f, indent=4)