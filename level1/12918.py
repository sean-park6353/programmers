def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i].isalpha() == True:
                return False
        return True
    else:
        return False
