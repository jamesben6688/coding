import collections
def trans(s):
    letter = ""
    hm = collections.defaultdict(int)
    num = 0
    i = 0
    while i < len(s):
        if s[i].isalpha():
            if letter != "":
                hm[letter] += num
            num = 0
            letter = s[i]
        elif s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == "(":
            hm_inside, length = trans(s[i + 1:])
            i += length+1
            for k in hm_inside.keys():
                print(k,"k",hm_inside[k])
                hm[k] += int(s[i]) * hm_inside[k]
                print(k, "k", hm[k])
        elif s[i]==")":
            if letter != "":
                hm[letter] = num
            return hm, i+1
        i += 1
        if letter != "":
            hm[letter]+= num
        return list(hm.items())

print(trans("A2(A3B2)2C9"))