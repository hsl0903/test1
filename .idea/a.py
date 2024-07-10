# 游戏地图
# 0: 空地
# 1: 墙
# 2: 箱子
# 3: 目标位置
# 4: 玩家
# 5: 箱子在目标位置
# 6: 玩家在目标位置
map = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

# 初始化玩家和箱子的位置
player_pos = (1, 1)
box_pos = (2, 2)
target_pos = (5, 5)

# 游戏主循环
while True:
    # 打印游戏地图
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (x, y) == player_pos:
                print('P', end=' ')
            elif (x, y) == box_pos:
                print('B', end=' ')
            elif (x, y) == target_pos:
                print('T', end=' ')
            else:
                print(map[y][x], end=' ')
        print()

    # 获取玩家输入
    move = input("请输入移动方向（w上，s下，a左，d右）：")

    # 根据玩家输入移动玩家
    if move == 'w' and map[player_pos[1]-1][player_pos[0]] != 1:
        player_pos = (player_pos[0], player_pos[1]-1)
    elif move == 's' and map[player_pos[1]+1][player_pos[0]] != 1:
        player_pos = (player_pos[0], player_pos[1]+1)
    elif move == 'a' and map[player_pos[1]][player_pos[0]-1] != 1:
        player_pos = (player_pos[0]-1, player_pos[1])
    elif move == 'd' and map[player_pos[1]][player_pos[0]+1] != 1:
        player_pos = (player_pos[0]+1, player_pos[1])

    # 检查玩家是否推动了箱子
    if player_pos == box_pos:
        if move == 'w' and map[box_pos[1]-1][box_pos[0]] != 1:
            box_pos = (box_pos[0], box_pos[1]-1)
        elif move == 's' and map[box_pos[1]+1][box_pos[0]] != 1:
            box_pos = (box_pos[0], box_pos[1]+1)
        elif move == 'a' and map[box_pos[1]][box_pos[0]-1] != 1:
            box_pos = (box_pos[0]-1, box_pos[1])
        elif move == 'd' and map[box_pos[1]][box_pos[0]+1] != 1:
            box_pos = (box_pos[0]+1, box_pos[1])

    # 检查是否完成了游戏
    if box_pos == target_pos:
        print("恭喜你，完成了游戏！")
        break
