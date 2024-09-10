text: str = ''
bad_words: list[str] = []

with open('input.txt', encoding= 'utf-8') as f:
    text = f.read()

with open('bad-words.txt', encoding= 'utf-8') as f:
    bad_words = f.read().split(' ')

for word in bad_words:
    text = text.replace(word, len(word) * '*')

with open('output.txt', 'w', encoding='utf-8')as f:
    f.write(text)
