from tkinter import *
import pygame
import time
import subprocess

# global variables

turn = "O"
end_game = False
game_win_condition = True
clicks = 0

# initializing pygame sound

pygame.mixer.init()

# game board

game_board = {1: " ", 2: " ", 3: " ",
              4: " ", 5: " ", 6: " ",
              7: " ", 8: " ", 9: " "}


# defining functions

def set_total_games():
    fs = open("Player_vs_Computer_score.txt", "r")
    w = fs.readlines()
    x = w[0]  # index of line.
    y = x.split("-")
    y[-1] = f"{int(y[-1]) + 1}\n"
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Computer_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 0:  # line to be replaces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def set_total_player_wins():
    fs = open("Player_vs_Computer_score.txt", "r")
    w = fs.readlines()
    x = w[1]  # index of line.
    y = x.split("-")
    y[-1] = f"{int(y[-1]) + 1}\n"
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Computer_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 1:  # line to be replaces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def set_total_computer_wins():
    fs = open("Player_vs_Computer_score.txt", "r")
    w = fs.readlines()
    x = w[2]  # index of line.
    y = x.split("-")
    y[-1] = f"{int(y[-1]) + 1}\n"
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Computer_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 2:  # line to be replaces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def set_total_tied():
    fs = open("Player_vs_Computer_score.txt", "r")
    w = fs.readlines()
    x = w[3]  # index of line.
    y = x.split("-")
    y[-1] = f"{int(y[-1]) + 1}\n"
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Computer_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 3:  # line to be replaces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def set_player_win():
    fs = open("Player_vs_Computer_score.txt", "r")
    w = fs.readlines()
    x = w[5]  # index of line.
    y = x.split("-")
    y[-1] = f"{int(y[-1]) + 1}\n"
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Computer_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 5:  # line to be replaces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def set_computer_win():
    fs = open("Player_vs_Computer_score.txt", "r")
    w = fs.readlines()
    x = w[6]  # index of line.
    y = x.split("-")
    y[-1] = f"{int(y[-1]) + 1}\n"
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Computer_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 6:  # line to be replaces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def set_tied():
    fs = open("Player_vs_Computer_score.txt", "r")
    w = fs.readlines()
    x = w[7]  # index of line.
    y = x.split("-")
    y[-1] = f"{int(y[-1]) + 1}"
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Computer_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 7:  # line to be replaces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def reset_score_player():
    file = open("Player_vs_Player_score.txt", "r")

    w = file.readlines()
    x = w[0]
    y = x.split("-")
    y[-1] = '0\n'
    z = "-".join(y)

    b = w[1]
    c = b.split("-")
    c[-1] = '0\n'
    d = "-".join(c)

    f = w[2]
    g = f.split("-")
    g[-1] = '0'
    h = "-".join(g)

    file.close()

    file = open("Player_vs_Player_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 0:
            file.writelines(z)
        elif i == 1:
            file.writelines(d)
        elif i == 2:
            file.writelines(h)
        else:
            file.writelines(line)
    file.close()


def reset_score_computer():
    file = open("Player_vs_Computer_score.txt", "r")

    w = file.readlines()
    x = w[5]
    y = x.split("-")
    y[-1] = '0\n'
    z = "-".join(y)

    b = w[6]
    c = b.split("-")
    c[-1] = '0\n'
    d = "-".join(c)

    f = w[7]
    g = f.split("-")
    g[-1] = '0'
    h = "-".join(g)

    file.close()

    file = open("Player_vs_Computer_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 5:
            file.writelines(z)
        elif i == 6:
            file.writelines(d)
        elif i == 7:
            file.writelines(h)
        else:
            file.writelines(line)
    file.close()

    reset_score_player()

    global Computer_root
    Computer_root.destroy()
    Computer_root.quit()


def computer_playing():
    bestScore = -100
    bestPosition = 0
    for key in game_board.keys():
        if game_board[key] == " ":
            game_board[key] = "X"
            score = minimax(game_board, False)
            game_board[key] = " "
            if score > bestScore:
                bestScore = score
                bestPosition = key
    game_board[bestPosition] = "X"


def minimax(game_board, ismaximizing):
    if check_win("O"):
        return -1
    elif check_win("X"):
        return 1
    elif check_draw():
        return 0
    elif ismaximizing:
        bestScore = -100
        for key in game_board.keys():
            if game_board[key] == " ":
                game_board[key] = "X"
                score = minimax(game_board, False)
                game_board[key] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 100
        for key in game_board.keys():
            if game_board[key] == " ":
                game_board[key] = "O"
                score = minimax(game_board, True)
                game_board[key] = " "
                if score < bestScore:
                    bestScore = score
        return bestScore


def toplevel_window_win_message(player):
    global tp
    tp = Toplevel(Computer_root)
    tp_width = 240
    tp_height = 190
    tp.configure(borderwidth=5, bg="#567999")
    window_x = Computer_root.winfo_x()
    window_y = Computer_root.winfo_y()
    center_x = int(window_x + (tp_width / 4.2))
    center_y = int(window_y + (tp_height / 1.3))
    tp.geometry(f'{tp_width}x{tp_height}+{center_x}+{center_y}')
    tp.maxsize(tp_width, tp_height)
    tp.minsize(tp_width, tp_height)
    if game_win_condition and player == "X":
        global win_message_label
        win_message_label = Label(tp, text="You lose", font="Arial 15 bold ", bg="#567999", fg="white")
        win_message_label.pack(padx=15, pady=45)
    elif game_win_condition and player == "O":
        win_message_label = Label(tp, text="You Win", font="Arial 15 bold ", bg="#567999", fg="white")
        win_message_label.pack(padx=15, pady=45)
    else:
        win_message_label = Label(tp, text="The game is a draw", font="Arial 15 bold ", bg="#567999", fg="white")
        win_message_label.pack(padx=15, pady=45)
    ok_button_frame = Frame(tp, borderwidth=1, bg="black")
    ok_button_frame.pack(padx=int((tp_width / 2) - 30), pady=int(tp_height - 190))
    ok_button = Button(ok_button_frame, text="OK", font="Arial 12", relief="raised", width=4, height=1, padx=10,
                       command=call_two_functions)
    ok_button.pack()
    tp.protocol("WM_DELETE_WINDOW", call_two_functions)
    tp.mainloop()


def call_two_functions():
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    tp.destroy()
    tp.quit()


def back_button():
    Computer_root.destroy()
    Computer_root.quit()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'First_window.py'])


