from collections import Counter

def solution(n):
    bin_n=bin(n)[2:]
    number=n+1
    bin_number=bin(number)[2:]

    while True:
        if Counter(bin_n)['1']==Counter(bin_number)['1']:
            break
        number+=1

    return number