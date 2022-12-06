def lengthOfLastWord(s):
    split_word = s.split(' ')
    for i in range(1, len(split_word) + 1):
        if split_word[-i].isalpha():
            ans = split_word[-i]
            return len(ans)


s = "hello world"
print(lengthOfLastWord(s))
