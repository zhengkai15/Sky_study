# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 5:15 下午
# @Author  : Kai Zheng
# @FileName: netease.py
# @Software: PyCharm
# @Email: 156252108@qq.com
# print(float('inf')< 1)
def solution(start, graph, N):
    passed = [start]
    nopass = [x for x in range(1, N + 1) if x != start]
    dis = graph[start]

    while len(nopass):
        idx = nopass[0]
        # 选出距离起点最近的点
        for i in nopass:
            if dis[i] < dis[idx]:
                idx = i
        nopass.remove(idx)
        passed.append(idx)
        # 更新距离
        for i in nopass:
            if dis[i] > dis[idx] + graph[idx][i]:
                dis[i] = dis[idx] + graph[idx][i]
        print(dis)
    return max(dis[1:]) if max(dis[1:]) != float("inf") else -1


N, K, M = input().strip().split(' ')
N, K, M = int(N), int(K), int(M)
graph = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    graph[i][i] = 0
for _ in range(M):
    s, t, d = input().strip().split(' ')
    s, t, d = int(s), int(t), int(d)
    graph[s][t] = min(d, graph[s][t])
print(solution(K, graph, N))


