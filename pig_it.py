import string
def pig_it(text):
    mots = text.split()
    mots_modifies = []
    for mot in mots:
        if mot[-1] in string.punctuation:
            mot_modifie =  mot[-1]
        elif len(mot) > 1:
            mot_modifie = mot[1:-1] + mot[-1] + mot[0] + "ay"
        elif len(mot) == 1:
            mot_modifie = mot + "ay"
        mots_modifies.append(mot_modifie)
    phrase = " ".join(mots_modifies)
    return phrase




print(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
print(pig_it('This is my string'),'hisTay siay ymay tringsay')