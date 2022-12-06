def isValid(s):
        open_characters = ['(', '[', '{']
        close_characters = [')', ']', '}']
        if s=="":
            return True

        for i in range(len(s)):
            if s[i] in open_characters:
                index_o = open_characters.index(s[i])
                if i+1 < len(s):
                    if s[i+1] in close_characters:
                        if close_characters.index(s[i+1])==index_o:
                            s = s[:i]+s[i+2:]
                            return True
        return False

s = "(]"
print((isValid(s)))