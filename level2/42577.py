def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i != j:
                if i.startswith(j):
                    return False
    return True


# def solution(phone_book):
#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)):
#             if i != j:
#                 if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
#                     return False

#     return True
