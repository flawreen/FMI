def arrayManipulation(n, queries):
    # Write your code here
    ls = [0 for _ in range(n + 1)]
    ok = 0
    res = 0
    val_max = queries[0][2]
    freq = [0 for _ in range(len(queries))]
    for i in range(1, len(queries)):
        print(queries[i])
        if queries[i][0] <= queries[i - 1][1]:
            ok = 1
            freq[i] = 1
            for j in range(queries[i][0], queries[i-1][1] + 1):
                ls[j] = ls[j] + queries[i][2] + queries[i - 1][2] if freq[i-1] == 0 else ls[j] + queries[i][2]
                print(j, ls[j])
            res = max(res, ls[queries[i][0]])
        else:
            val_max = max(val_max, queries[i][2])

    print(ls)
    if not ok:
        return val_max
    else:
        return res


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
