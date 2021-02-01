

import operator

def solution(g,p):
    index=[i for i in range(len(p))]

    # 1단계인 장르별 합을 구해서 장르 순서 기록
    category={}
    genre=list(set(g))
    # print(genre)

    for i in genre:
        tmp=0
        for j in range(len(g)):
            if i==g[j]:
                tmp+=p[j]
        category[i]=tmp
    print(category)
    order=sorted(category.items(),reverse= True,key=operator.itemgetter(1))
    print(order)
        

    # 2단계인 장르 안에서 재생 횟수를 비교하자

    my_tuple=[]

    for i in range(len(g)):
        my_tuple.append((g[i],p[i]))
    tmp=dict(zip(index,my_tuple))

    a=sorted(tmp.items(),key= lambda x:(x[1][0],-x[1][1],x[0]))
    for i in a:
        print(i)

    answer=[]
    for i in order:
        cnt=0
        for j in a:
            if cnt==2:
                continue
            if i[0]==j[1][0]:
                answer.append(j[0])
                cnt+=1
    return answer


            
# g=['a','a','c','a','b','b','c','a','d','b','b','a']
# p=[50,50,400,50,60,90,400,100,4500,1500,1300,420]
g=['pop','pop','pop','rap','rap']
p=[45,50,40,60,70]
# solution(g,p)
print(solution(g,p))

