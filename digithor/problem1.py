test_case = int(input())
all_game = []

for i in range(test_case):

    input_year = int(input())

    game_count = 0

    for j in range(2020, input_year+1, 4):
        game_count = game_count + 1

    all_game.append(game_count)
    
for item in all_game:
    print(item)
    