def solution(arr):
    arr.sort()
    
    answer=True
    for i in range(len(arr)-1):
        if arr[i+1].startswith(arr[i]):
            answer=False
            break
    return answer



# def solution(phone_book):
#     for i in phone_book:
#         for j in phone_book:
#             if i != j:
#                 if i.startswith(j):
#                     return False
#     return True




