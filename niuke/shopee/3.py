# [[-2,-3,3],[-5,-10,1],[10,30,-5]],[0,0],[2,2]
# 详细描述
# 一个机器人要从起始点A和终点B。机器人从起点开始，每次能从上，下，左，右移动一步通过一个房间。并且每个房间只能路过一次。

# 设定机器人的健康数为H，如果经过的房间是正整数a，那么机器人经过这个房间就能获得对应的健康点数，健康数变成H+a，如果经过的房间为负数，那么机器人就会失去对应的健康点数a， 机器人的健康数变成H-a，问如果要保证机器人生命数一直是正数，H初始值至少为多少？

# 房间点数由一个二维数组M*N 表示，起点和终点由一个一维数组组成。

# 1 <= M,N <= 200

# m == rooms.length

# n == rooms[i].length

# -1000 <= rooms[i][j] <= 1000

# 0 <= i,j <= M,N


#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param rooms int整型二维数组 房间
# @param startPoint int整型一维数组 起始点
# @param endPoint int整型一维数组 终点
# @return int整型
#

#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param rooms int整型二维数组 房间
# @param startPoint int整型一维数组 起始点
# @param endPoint int整型一维数组 终点
# @return int整型
#
class Solution:
    def minimumInitHealth(self, rooms, startPoint, endPoint) :
        # write code here
        # 所有行走方案中的最优方案（最小的路径元素和的值最大），返回最小 路径元素和 的相反数+1
        # DP
        Sum=room[0][0]
        out=0
        while i <= len(rooms):
            while j <= len(rooms[i]):
                if room[i][j+1]>= room[i+1][j]
                    out =min(Sum,Sum + room[i][j+1])
                    Sum =Sum + room[i][j+1]
        return -out+ 1




