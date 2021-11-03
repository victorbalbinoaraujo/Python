def add_prefix_un(word):
    return 'un' + word

def make_word_groups(vocab_words):
    return f' :: {vocab_words[0]}'.join(vocab_words)

def remove_suffix_ness(word):
    return word.replace('iness', 'y') if word.endswith('iness') else word.replace('ness', '')

def noun_to_verb(sentence, index):
    return sentence.replace('.', '').split(' ')[index] + 'en'