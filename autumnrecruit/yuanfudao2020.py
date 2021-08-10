# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 9:26 下午
# @Author  : Kai Zheng
# @FileName: yuanfudao2020.py
# @Software: PyCharm
# @Email: 156252108@qq.com
'''
# T = int(input())

from collections import deque
def help(arr):
    N = len(arr)
    adj = [[] for _ in range(N)]
    degree = [0] * N
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                degree[i] += 1
                adj[j].append(i)
    queue = deque()
    for i in range(N):
        if not degree[i]:
            queue.append(i)
    while queue:
        node = queue.popleft()
        for x in adj[node]:
            degree[x] -= 1
            if degree[x] == 0:
                queue.append(x)
    if sum(degree) == 0:
        return 1
    else:
        return 0
# for _ in range(T):
#     N = int(input())
#     arr = []
#     for i in range(N):
#         arr.append(list(map(int, input().split())))
#         print(help(arr))
arr= [[0,1,0],[0,0,0],[0,0,0]]
print(help(arr))
'''

from collections import deque
arr= [[0,1,0],[0,0,0],[0,0,0]]
N = len(arr)
adj = [[] for _ in range(N)] # 记录 arr[i]中 == 1 的 i index，列信息
degree = [0] * N # 记录arr[i]里面有几个1
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            degree[i] += 1
            adj[j].append(i)
print(degree)
print(adj)
queue = deque() # 如果degree里面是0，queue记录这个index：就是说queue 记录arr中都是0的index
for i in range(N):
    if not degree[i]:
        queue.append(i)
print(queue)
while queue: # 如果 queue不为空的话就循环
    node = queue.popleft()
    for x in adj[node]: #遍历列信息中的为1 的i index 每个减去1
        degree[x] -= 1
        if degree[x] == 0:
            queue.append(x) # queue 这个x index
if sum(degree) == 0: 如果degree 中所有都是0，说明可以正确加载。
    print(1)
else:
    print(0)
