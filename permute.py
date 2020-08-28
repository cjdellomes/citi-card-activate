def permute(a, n):
    result = []

    backtrack(a, n, [], result)

    return result


def backtrack(a, n, curr, result):
    if len(curr) == n:
        result.append(list_to_str(curr))
        return

    for i in a:
        curr.append(i)

        backtrack(a, n, curr, result)

        curr.pop()


def list_to_str(a):
    s = ''
    for i in a:
        s += str(i)
    return s
