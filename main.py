

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
seikai=random.randint(1,319)
correct=False

for i in range(14):
    kaitou=int(input("当たりだと思う数字（1~319）を入力して正解してな～～："))
    sa=abs(kaitou-seikai)
    nokori=(13-i)

    if kaitou==seikai:
        print("大当たり~~~~~~~~!!")
        correct=True
        break
    elif 51<=sa<=100 and kaitou<=seikai:
        hint="50~100でかくせなかんな~まだ遠いで~~"
    elif 51<=sa<=100 and seikai<=kaitou:
        hint="50~100ちっさくせなかんな~まだ遠いで～～"
    elif 11<=sa<=50 and kaitou<=seikai:
        hint="ちょっと惜しい、、10~50でかくしてや～"
    elif 11<=sa<=50 and seikai<=kaitou:
        hint="ちょっと惜しい、、10~50ちっさくしてや～"
    elif 1<=sa<=10 and kaitou<=seikai:
        hint="だいぶ近い、、!1~10でかくするんやで！"
    elif 1<=sa<=10 and seikai<=kaitou:
        hint="だいぶ近い、、!1~10ちっさくするんや！"
    elif 101<=sa<=200 and kaitou<=seikai:
        hint="100~200でかくせなかんで~~まだ遠すぎて草"
    elif 101<=sa<=200 and seikai<=kaitou:
        hint="100~200ちっさくせなかんで~~まだ遠すぎて草"
    elif 200<sa and kaitou<=seikai:
        hint="200以上でかくして~遠すぎてワロタ"
    elif 200<sa and seikai<=kaitou:
        hint="200以上ちっさくして~遠すぎてワロタ"
    print(f"外れWWあと{nokori}回であててな～ちなみに{hint}")
    
    if nokori==0:print(f"ざんね~~~~んww正解は{seikai}")


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

import random
seikai=random.randint(1,319)

for i in range(15):
    kaitou=int(input("当たりだと思う数字（1~319）を入力して正解してな～～："))
    sa=abs(kaitou-seikai)
    nokori=(14-i)

    if kaitou<seikai:
        direction="でかく"
    else:
        direction="ちっさく"

    if kaitou==seikai:
        print("大当たり~~~~~~~~!!")
        break
    elif 51<=sa<=100:
        hint=(f"50~100{direction}せなかんな~まだ遠いで~~")
    elif 11<=sa<=50:
        hint=(f"ちょっと惜しい、、10~50{direction}してや～")
    elif 1<=sa<=10:
        hint=(f"だいぶ近い、、!1~10{direction}するんやで！")
    elif 101<=sa<=200:
        hint=(f"100~200{direction}せなかんで~~まだ遠すぎて草")
    elif 200<sa:
        hint=(f"200以上{direction}して~遠すぎてワロタ")
    
    if nokori>0:
        print(f"外れWWあと{nokori}回であててな～ちなみに{hint}")
    else:
        print(f"ざんね~~~~んww正解は{seikai}!")
