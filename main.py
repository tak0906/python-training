import random
import json
from datetime import datetime

class NumberGame:

    def __init__(self):
        self.best_scores = self.load_score()
        self.difficulty = {
            "easy":(100,20),
            "normal":(300,15),
            "hard":(500,10)
            }

    def load_score(self):
        try:
            with open("score.json","r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"easy":[],"normal":[],"hard":[]}

    def save_score(self):
        with open("score.json","w") as f:
            json.dump(self.best_scores,f,indent = 4)

    def get_hint(self,sa,direction):
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

    def show_score(self):
        print("\nランキング")
        for k, v in self.best_scores.items():
            print(f"\n【{k}】")
            if not v:
                print("未記録")
            else:
                for i, record in enumerate(v, 1):
                    print(f"{i}位 {record['name']} : {record['score']}回")

    def show_history(self,history):
        print("\n入力履歴")
        for i, (num, d) in enumerate(history, 1):
            print(f"{i}回目: {num} → {d}")

    def play_game(self):
        
        history = []

        cmd = input("コマンド (Enterで開始 / rでリセット): ")
        if cmd == "r":
            self.best_scores = {"easy": [], "normal": [], "hard": []}
            self.save_score()
            print("ランキングリセットしたで！")
         
        print("==============")
        print("数字当てゲーム")
        print("==============")
        self.show_score()
    
        while True:
            dif = input("難易度は何にする?(hard/normal/easy):").lower()
            if dif in self.difficulty:
                break
            print("easy / normal / hard で入力してな!")

        while True:
            name = input("名前を入力してな!:").strip()
            if name:
                break
            print("ちゃんと名前いれてな～")

  
        max_num,max_try = self.difficulty[dif]
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
            hint=self.get_hint(sa,direction)
            history.append((kaitou,hint))
         
            if kaitou==seikai:
                score = i + 1
                print(f"大当たり~~~~~~~~!!今回は{score}回で当てれたな~~!!")
                self.show_history(history)

                new_record = {"name": name, "score": score,"date": datetime.now().strftime("%Y-%m-%d %H:%M")}
                old_scores = self.best_scores[dif].copy()

                before_len = len(self.best_scores[dif])

                self.best_scores[dif].append(new_record)
                self.best_scores[dif].sort(key=lambda x: x["score"])
                self.best_scores[dif] = self.best_scores[dif][:3]

                if new_record in self.best_scores[dif]:
                    print("新記録更新やで！！")
                    self.save_score()

                print(f"今回記録：{score}回")
                medals = ["🥇", "🥈", "🥉"]
                for i, record in enumerate(self.best_scores[dif], 1):
                    mark = medals[i-1] if i <= 3 else f"{i}位"
                    print(f"{mark} {record['name']} : {record['score']}回 ({record['date']})")
                return
        
            if nokori>0:
                print(f"外れWWあと{nokori}回であててな～ちなみに{hint}")
            
            else:
                print(f"ざんね~~~~んww正解は{seikai}!")
                self.show_history(history)
                return    

def main():
    game = NumberGame()

    while True:
        game.play_game()

        ans = input("もう一回遊ぶ？ (y/n): ")
        if ans == "n":
            print("遊んでくれてありがとな～！")
            break

if __name__ == "__main__":
    main()