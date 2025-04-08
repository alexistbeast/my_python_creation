import math
def get_middle(s):
    #If the string's length is impair, return the middle character.
    #If the string's length is paire, return the middle 2 characters.
    if len(s) % 2 != 0: #si impair
        index_milieu = math.floor(len(s) / 2)
        return s[index_milieu]
    elif len(s) % 2 == 0: #si pair
        index_1 = s[round(len(s) /2)-1]
        index_2 = s[round(len(s) /2)]
        return index_1 + index_2
    

print(get_middle("test"))
print(get_middle("testing"))