from collections import Counter

begin="hit"
target="cog"
words=["hot","dot","dog","lot","log","cog"]
tmp=[False]*6
visit=dict(zip(words,tmp))
cnt=0

# print(visit)

def dfs(start,next):
    global cnt
    visit[next]=True
    if visit[target]==True:
        return
    for i in words:
        if visit[i]==True:   # 방문했으면
            continue
        if len(set(next)-set(i))==1: 
            cnt+=1
            dfs(next,i)

for i in words:
    visit=dict(zip(words,tmp))
    if len(set(begin)-set(i))==1:
        dfs(begin,i)