def restart_button_function():
    global frame12
    frame12 = Frame(Computer_root, bg="black", borderwidth=2)
    frame12.grid(pady=14)

    global restart_button
    restart_button = Button(frame12, relief="raised", height=2, width=12, borderwidth=1, text="Restart Game",
                            font="Arial 15", command=restart_game)
    restart_button.pack()


def restart_game():
    global end_game
    for i in game_board.keys():
        game_board[i] = " "
    for i in buttons:
        i["text"] = " "
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    restart_button.destroy()
    frame12.destroy()
    end_game = False


def check_draw():
    global game_win_condition
    for i in game_board.keys():
        if game_board[i] == " ":
            return False
    game_win_condition = False
    return True


def check_win(player):
    global game_win_condition
    if game_board[1] == game_board[2] == game_board[3] and game_board[3] == player:
        game_win_condition = True
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[7] == player:
        game_win_condition = True
        return True
    elif game_board[1] == game_board[5] == game_board[9] and game_board[9] == player:
        game_win_condition = True
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[8] == player:
        game_win_condition = True
        return True
    elif game_board[3] == game_board[6] == game_board[9] and game_board[9] == player:
        game_win_condition = True
        return True
    elif game_board[4] == game_board[5] == game_board[6] and game_board[6] == player:
        game_win_condition = True
        return True
    elif game_board[7] == game_board[8] == game_board[9] and game_board[9] == player:
        game_win_condition = True
        return True
    elif game_board[3] == game_board[5] == game_board[7] and game_board[7] == player:
        game_win_condition = True
        return True
    else:
        return False


def click(event):
    global turn, end_game, clicks
    clicks += 1
    if end_game:
        return
    else:
        button = event.widget

        # determining the position of the button clicked

        buttonlabel = str(button)
        buttonposition = buttonlabel[-9]
        if buttonposition == "e":
            buttonposition = 1
        else:
            buttonposition = int(buttonposition)

        # get input from the user , play the click sound

        if game_board[buttonposition] == " ":
            if turn == "O":
                game_board[buttonposition] = "O"
                pygame.mixer.music.load("alu_sound.mp3")
                pygame.mixer.music.play()
                button["text"] = "O"

                # check win

                if check_win(turn):
                    # global Player
                    # Player += 1
                    set_player_win()
                    set_total_games()
                    set_total_player_wins()
                    end_game = True
                    pygame.mixer.music.load("Win windows sound.mp3")
                    pygame.mixer.music.play()
                    toplevel_window_win_message(turn)
                    restart_button_function()

                # check draw

                elif check_draw():
                    # global Tied
                    # Tied += 1
                    set_tied()
                    set_total_games()
                    set_total_tied()
                    end_game = True
                    pygame.mixer.music.load("Draw windows sound.mp3")
                    pygame.mixer.music.play()
                    toplevel_window_win_message(turn)
                    restart_button_function()
                turn = "X"
                Computer_root.update_idletasks()
            if clicks == 1:
                if end_game != True:
                    computer_playing()
                    for key in game_board.keys():
                        buttons[key - 1]["text"] = game_board[key]
                    pygame.mixer.music.load("cross_sound.mp3")
                    pygame.mixer.music.play()
                    if check_win(turn):
                        end_game = True
                        pygame.mixer.music.load("Win windows sound.mp3")
                        pygame.mixer.music.play()
                        toplevel_window_win_message(turn)
                        restart_button_function()
                    elif check_draw():
                        end_game = True
                        pygame.mixer.music.load("Draw windows sound.mp3")
                        pygame.mixer.music.play()
                        toplevel_window_win_message(turn)
                        restart_button_function()
            else:
                if end_game != True:
                    time.sleep(0.28)
                    computer_playing()
                    for key in game_board.keys():
                        buttons[key - 1]["text"] = game_board[key]
                    pygame.mixer.music.load("cross_sound.mp3")
                    pygame.mixer.music.play()
                    if check_win(turn):
                        # Computer += 1
                        set_computer_win()
                        set_total_games()
                        set_total_computer_wins()
                        end_game = True
                        pygame.mixer.music.load("Lose windows sound.mp3")
                        pygame.mixer.music.play()
                        toplevel_window_win_message(turn)
                        restart_button_function()
                    elif check_draw():
                        # Tied += 1
                        set_tied()
                        set_total_tied()

                        # here set total games is not set because at the end of the game,
                        # if it is draw then it will be players turn

                        end_game = True
                        pygame.mixer.music.load("Draw windows sound.mp3")
                        pygame.mixer.music.play()
                        toplevel_window_win_message(turn)
                        restart_button_function()
            turn = "O"


