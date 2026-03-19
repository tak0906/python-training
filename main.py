import random
import json

def load_score():
    try:
        with open("score.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"easy":None,"normal":None,"hard":None}

def save_score(score):
    with open("score.json","w") as f:
        json.dump(score,f,indent = 4)

def get_hint(sa,direction):
    if sa==0:
        return f"正解！"
    elif sa==1:
        return f"ニアピン！もう目前やで!"
    elif 1<sa<=10:
        return f"だいぶ近い、、!1~10{direction}するんやで！"
    elif 11<=sa<=50:
        return f"ちょっと惜しい、、10~50{direction}してや～"
    elif 51<=sa<=100:
        return f"50~100{direction}せなかんな~まだ遠いで~~"    
    elif 101<=sa<=200:
        return f"100~200{direction}せなかんで~~まだ遠すぎて草"
    else:
        return f"200以上{direction}して~遠すぎてワロタ"

def show_score(scores):
    print("\n現在の最短記録")

    for k,v in scores.items():
        if v is None:
            print(f"{k} : 未記録")
        else:
            print(f"{k} : {v}回")

def show_history(history):
    print("\n入力履歴")
    for i, (num, d) in enumerate(history, 1):
        print(f"{i}回目: {num} → {d}")


difficulty = {
    "easy":(100,20),
    "normal":(300,15),
    "hard":(500,10)
}

def play_game(best_scores):

    history = []

    print("==============")
    print("数字当てゲーム")
    print("==============")
    show_score(best_scores)

    while True:
        dif = input("難易度は何にする?(hard/normal/easy):").lower()
        if dif in difficulty:
            break
        print("easy / normal / hard で入力してな!")

    max_num,max_try = difficulty[dif]
    seikai = random.randint(1,max_num)

    for i in range(max_try):

        print("\n--------------------")
        print(f"{i+1}回目の挑戦！")
        print("--------------------")
        
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
        direction="でかく"  if kaitou<seikai else "ちっさく"
        hint=get_hint(sa,direction)
        history.append((kaitou,hint))

        if kaitou==seikai:
            score = i + 1
            print(f"大当たり~~~~~~~~!!今回は{score}回で当てれたな~~!!")
            show_history(history)

            if best_scores[dif] is None or score < best_scores[dif]:
                best_scores[dif] = score
                print("新記録更新やで！！")
                save_score(best_scores)
            
            print(f"今回記録：{score}回")
            print(f"最短記録：{best_scores[dif]}回")
            return best_scores
        
        if nokori>0:
            print(f"外れWWあと{nokori}回であててな～ちなみに{hint}")

        else:
            print(f"ざんね~~~~んww正解は{seikai}!")
            show_history(history)
            return best_scores

def main():

    best_scores = load_score()

    while True:
        
        best_scores = play_game(best_scores)

        ans = input("もう一回遊ぶ？ (y/n): ")
        if ans == "n":
            print("遊んでくれてありがとな～！")
            break

if __name__ == "__main__":
    main()