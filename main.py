#main


# 13行24列の二次元配列を初期化
rows, cols = 13, 24
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

#重複なくタグを読み込む．
Check=[]#確認用リスト
for num in range(0,rows,1):
        while True:
            check=input()
            flag = True
            for num2 in range(0,rows,1):
                if check==matrix[num2]:
                    flag= False
            if flag==True:
                 matrix[num]=check
                 break


print("")


#置き換え
if "E280F3372000F00007F59EC3" in matrix:
    matrix[matrix.index("E280F3372000F00007F59EC3")]="9M"
if "E280F3372000F00007F5885C" in matrix:
    matrix[matrix.index("E280F3372000F00007F5885C")]="9P"
if "E280F3372000F00007F5996F" in matrix:
    matrix[matrix.index("E280F3372000F00007F5996F")]="9S"

if "E280F3372000F00007F563A8" in matrix:
    matrix[matrix.index("E280F3372000F00007F563A8")]="1M"
if "E280F3372000F00007F58EB2" in matrix:
    matrix[matrix.index("E280F3372000F00007F58EB2")]="1P"
if "E280F3372000F00007F55C05" in matrix:
    matrix[matrix.index("E280F3372000F00007F55C05")]="1S"


if "E280F3372000F00007F58098" in matrix:
    matrix[matrix.index("E280F3372000F00007F58098")]="East"
if "E280F3372000F00007F572A3" in matrix:
    matrix[matrix.index("E280F3372000F00007F572A3")]="South"
if "E280F3372000F00007F594B3" in matrix:
    matrix[matrix.index("E280F3372000F00007F594B3")]="West"
if "E280F3372000F00007F59B40" in matrix:
    matrix[matrix.index("E280F3372000F00007F59B40")]="North"


if "E280F3372000F00007F5544F" in matrix:
    matrix[matrix.index("E280F3372000F00007F5544F")]="White"
if "E280F3372000F00007F5A143" in matrix:
    matrix[matrix.index("E280F3372000F00007F5A143")]="Red"
if "E280F3372000F00007F5A52D" in matrix:
    matrix[matrix.index("E280F3372000F00007F5A52D")]="Green"


for num in range(0,rows,1):
    print(matrix[num])

print("1")