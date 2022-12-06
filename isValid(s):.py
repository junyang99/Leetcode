def isValid(s):
    open_bracket1 = False
    open_bracket2 = False
    open_bracket3 = False
    outer_layer = False
    middle_layer = False
    inner_layer = False

    for char in s:
        if char == "(":
            open_bracket1 = True
            open_bracket2 = False
            open_bracket3 = False
            if outer_layer == False:
                outer_layer = True
            elif outer_layer == True and middle_layer == False:
                middle_layer = True
            elif outer_layer == True and middle_layer == True:
                inner_layer = True

        elif char == "[":
            open_bracket2 = True
            open_bracket1 = False
            open_bracket3 = False
            if outer_layer == False:
                outer_layer = True
            elif outer_layer == True and middle_layer == False:
                middle_layer = True
            elif outer_layer == True and middle_layer == True:
                inner_layer = True

        elif char == "{":
            open_bracket3 = True
            open_bracket1 = False
            open_bracket2 = False
            if outer_layer == False:
                outer_layer = True
            elif outer_layer == True and middle_layer == False:
                middle_layer = True
            elif outer_layer == True and middle_layer == True:
                inner_layer = True
        
        if char == ")" and open_bracket1 == False:
            return False
        elif char == "]" and open_bracket2 == False:
            return False
        elif char == "}" and open_bracket3 == False:
            return False
    return True

s = ""

print(isValid(s))

#"{[]}" = True
#"([)]" = false
