# https://leetcode.com/problems/roman-to-integer/
s = "CMLII"
def romanToInt(s):
    num_dict = {"I" : 1, "V": 5, "X" : 10, "L" : 50,  "C" : 100, "D" :500, "M": 1000}
    num = 0
    if len(s) == 1:
        return num_dict[s]

    if len(s) == 2:
        if num_dict[s[1]] > num_dict[s[0]]:
            return num_dict[s[1]] - num_dict[s[0]]
        else:
            return num_dict[s[0]]+ num_dict[s[1]]

    if len(s) >  2:        
        num += num_dict[s[-1]]
        for i in range(0, len(s)-1):
            if i < len(s)-1:
                if num_dict[s[i]] < num_dict[s[i+1]]:
                    num -= num_dict[s[i]]
                else: 
                    num += num_dict[s[i]]
        return num

print(romanToInt(s))
