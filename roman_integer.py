def roman_integer(s):
    I = 1 ; V = 5 ; X = 10 ; L = 50 ; C = 100 ; D = 500 ; M = 1000
    ans = 0
    previous_char = 0
    for alpha in s:
        if alpha == "I":
            current_char = 1
            ans += 1
        if alpha == "V":
            current_char = 5
            ans += 5
        if alpha == "X":
            current_char = 10
            ans += 10
        if alpha == "L":
            current_char = 50
            ans += 50
        if alpha == "C":
            current_char = 100
            ans += 100
        if alpha == "D":
            current_char = 500
            ans += 500
        if alpha == "M":
            current_char = 1000
            ans += 1000

        if previous_char < current_char:
            ans -= 2 * previous_char

        if alpha == "I":
            previous_char = 1
        if alpha == "V":
            previous_char = 5
        if alpha == "X":
            previous_char = 10
        if alpha == "L":
            previous_char = 50
        if alpha == "C":
            previous_char = 100
        if alpha == "D":
            previous_char = 500
        if alpha == "M":
            previous_char = 1000
    return ans 

s = "MCMXCIV"
print(roman_integer(s))
