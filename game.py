# coding:utf-8

from random import randint
name = raw_input('请输入你的名字：')

f = open('E:\\PythonFile\\test\\game.txt')
line = f.readline()
f.close()

scores = {}  # c初始化空字典

for l in line:
    s = l.split()   # 拆分行
    scores[s[0]] = s[1:]  # 第一项作为key 其他为value

score = scores.get(name)

if score is None:
    score = [0, 0, 0]   # 初始化
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times > 0:
    avg_time = float(total_times/game_times)
else:
    avg_time = 0
print "%s你已经玩了%d次,最少%d轮猜出答案,平均%f轮猜出答案"%(name, game_times, min_times, avg_time)
num = randint(1, 100)
times = 0
print '猜猜我想的是多少？'
bingo = False
while bingo is False:
    answer = input()
    if answer < num:
        print '小了'
    if answer > num:
        print '大了'
    if answer == num:
        print'恭喜你，猜对了！！'
        bingo = True

while bingo is True:
    times += 1
    answer = input()
    if answer < num:
        print '小了'
    if answer > num:
        print '大了'
    if answer == num:
        print'恭喜你，猜对了！！'
        bingo = True

if game_times == 0 or game_times < min_times:
    min_times = game_times
total_times += times
game_times += 1
scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for n in score:
    line = n + '' + '' .join(scores[n]) + '\=n'
    result += line
f = open('E:\\PythonFile\\test\\game.txt', 'w')
f.write(result)
f.close()
