def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0],signature[1]]
    for i in range(n-3):
        n_suite = signature[i] + signature[i+1] + signature[i+2]
        signature.append(n_suite)
    return signature
print(tribonacci([1,1,1],10))