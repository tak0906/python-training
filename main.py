name=input("名前を入力してください：")
age=input("年齢を入力してください：")
print("こんにちは"+name+"!")
print("来年で"+str(int(age)+1)+"歳ですね!")

import random
answer=random.randint(1,10)
guess=int(input("正解だと思う数字(1~10))を入力してください："))
if guess==answer:
    print("正解！")
else:
    print("不正解!正解は", answer)


import random
ooatari=random.randint(1,319)
correct=False

for i in range(10):
    kaitensu=input("当たりだと思う数字を1~319の間で入力してください：")
    if kaitensu==ooatari:
        print("大当たり~~~~~~!!")
        correct=True
        break
    else:print("外れW")
if not correct:
    print("ざんね~~~~~~~んww大当たりは",ooatari)

import random
seikai=random.randint(1,319)
correct=False

for i in range(1,20):
    kaitou=int(input("当たりだと思う数字（1~319）を入力してください："))
    if kaitou==seikai:
        print("大当たり~~~~~~~~!!")
        correct=True
        break
    elif 51<=(abs(int(kaitou)-int(seikai)))<=100:
        print("外れwあと"+str(20-i)+"回であててな～（50~100離れてる~まだ遠いで～～）")
    elif 11<=(abs(int(kaitou)-int(seikai)))<=50:
        print("外れwあと"+str(20-i)+"回であててな～（10~50離れや、、ちょっと惜しいあぶない)")
    elif 1<=(abs(int(kaitou)-int(seikai)))<=10:
        print("外れwあと"+str(20-i)+"回であててな～（だいぶ近い、、！)")
    elif 101<=(abs(int(kaitou)-int(seikai)))<=200:
        print("外れwwあと"+str(20-i)+"回であててな～（100~200離れてる~~まだ遠すぎて草）")
    elif 200<(abs(int(kaitou)-int(seikai))):
        print("外れWWあと"+str(20-i)+"回であててな～（200以上離れてんで~~遠すぎてワロタ）")
if not correct:print("ざんね~~~~んww正解は",seikai)

import random
atari=random.randint(1,319)
correct=False

while True:
    kaiten=input("当たりだと思う数字（1~319）を入力してください")
    if atari==kaiten:
         print("大当たり~~~~~~~!!!")
         correct=True
         break
    else:print("外れw")
