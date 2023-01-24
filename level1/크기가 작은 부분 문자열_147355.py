def solution(t, p):
    arr = []
    for i in range(0, len(t)+1-len(p)):
        arr.append(t[i:i+len(p)])
    
    print(arr)
    cnt = 0
    for data in arr:
        if int(p) >= int(data):
            cnt += 1 
    return cnt