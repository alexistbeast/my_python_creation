def solution(args):
    result = []
    i = 0
    while i < len(args):
        start = args[i]
        while i + 1 < len(args) and args[i + 1] == args[i] + 1:
            i += 1
        if i - (args.index(start)) >= 2: #donc si c'est une suite
            result.append(f"{start}-{args[i]}")
        else:
            print(args.index(start),i)
            # Sinon on ajoute les éléments individuels
            for j in range(args.index(start), i + 1):
                result.append(str(args[j]))
        i += 1
    return ",".join(result)
