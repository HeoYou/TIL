#tree BFS DFS 만들기

# deque를 사용한 이유는 bfs에서 큐를 사용하기 때문에
from collections import deque
import sys
input = sys.stdin.readline

# make tree
def make_tree() -> list:
    n, m = map(int, input().split())

    tree = [[] for i in range(n + 1)]

    for i in range(m):
        p, c = map(int, input().split())
        tree[p].append(c)
        tree[c].append(p)

    return tree

def DFS(tree: list, start_node: int):

    stack = []
    visit = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        print(node)
        visit.append(node)

        for n in tree[node]:
            if n not in visit:
                stack.append(n)

def BFS(tree: list, start_node: int):
    queue = deque()
    visit = []

    queue.append(start_node)

    while queue:
        node = queue.popleft()
        print(node)
        visit.append(node)

        for n in tree[node]:
            if n not in visit:
                queue.append(n)

tree = make_tree()
DFS(tree, 1)
print()
BFS(tree, 1)


    
    

