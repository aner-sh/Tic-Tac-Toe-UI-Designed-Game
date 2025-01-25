import turtle

my = turtle.Turtle()
my.speed(10)

BOARD_SIZE = 200
game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
moves_counter = 0
is_x_turn = True
is_winner = False


def board():
    my.clear()
    my.penup()
    my.goto(0, BOARD_SIZE)
    my.pendown()
    my.color("blue violet")
    my.write("Let's Play Tic-Tac-Tow", move=False, align="CENTER", font=("cooper black", 30, "bold"))

    my.penup()
    my.goto(-BOARD_SIZE / 2, -BOARD_SIZE / 6)
    my.pendown()
    my.pensize(4)
    my.pencolor("grey")
    my.setheading(90)
    my.forward(BOARD_SIZE / 2)
    my.setheading(0)
    my.forward(BOARD_SIZE)
    my.setheading(270)
    my.forward(BOARD_SIZE)
    my.setheading(180)
    my.forward(BOARD_SIZE)
    my.setheading(90)
    my.forward(BOARD_SIZE - BOARD_SIZE / 3)
    my.setheading(0)
    my.forward(BOARD_SIZE)
    my.setheading(270)
    my.forward(BOARD_SIZE / 3)
    my.setheading(180)
    my.forward(BOARD_SIZE)
    my.penup()
    my.goto(-BOARD_SIZE / 6, BOARD_SIZE / 3)
    my.pendown()
    my.setheading(270)
    my.forward(BOARD_SIZE)
    my.setheading(0)
    my.forward(BOARD_SIZE / 3)
    my.setheading(90)
    my.forward(BOARD_SIZE)

def draw_x(row, col):
    global moves_counter
    x = -BOARD_SIZE / 2 + (col - 1) * BOARD_SIZE / 3
    y = BOARD_SIZE / 2 - (row - 1) * BOARD_SIZE / 3 - BOARD_SIZE / 6
    my.penup()
    my.goto(x, y)
    my.pendown()
    my.pencolor("red")
    my.pensize(4)
    my.speed(100)
    my.goto(x + BOARD_SIZE / 3, y - BOARD_SIZE / 3)
    my.penup()
    my.goto(x + BOARD_SIZE / 3, y)
    my.pendown()
    my.goto(x, y - BOARD_SIZE / 3)
    game_board[row - 1][col - 1] = 'X'
    moves_counter += 1


def draw_o(row, col):
    global moves_counter
    x = -BOARD_SIZE / 2 + (col - 1) * BOARD_SIZE / 3 + BOARD_SIZE / 3
    y = BOARD_SIZE / 2 - (row - 1) * BOARD_SIZE / 3 - BOARD_SIZE / 3
    my.penup()
    my.goto(x, y)
    my.pendown()
    my.pencolor("blue")
    my.pensize(4)
    my.speed(100)
    my.circle(BOARD_SIZE / 6)
    game_board[row - 1][col - 1] = 'O'
    moves_counter += 1


def check_winner():
    global is_winner

    if game_board[0] == ["X", "X", "X"] or game_board[0] == ["O", "O", "O"]:
        is_winner = True
    elif game_board[1] == ["X", "X", "X"] or game_board[1] == ["O", "O", "O"]:
        is_winner = True
    elif game_board[2] == ["X", "X", "X"] or game_board[2] == ["O", "O", "O"]:

        is_winner = True
    elif game_board[0][0] == 'X' and game_board[1][0] == 'X' and game_board[2][0] == 'X':
        is_winner = True
    elif game_board[0][1] == 'X' and game_board[1][1] == 'X' and game_board[2][1] == 'X':
        is_winner = True
    elif game_board[0][2] == 'X' and game_board[1][2] == "X" and game_board[2][2] == 'X':
        is_winner = True
    elif game_board[0][0] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X':
        is_winner = True
    elif game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X':
        is_winner = True

    elif game_board[0][0] == 'O' and game_board[1][0] == 'O' and game_board[2][0] == 'O':
        is_winner = True
    elif game_board[0][1] == 'O' and game_board[1][1] == 'O' and game_board[2][1] == 'O':
        is_winner = True
    elif game_board[0][2] == 'O' and game_board[1][2] == "O" and game_board[2][2] == 'O':
        is_winner = True
    elif game_board[0][0] == 'O' and game_board[1][1] == 'O' and game_board[2][2] == 'O':
        is_winner = True
    elif game_board[0][2] == 'O' and game_board[1][1] == 'O' and game_board[2][0] == 'O':
        is_winner = True

    return is_winner


