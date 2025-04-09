def order(sentence):
    phrase = ""
    if not sentence:
        return ""
    mots = sentence.split()
    n = 9
    for i in range(n+1):
        for mot in mots:
            if str(i) in mot:
                phrase += mot
                phrase += " "
    phrase = phrase.strip()
    return phrase


print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""), "")