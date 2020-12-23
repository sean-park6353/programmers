def solution(phone_number):
    tmp = phone_number[-4:]
    result = phone_number[0:-4]
    answer = result
    answer = "*"*len(result)+tmp
    return answer


print(solution('21551241'))
