def isValid(s):
    open_bracket = ["(", "[", "{"]
    close_bracket = [")", "]", "}"]

    if s == "":
        return True
    
    for i in range(len(s)):
        if s[i] in open_bracket:
            index_o = s.index(s[i])
            if i+1 < len(s):
                if s[i+1] in close_bracket:
                    if close_bracket.index(s[i+1]) == index_o:
                        s = s[:i] + s[i+1:]
                        return True 

    return False 

s = ""
print(isValid(s))