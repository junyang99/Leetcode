def generateParenthesis(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['()']
    res = []
    for i in range(n):
        for e1 in generateParenthesis(i):
            for e2 in generateParenthesis(n-1-i):
                res.append('(' + e1 + ')' + e2)
    return res

print(generateParenthesis(2))