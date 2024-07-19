# main

# 計算
from mahjong.hand_calculating.hand import HandCalculator
# 麻雀牌
from mahjong.tile import TilesConverter
# 役, オプションルール
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
# 鳴き
from mahjong.meld import Meld
# 風(場&自)
from mahjong.constants import EAST, SOUTH, WEST, NORTH  # シャンテン数
from mahjong.shanten import Shanten

import socket

shanten = Shanten()
calculator = HandCalculator()

#シャンテン数計算
def Shantensuu(tile):
    # 計算
    res = shanten.calculate_shanten(tile)
    return res

#結果出力
def print_hand_result(hand_result):
    # 翻数, 符数
    print(hand_result.han, hand_result.fu)
    # 点数(ツモアガリの場合[左：親失点, 右:子失点], ロンアガリの場合[左:放銃者失点, 右:0])
    print(hand_result.cost['main'], hand_result.cost['additional'])
    # 役
    print(hand_result.yaku)
    # 符数の詳細

    # 国士無双13面待ちでエラー出ます；；
    #  for fu_item in hand_result.fu_details:
    #       print(fu_item)
    print('')


# ------------リーチを検知------------#

#-------------スマホと通信------------#
# ホスト名を取得、表示
PORT = 5000
host = socket.gethostname()
print(host)

# # ipアドレスを取得、表示
# ip = socket.gethostbyname(host)
# print(ip) 

# #01. Socket Making : socket()
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #02. Address & Port : bind()
# server.bind(("10.0.0.102", PORT))
# #03. Waiting the connection : listen()
# server.listen()
# #04. Getting the socket : accept()
# client, addr = server.accept()

# print("通信成功\n")

#テスト用
# client.sendall(b"reach!\n") #messeage

#-------------スマホと通信------------#

