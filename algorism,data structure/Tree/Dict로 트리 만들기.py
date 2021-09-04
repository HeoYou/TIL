# N개의 노드, M개의 간선
# 5 4
# 2 3
# 2 4
# 3 1
# 3 5

import sys
input =  sys.stdin.readline

# n개의 노드와 m개의 간선을 입력받는다.
n, m = map(int, input().split())

# 먼저 트리를 만들기 위해 dict를 만들어준다. 
dic = {i: [] for i in range(1, n + 1)}
# dict에서 1번 key 원소는 1번노드와 연결된 노드의 리스트를 뜻한다.

#총 m개의 간선을 등록하기 위해 for문을 이용한다.
for i in range(m):
    
    # parent노드 child 노드를 받는다. 
    p, c = map(int, input().split())

    # dic의 p키의 원소인 리스트에 c를 추가한다.
    dic[p].append(c)
    # 위와같이 c에 p도 추가한다. 
    dic[c].append(p)
    # 양쪽다 추가해주는 이유는 트리는 방향성이 없기 때문이다. 부모에서 자식을 찾을 수도 자식에서 부모를 찾을 수도 있다.
    


print(dic)