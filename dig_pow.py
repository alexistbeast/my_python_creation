def dig_pow(n, p):
    resultat = 0
    chiffre = [int(c) for c in str(n)]
    for i in range(len(chiffre)):
        if i < len(chiffre):
            resultat += pow(chiffre[i],p)
            p += 1
    if resultat % n == 0:
        return resultat // n
    return -1






print(dig_pow(89, 1), 1)
'''print(dig_pow(92, 1), -1)
print(dig_pow(46288, 3), 51)
print(dig_pow(41, 5), 25)
print(dig_pow(114, 3), 9)
print(dig_pow(8, 3), 64)'''