def play_turn(y, x):
    global moves_counter
    global game_board
    global is_x_turn
    global is_winner


    if not is_winner and moves_counter != 9:
        row = 0
        col = 0
        if 0 < x < BOARD_SIZE / 3:
            row = 1
        elif -BOARD_SIZE / 3 < x < 0:
            row = 2
        elif -BOARD_SIZE / 3 * 2 < x < -BOARD_SIZE / 3:
            row = 3

        if -BOARD_SIZE / 2 < y < -BOARD_SIZE / 6:
            col = 1
        elif -BOARD_SIZE / 6 < y < BOARD_SIZE / 6:
            col = 2
        elif BOARD_SIZE / 6 < y < BOARD_SIZE / 2:
            col = 3

        if not is_winner:
            if row != 0 and col != 0 and game_board[row - 1][col - 1] == " ":
                if is_x_turn:
                    my.penup()
                    my.goto(0, BOARD_SIZE - 40)
                    my.pendown()
                    my.speed(100)
                    my.color("WHITE")
                    my.write("█████████████", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                    my.penup()
                    my.goto(0, BOARD_SIZE - 40)
                    my.pendown()
                    my.color("BLUE")
                    my.write("O's TURN", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                    draw_x(row, col)

                else:
                    my.penup()
                    my.goto(0, BOARD_SIZE - 40)
                    my.pendown()
                    my.speed(100)
                    my.color("WHITE")
                    my.write("█████████████", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                    my.penup()
                    my.goto(0, BOARD_SIZE - 40)
                    my.pendown()
                    my.color("RED")
                    my.write("X's TURN", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                    draw_o(row, col)

                is_x_turn = not is_x_turn

                is_winner = check_winner()
                if is_winner and moves_counter % 2 == 0:
                    print("CONGRATS! O IS THE WINNER!")
                    my.penup()
                    my.goto(0, BOARD_SIZE - 40)
                    my.pendown()
                    my.speed(100)
                    my.color("WHITE")
                    my.write("█████████████", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                    my.penup()
                    my.goto(0, BOARD_SIZE - 40)
                    my.pendown()
                    my.speed(100)
                    my.color("orange")
                    my.write("O WINS!", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]



                if is_winner and moves_counter % 2 != 0:
                    print("CONGRATS! X IS THE WINNER!")
                    my.penup()
                    my.goto(0, BOARD_SIZE - 40)
                    my.pendown()
                    my.speed(100)
                    my.color("WHITE")
                    my.write("█████████████", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                    my.penup()
                    my.goto(0, BOARD_SIZE - 40)
                    my.pendown()
                    my.speed(100)
                    my.color("orange")
                    my.write("X WINS!", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]



            else:
                my.penup()
                my.goto(0, BOARD_SIZE - 40)
                my.pendown()
                my.color("WHITE")
                my.write("█████████████", move=False, align="CENTER", font=("Verdana", 20, "bold"))
                print("Illegal move")
                my.penup()
                my.goto(0, BOARD_SIZE - 40)
                my.pendown()
                my.color("RED")
                my.write("illeagal move", move=False, align="CENTER", font=("Verdana", 20, "bold"))


        is_winner = check_winner()
        if is_winner == False and moves_counter == 9:
            print("DRAW. NO WINNER")
            my.penup()
            my.goto(0, BOARD_SIZE - 40)
            my.pendown()
            my.speed(100)
            my.color("white")
            my.write("█████████████", move=False, align="CENTER", font=("Verdana", 20, "bold"))
            my.penup()
            my.goto(0, BOARD_SIZE - 40)
            my.pendown()
            my.speed(100)
            my.color("DARK BLUE")
            my.write("NO WINNER", move=False, align="CENTER", font=("Verdana", 20, "bold"))
            game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]



def main():
    board()
    tw = turtle.Screen()
    tw.onclick(play_turn)


main()

turtle.mainloop()
