def game_time(games_played,amount_played):
    print(f"you have played {games_played} games.")
    print(f"you have been playing games for {amount_played} years.")
    print(f"That's {round(games_played/amount_played)} games per year.")

print("hi, I am here to determine if you play too many games.")
input_1 = int(input("Please input how many games you have played\n>"))
input_2 = int(input("please input how long you have been playing games for\n>"))
game_time(input_1,input_2)
