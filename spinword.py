def spin_words(sentence):
    sentence = sentence.split()
    for y,x in enumerate(sentence):
        if len(x) >= 5:
            sentence[y] = x[::-1]
            continue
        sentence[y] = x
        
    return ' '.join(sentence)