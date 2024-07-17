
#計算
from mahjong.hand_calculating.hand import HandCalculator
#麻雀牌
from mahjong.tile import TilesConverter
#役, オプションルール
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
#鳴き
from mahjong.meld import Meld
#風(場&自)
from mahjong.constants import EAST, SOUTH, WEST, NORTH#シャンテン数
from mahjong.shanten import Shanten

#Shanten(シャンテン数計算用クラス)のインスタンスを生成
shanten = Shanten()

#アガリ形(man=マンズ, pin=ピンズ, sou=ソーズ, honors=1:東, 2:南, 3:西, 4:北, 5:白, 6:發, 7:中)
tiles = TilesConverter.string_to_34_array(man='677889', pin='88', sou='456', honors='222')

#計算
result = shanten.calculate_shanten(tiles)

print(1)
print(result)