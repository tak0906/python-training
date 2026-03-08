import random
def get_hint(sa,direction):
    if 1<=sa<=10:
        return f"だいぶ近い、、!1~10{direction}するんやで！"
    elif 11<=sa<=50:
        return f"ちょっと惜しい、、10~50{direction}してや～"
    elif 101<=sa<=200:
        return f"100~200{direction}せなかんで~~まだ遠すぎて草"
    elif 51<=sa<=100:
        return f"50~100{direction}せなかんな~まだ遠いで~~"
    else:
        return f"200以上{direction}して~遠すぎてワロタ"

def play_game():
    seikai=random.randint(1,319)
    max_try=15
    for i in range(max_try):
        kaitou=int(input("当たりだと思う数字（1~319）を入力して正解してな～～："))
        sa=abs(kaitou-seikai)
        nokori=(max_try - i - 1)

        if kaitou<seikai:
            direction="でかく"
        else:
            direction="ちっさく"

        if kaitou==seikai:
            print("大当たり~~~~~~~~!!")
            break

        hint=get_hint(sa,direction)
        
        if nokori>0:
            print(f"外れWWあと{nokori}回であててな～ちなみに{hint}")
        else:
            print(f"ざんね~~~~んww正解は{seikai}!")

def main():
    play_game()

if __name__ == "__main__":
    main()
