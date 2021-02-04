
def solution(skill, skill_trees):
    cnt=0
    for s in skill_trees:
        essential=[] # 필수 스킬들만 저장할 리스트
        for alpha in s:
            if alpha in skill:   # 필수 스킬들만 뽑아서 essentail에 넣는다.
                essential.append(alpha)
        present_skill_tree=''.join(essential)
        if len(skill)==len(present_skill_tree):
            if skill==present_skill_tree:
                cnt+=1
        else:
            flg=0
            for i in range(len(present_skill_tree)):
                if present_skill_tree[i]==skill[i]:
                    flg+=1
            if flg==len(present_skill_tree): 
                cnt+=1
    return cnt


a="cbd"
skill_trees=["bacde","cbadf","aecb","bda","cxpvd"]

print(solution(a,skill_trees))
