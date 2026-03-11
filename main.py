import random

def get_hint(sa,direction):
    if 1<=sa<=10:
        return f"だいぶ近い、、!1~10{direction}するんやで！"
    elif 11<=sa<=50:
        return f"ちょっと惜しい、、10~50{direction}してや～"
    elif 51<=sa<=100:
        return f"50~100{direction}せなかんな~まだ遠いで~~"    
    elif 101<=sa<=200:
        return f"100~200{direction}せなかんで~~まだ遠すぎて草"
    else:
        return f"200以上{direction}して~遠すぎてワロタ"

difficulty = {
    "easy":(100,20),
    "normal":(300,15),
    "hard":(500,10)
}

def play_game():
    while True:
        dif = input("数字当てゲーム！難易度は何にする?(hard/normal/easy):")
        if dif in difficulty:
            break
        print("easy / normal / hard で入力してな!")

    max_num,max_try = difficulty[dif]
    seikai = random.randint(1,max_num)

    for i in range(max_try):
        try:
            kaitou = int(input(f"当たりだと思う数字（1~{max_num}）を入力して正解してな～～："))

        except ValueError:
            print("数字を入力してな～～")
            continue

        if kaitou < 1 or kaitou > max_num:
            print(f"1~{max_num}で入力してな～～あと{max_try - i - 1}回やで～")
            continue

        sa=abs(kaitou-seikai)
        nokori= max_try - i - 1

        if kaitou<seikai:
            direction="でかく"
        else:
            direction="ちっさく"

        if kaitou==seikai:
            print(f"大当たり~~~~~~~~!!今回は{i+1}回で当てれたな~~!!")
            break

        hint=get_hint(sa,direction)
        
        if nokori>0:
            print(f"外れWWあと{nokori}回であててな～ちなみに{hint}")
        else:
            print(f"ざんね~~~~んww正解は{seikai}!")

def main():
    while True:
        play_game()
        ans = input("もう一回遊ぶ？ (y/n): ")
        if ans == "n":
            break
    

if __name__ == "__main__":
    main()



import random

def get_hint(sa,direction):
    if 1<=sa<=10:
        return f"だいぶ近い、、!1~10{direction}するんやで！"
    elif 11<=sa<=50:
        return f"ちょっと惜しい、、10~50{direction}してや～"
    elif 51<=sa<=100:
        return f"50~100{direction}せなかんな~まだ遠いで~~"    
    elif 101<=sa<=200:
        return f"100~200{direction}せなかんで~~まだ遠すぎて草"
    else:
        return f"200以上{direction}して~遠すぎてワロタ"

def difficult(dif):
    if dif == "hard":
        return random.randint(1,500),500
    elif dif == "normal":
        return random.randint(1,300),300
    else:
        return random.randint(1,100),100

def play_game():
    while True:
        dif = input("数字当てゲーム！難易度は何にする?(hard/normal/easy):")
        if dif in ("easy","normal","hard"):
            break
        print("easy / normal / hard で入力してな!")

    seikai,max_num = difficult(dif)
    max_try=15

    for i in range(max_try):
        try:
            kaitou = int(input(f"当たりだと思う数字（1~{max_num}）を入力して正解してな～～："))

        except ValueError:
            print("数字を入力してな～～")
            continue

        if kaitou < 1 or kaitou > max_num:
            print(f"1~{max_num}で入力してな～～あと{max_try - i - 1}回やで～")
            continue

        sa=abs(kaitou-seikai)
        nokori= max_try - i - 1

        if kaitou<seikai:
            direction="でかく"
        else:
            direction="ちっさく"

        if kaitou==seikai:
            print(f"大当たり~~~~~~~~!!今回は{i+1}回で当てれたな~~!!")
            break

        hint=get_hint(sa,direction)
        
        if nokori>0:
            print(f"外れWWあと{nokori}回であててな～ちなみに{hint}")
        else:
            print(f"ざんね~~~~んww正解は{seikai}!")

def main():
    while True:
        play_game()
        ans = input("もう一回遊ぶ？ (y/n): ")
        if ans == "n":
            break
    

if __name__ == "__main__":
    main()
