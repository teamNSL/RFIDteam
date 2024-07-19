# main


# ------------リーチを検知------------#



# ------------リーチを検知------------#


# 13行24列の二次元配列を初期化
rows, cols = 14, 24
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# 重複なくタグを読み込む．
Check = []  # 確認用リスト
for num in range(0, rows, 1):
    while True:
        check = input()
        flag = True
        for num2 in range(0, rows, 1):
            if check == matrix[num2]:
                flag = False
        if flag == True:
            matrix[num] = check
            break

print("リーチ目はすべて読んだよ")
# リーチ検知
reach = []
while True:
    reach = input()
    if reach not in matrix:
        break
print("最後の一枚引いたよ")

# 手牌を書くリストに格納
hand_man = ''
hand_pin = ''
hand_sou = ''
hand_honors = ''

# --------手牌追加--------#
# man
if "E280F3372000F00007F563A8" in matrix:
    hand_man = hand_man + "1"
if "E280F3372000F00007F59EC3" in matrix:
    hand_man = hand_man + '9'

if "E280F3372000F00007F58EB2" in matrix:
    hand_pin = hand_pin + "1"
if "E280F3372000F00007F5885C" in matrix:
    hand_pin = hand_pin+"9"

# sou
if "E280F3372000F00007F55C05" in matrix:
    hand_sou = hand_sou + "1"
if "E280F3372000F00007F5996F" in matrix:
    hand_sou = hand_sou+"9"

# honors
if "E280F3372000F00007F58098" in matrix:
    hand_honors = hand_honors + "1"
if "E280F3372000F00007F572A3" in matrix:
    hand_honors = hand_honors + "2"
if "E280F3372000F00007F594B3" in matrix:
    hand_honors = hand_honors+"3"
if "E280F3372000F00007F59B40" in matrix:
    hand_honors = hand_honors+"4"

if "E280F3372000F00007F5544F" in matrix:
    hand_honors = hand_honors+"5"
if "E280F3372000F00007F5A52D" in matrix:
    hand_honors = hand_honors+"6"
if "E280F3372000F00007F5A143" in matrix:
    hand_honors = hand_honors+"7"

# ------------格納完了------------#


#------------上がり判定-----------#


matrix[13] = reach

print("マンズ："+hand_man)
print("ピンズ："+hand_pin)
print("ソーズ："+hand_sou)
print("honors："+hand_honors)
print("最後の一枚："+reach)
