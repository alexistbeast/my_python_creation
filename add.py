def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    result = ""
    for p in sorted(factors):
        exp = factors[p]
        if exp == 1:
            result += f"({p})"
        else:
            result += f"({p}**{exp})"
    return result

print(add(1)(2)(3)(4)(5))  # Affiche 15
print(add(1)(2)(3))  # Affiche 6
print(add(1)(2))  # Affiche 3
print(add(1))  # Affiche 1