# creating window

Computer_root = Tk()

window_width = 350
window_height = 482

screen_width = Computer_root.winfo_screenwidth()
screen_height = Computer_root.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# window properties

Computer_root.title("Tic-Tac-Toe")
Computer_root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Computer_root.minsize(window_width, window_height)
Computer_root.maxsize(window_width, window_height)
Computer_root["background"] = "#457bad"

# topic frame

frame1 = Frame(Computer_root, bg="#457bad", borderwidth=2)
frame1.grid(padx=(0, 88), pady=14)

back_button = Button(frame1, text="🡸", width=4, height=1, font="Arial 14 bold ", relief="solid", command=back_button,
                     bg="#457bad")
back_button.grid(padx=(0, 10), row=0, column=0)

label = Label(frame1, text="Tic-Tac-Toe", font="Arial 20", relief="solid", borderwidth=2, padx=2, pady=2)
label.grid(padx=(20, 0), row=0, column=1)

# mainframe

frame2 = Frame(Computer_root, bg="black", borderwidth=3)
frame2.grid(padx=43, pady=7)

# label -- inside this all the subframes and buttons are included

label1 = Label(frame2)
label1.grid()

# Subframe and buttons -- inside sub-frames are the buttons

# ROW 1
# BUTTON 1

frame3 = Frame(label1, bg="grey", borderwidth=2)
frame3.grid(row=0, column=0, padx=10, pady=10)

button1 = Button(frame3, text=" ", height=2, width=4, font="Arial 17")
button1.grid()
button1.bind("<Button-1>", click)

# BUTTON 2

frame4 = Frame(label1, bg="grey", borderwidth=2)
frame4.grid(row=0, column=1, padx=10, pady=10)

button2 = Button(frame4, text=" ", height=2, width=4, font="Arial 17")
button2.grid()
button2.bind("<Button-1>", click)

# BUTTON 3

frame5 = Frame(label1, bg="grey", borderwidth=2)
frame5.grid(row=0, column=2, padx=10, pady=10)

button3 = Button(frame5, text=" ", height=2, width=4, font="Arial 17")
button3.grid()
button3.bind("<Button-1>", click)

# ROW 2
# BUTTON 4

frame6 = Frame(label1, bg="grey", borderwidth=2)
frame6.grid(row=1, column=0, padx=10, pady=10)

button4 = Button(frame6, text=" ", height=2, width=4, font="Arial 17")
button4.grid()
button4.bind("<Button-1>", click)

# BUTTON 5

frame7 = Frame(label1, bg="grey", borderwidth=2)
frame7.grid(row=1, column=1, padx=10, pady=10)

button5 = Button(frame7, text=" ", height=2, width=4, font="Arial 17")
button5.grid()
button5.bind("<Button-1>", click)

# BUTTON 6

frame8 = Frame(label1, bg="grey", borderwidth=2)
frame8.grid(row=1, column=2, padx=10, pady=10)

button6 = Button(frame8, text=" ", height=2, width=4, font="Arial 17")
button6.grid()
button6.bind("<Button-1>", click)

# ROW 3
# BUTTON 7

frame9 = Frame(label1, bg="grey", borderwidth=2)
frame9.grid(row=2, column=0, padx=10, pady=10)

button7 = Button(frame9, text=" ", height=2, width=4, font="Arial 17")
button7.grid()
button7.bind("<Button-1>", click)

# BUTTON 8

frame10 = Frame(label1, bg="grey", borderwidth=2)
frame10.grid(row=2, column=1, padx=10, pady=10)

button8 = Button(frame10, text=" ", height=2, width=4, font="Arial 17")
button8.grid()
button8.bind("<Button-1>", click)

# BUTTON 9

frame11 = Frame(label1, bg="grey", borderwidth=2)
frame11.grid(row=2, column=2, padx=10, pady=10)

button9 = Button(frame11, text=" ", height=2, width=4, font="Arial 17")
button9.grid()
button9.bind("<Button-1>", click)


# buttons list

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

# event loop

Computer_root.protocol("WM_DELETE_WINDOW", reset_score_computer)
Computer_root.mainloop()
