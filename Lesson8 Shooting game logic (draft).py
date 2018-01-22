播放音效

生成角色

counter = 0

while true：
    if 玩家按下退出按键：
        break

    counter += 1

    if counter==50:
        生成小飞机

    移动小飞机
    刷新屏幕

    角色位置与玩家鼠标位置同步
    刷新屏幕

    if 角色触碰到小飞机:
        播放爆炸音效
        背景音乐停止
        print（“game over”）
