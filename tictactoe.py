def output(field):
    global x_wins, o_wins, draw
    number_of_X = number_of_O = number_of__ = 0
    x_wins = o_wins = draw = False
    print("---------")
    for i in range(3):
        X_in_line = O_in_line = 0
        print("| ", end='')
        for j in range(3):
            symbol = field[i][j]
            if symbol == "X":
                number_of_X += 1
                X_in_line += 1
            elif symbol == "O":
                number_of_O += 1
                O_in_line += 1
            elif symbol == "_":
                number_of__ += 1
            print(symbol + " ", end='')
        if X_in_line == 3:
            x_wins = True
        if O_in_line == 3:
            o_wins = True
        print("|")
    print("---------")
    if number_of__ == 0:
        draw = True


field = [["_"] * 3 for _ in range(3)]
X_plays = True
output(field)
while not (x_wins or o_wins or draw):
    while True:
        coordinates = input("Enter the coordinates: ").split()
        try:
            y = int(coordinates[0]) - 1
            x = 3 - int(coordinates[1])
        except ValueError:
            print('You should enter numbers!')
        else:
            if x in range(3) and y in range(3):
                if field[x][y] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    field[x][y] = "X" if X_plays else "O"
                    break
            else:
                print("Coordinates should be from 1 to 3!")
    output(field)
    for j in range(3):
        X_in_row = O_in_row = 0
        for i in range(3):
            if field[i][j] == "X":
                X_in_row += 1
            if field[i][j] == "O":
                O_in_row += 1
        if X_in_row == 3:
            x_wins = True
        if O_in_row == 3:
            o_wins = True
    if field[0][0] == field[1][1] == field[2][2] == "X":
        x_wins = True
    if field[0][2] == field[1][1] == field[2][0] == "X":
        x_wins = True
    if field[0][0] == field[1][1] == field[2][2] == "O":
        o_wins = True
    if field[0][2] == field[1][1] == field[2][0] == "O":
        o_wins = True
    X_plays = not X_plays
if x_wins:
    print("X wins")
elif o_wins:
    print("O wins")
elif draw:
    print("Draw")