#-------------ゲームを開始------------#
while True:

    #-------------スマホと通信------------#


    #読み込んだRFIDをリーチ棒か確認
    Check = []  # 確認用リスト
    reach_stick = []

    while True:
        check = input()
        if check == "E280F3372000F00007F593BA":
            print("リーチです！！")
            break
            
    # ------------リーチを検知------------#

    #----------リーチしたことを伝える------#
    #05. Data Yaritori : send(), recv()
    #client.sendall(b"reach!\n") #messeage
    #----------リーチしたことを伝える------#


    # 13行24列の二次元配列を初期化
    rows, cols = 14, 24

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # 重複なくタグを読み込む．



    for num in range(0, rows-1, 1):
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

    #pin
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
    #東
    if "E280F3372000F00007F58098" in matrix:
        hand_honors = hand_honors + "1"
    #南
    if "E280F3372000F00007F572A3" in matrix:
        hand_honors = hand_honors + "2"
    #西
    if "E280F3372000F00007F594B3" in matrix:
        hand_honors = hand_honors+"3"
    #北
    if "E280F3372000F00007F59B40" in matrix:
        hand_honors = hand_honors+"4"
    #白1
    if "E280F3372000F00007F5544F" in matrix:
        hand_honors = hand_honors+"5"
    #白2
    if "999900000000000000000000" in matrix:
        hand_honors = hand_honors+"5"
    #發
    if "E280F3372000F00007F5A52D" in matrix:
        hand_honors = hand_honors+"6"
    #中
    if "E280F3372000F00007F5A143" in matrix:
        hand_honors = hand_honors+"7"



    # ------------格納完了------------#

    while True:
        #----------ツモ格納------------#
        reach = []
        while True:
            reach = input()
            if reach not in matrix:
                matrix[rows-1] =  reach
                break
        print("最後の一枚引いたよ")

        #ツモが何かを識別
        #引いた牌の種類を識別するための変数
        type_reach = []

        #man
        if reach == "E280F3372000F00007F563A8":
            type_reach = "man"
            reach = "1"
            hand_man = hand_man + "1"

        if reach == "997800000000000000000000":
            type_reach = "man"
            reach = "2"
            hand_man = hand_man + "2"

        if reach == "E280F3372000F00007F59EC3":
            type_reach = "man"
            reach = "9"
            hand_man = hand_man + "9"
        
        #pin
        if reach == "E280F3372000F00007F58EB2":
            type_reach = "pin"
            reach = "1"
            hand_pin = hand_pin + "1"

        if reach == "E280F3372000F00007F59EC3":
            type_reach = "pin"
            reach = "9"
            hand_pin = hand_pin + "9"

        #sou
        if reach == "E280F3372000F00007F55C05":
            type_reach = "sou"
            reach = "1"
            hand_sou = hand_sou + "1"

        if reach == "E280F3372000F00007F5996F":
            type_reach = "sou"
            reach = "9"
            hand_sou = hand_sou + "9"

        #東
        if reach == "E280F3372000F00007F58098":
            type_reach = "honors"
            reach = "1"
            hand_honors = hand_honors+"1"

        #南
        if reach == "E280F3372000F00007F572A3":
            type_reach = "honors"
            reach = "2"
            hand_honors = hand_honors+"2"

        #西
        if reach == "E280F3372000F00007F594B3":
            type_reach = "honors"
            reach = "3"
            hand_honors = hand_honors+"3"

        #北
        if reach == "E280F3372000F00007F59B40":
            type_reach = "honors"
            reach = "4"
            hand_honors = hand_honors+"4"

        #白1
        if reach == "E280F3372000F00007F58098":
            type_reach = "honors"
            reach = "5"
            hand_honors = hand_honors+"5"

        #白2
        if reach == "999900000000000000000000":
            type_reach = "honors"
            reach = "5"
            hand_honors = hand_honors+"5"

        #發E280F3372000F00007F58098
        if reach == "E280F3372000F00007F5A52D":
            type_reach = "honors"
            reach = "6"
            hand_honors = hand_honors+"6"

        #中
        if reach == "E280F3372000F00007F5A143":
            type_reach = "honors"
            reach = "7"
            hand_honors = hand_honors+"7"

        #----------ツモ格納------------#

        # -----------上がり判定-----------

        # アガリ形(man=マンズ, pin=ピンズ, sou=ソーズ, honors=1:東, 2:南, 3:西, 4:北, 5:白, 6:發, 7:中)
        # 点数計算に使う
        tiles = TilesConverter.string_to_136_array(man=hand_man, pin=hand_pin, sou=hand_sou, honors=hand_honors)

        # 手配（聴牌チェックに使う）
        hand_tiles = TilesConverter.string_to_34_array(man=hand_man, pin=hand_pin, sou=hand_sou, honors=hand_honors)

        # ------------------オプション設定------------------#

        # アガリ牌(上と同じ)
        # ここだけ引数で指定する必要がある
        match type_reach:
            
            #ツモが萬豆の場合
            case "man":
                win_tile = TilesConverter.string_to_136_array(man=reach)[0]
            #ツモが筒子の場合
            case "pin":
                win_tile = TilesConverter.string_to_136_array(pin=reach)[0]
            #ツモが索子の場合
            case "sou":
                win_tile = TilesConverter.string_to_136_array(sou=reach)[0]
            #ツモが字牌の場合
            case "honors":
                win_tile = TilesConverter.string_to_136_array(honors=reach)[0]

        # 鳴き(なし)
        melds = None

        # ドラ(なし)
        dora_indicators = None

        # オプション(ツモを追加,Falseだとロン)
        config = HandConfig(is_tsumo=True)

        # ------------------オプション設定------------------#

        
        shan = Shantensuu(hand_tiles)
        print(shan)

        # ------------------上がれるか判定------------------#
        match shan:
            case -1:
                print("上がりです")

                # 点数計算
                result = calculator.estimate_hand_value(
                    tiles, win_tile, melds, dora_indicators, config)
                print_hand_result(result)
                
                #当たりはいのメッセージを送信
                #client.sendall(b"Hit!\n") #messeage

                print("マンズ："+hand_man)
                print("ピンズ："+hand_pin)
                print("ソーズ："+hand_sou)
                print("honors："+hand_honors)
                print("最後の一枚："+reach)

                break

            case 0:
                print("聴牌です")

                print("マンズ："+hand_man)
                print("ピンズ："+hand_pin)
                print("ソーズ："+hand_sou)
                print("honors："+hand_honors)
                print("最後の一枚："+reach)                

                match type_reach:
                    case "man":
                        hand_man = hand_man[:-1]
                    case "pin":
                        hand_pin = hand_pin[:-1]
                    case "sou":
                        hand_sou = hand_sou[:-1]
                    case "honors":
                        hand_honors = hand_honors[:-1]
                
                print("マンズ："+hand_man)
                print("ピンズ："+hand_pin)
                print("ソーズ："+hand_sou)
                print("honors："+hand_honors)
                print("最後の一枚："+reach)     

                #はずれの場合のメッセージ送信
                #client.sendall(b"Lose!\n") #messeage

        # -----------------上がれるか判定------------------#

        # -----------上がり判定-----------#
    
    #----------継続メッセージを受信-------#
    mess = "1"
    if mess == 0:
        break
    #----------継続メッセージを受信-------#


#client.close()
#server.close()