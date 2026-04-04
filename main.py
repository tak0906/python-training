from game import NumberGame

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