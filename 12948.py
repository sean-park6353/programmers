def solution(phone_number):
    tmp = phone_number[-4:]
    result = phone_number.strip(tmp)
    answer = result
    answer = "*"*len(result)+tmp
    return answer


solution('01033334444')
