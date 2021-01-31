
s='()()'

def solution(s):
    tmp=list(map(str,s.strip()))
    stack=[]
    while tmp:
        bracket=tmp.pop(0)
        if bracket=="(":
            stack.append(bracket)
        else:
            if len(stack)==0: # 비어있을 때 ) 가 오면 에러
                return False
            else:
                stack.pop()
                continue
    if len(stack)!=0:
        return False
    else:
        return True

print(solution(s))