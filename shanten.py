
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

# 各インスタンスを生成
shanten = Shanten()
calculator = HandCalculator()


def Shantensuu(tile):

    # 計算
    res = shanten.calculate_shanten(tile)
    return res


# 結果出力用
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


# main

# -----------------手配管理------------------------#

# -----------------手配管理------------------------#

hand_man = '91'
hand_pin = '19'
hand_sou = '19'
hand_honors = '12345677'


tumo = ''


# 手配の情報を整える
# アガリ形(man=マンズ, pin=ピンズ, sou=ソーズ, honors=1:東, 2:南, 3:西, 4:北, 5:白, 6:發, 7:中)
# 点数計算に使う
tiles = TilesConverter.string_to_136_array(
    hand_man, hand_pin, hand_sou, hand_honors)

# 手配（聴牌チェックに使う）
hand_tiles = TilesConverter.string_to_34_array(
    hand_man, hand_pin, hand_sou, hand_honors)

# ------------------オプション設定------------------#

# アガリ牌(上と同じ)
# ここだけ引数で指定する必要がある
win_tile = TilesConverter.string_to_136_array(honors='7')[0]

# 鳴き(なし)
melds = None

# ドラ(なし)
dora_indicators = None

# オプション(ツモを追加,Falseだとロン)
config = HandConfig(is_tsumo=True)

# ------------------オプション設定------------------#


# ------------------上がれるか判定------------------#
shan = Shantensuu(hand_tiles)
print(shan)

match shan:
    case -1:
        print("上がりです")

        # 点数計算
        result = calculator.estimate_hand_value(
            tiles, win_tile, melds, dora_indicators, config)
        print_hand_result(result)

    case 0:
        print("聴牌です")

# -----------------上がれるか判定------------------#
