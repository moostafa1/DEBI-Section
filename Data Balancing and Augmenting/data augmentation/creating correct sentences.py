import random
import nltk
from nltk.corpus import brown
nltk.download('brown')

def generate_sentences(n):
    sentences = brown.sents()
    grammatically_correct_sentences = [' '.join(sentence) for sentence in sentences]
    selected_sentences = random.sample(grammatically_correct_sentences, n)
    return selected_sentences

num_sentences = 3945
correct_sentences = generate_sentences(num_sentences)

with open('correct_sentences.txt', 'w') as f:
    for sentence in correct_sentences:
        f.write(sentence + '\n')
