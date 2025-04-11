import string
def rot13(message):
    alphabet_min = string.ascii_lowercase
    alphabet_maj = string.ascii_uppercase
    reponse = ""
    for i in message:
        if i in alphabet_min:
            start_index = alphabet_min.index(i)
            target_key = (start_index + 13) % 26 #13 car décalage de rot 13 et 26 car il y a que 26 lettre dans l'alphabet donc imaginons z = 26 26 + 13 et 39 39 % 26 = 13
            reponse += alphabet_min[target_key]
        elif i in alphabet_maj:
            start_index = alphabet_maj.index(i)
            target_key = (start_index + 13) % 26 #13 car décalage de rot 13 et 26 car il y a que 26 lettre dans l'alphabet donc imaginons z = 26 26 + 13 et 39 39 % 26 = 13
            reponse += alphabet_maj[target_key]
        else:
            reponse += i
    return reponse
    
        



print(rot13('test'))