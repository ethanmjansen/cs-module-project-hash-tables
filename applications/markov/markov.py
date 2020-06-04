import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words = words.split()

after = {}

def make_pairs(words):
    pairs = []

    for word in range(len(words)-1):
        a = (words[word], words[word+1])
        pairs.append(a)

    return pairs
      
pairs = make_pairs(words)

after = {}

for word_1, word_2 in pairs:
    if word_1 in after.keys():
        after[word_1].append(word_2)
    else:
        after[word_1] = [word_2]

start_words = []
end_words = []
for word in words:
    if word.isupper() or word.startswith('"'):
        start_words.append(word)
    if word.endswith('.') or word.endswith('!') or word.endswith('?') or word.endswith('."'):
        end_words.append(word)


# TODO: construct 5 random sentences
# Your code here
for _ in range(5):
    start_here = random.choice(start_words)

    finished = False

    while not finished:
        print(start_here, end=" ")

        if start_here in end_words:
           finished = True
           print('\n')
        else:
            next_start = after[start_here]
            start_here = random.choice(next_start)
