from tkinter import *
import subprocess
import pygame

# global variables

turn = "O"
end_game = False
game_win_condition = True

# scoring system variables

Player1 = 0
Player2 = 0
Tied = 0

# initializing pygame sound

pygame.mixer.init()

# game board

game_board = {1: " ", 2: " ", 3: " ",
              4: " ", 5: " ", 6: " ",
              7: " ", 8: " ", 9: " "}


# defining functions

def set_player1_score():
    fs = open("Player_vs_Player_score.txt", "r")
    w = fs.readlines()
    x = w[0]  # index of line.
    y = x.split("-")
    y[-1] = f'{Player1}\n'
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Player_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 0:  # line to be replces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def set_player2_score():
    fs = open("Player_vs_Player_score.txt", "r")
    w = fs.readlines()
    x = w[1]  # index of line.
    y = x.split("-")
    y[-1] = f'{Player2}\n'
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Player_score.txt", "w")
    for i, line in enumerate(w, 0):
        if i == 1:  # line to be replces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


def set_tied_score():
    fs = open("Player_vs_Player_score.txt", "r")
    w = fs.readlines()
    x = w[2]  # index of line.
    y = x.split("-")
    y[-1] = f'{Tied}'
    z = "-".join(y)
    fs.close()

    fs = open("Player_vs_Player_score.txt", "w")

    for i, line in enumerate(w, 0):
        if i == 2:  # line to be replces
            fs.writelines(z)
        else:
            fs.writelines(line)
    fs.close()


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

    reset_score_computer()

    global Player_root
    Player_root.quit()
    Player_root.destroy()


# creating the restart button
def restart_button_function():
    global frame12
    frame12 = Frame(Player_root, bg="black", borderwidth=2)
    frame12.grid(pady=14)

    global restart_button
    restart_button = Button(frame12, relief="raised", height=2, width=12, borderwidth=1, text="Restart Game",
                            font="Arial 15", command=restart_game)
    restart_button.pack()


# functionality of restart game button

def restart_game():
    global end_game, buttons
    for i in game_board.keys():
        game_board[i] = " "
    for i in buttons:
        i["text"] = " "
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    end_game = False
    restart_button.destroy()
    frame12.destroy()


# functionality of back button in the root window
def back_button():
    Player_root.destroy()
    Player_root.quit()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'First_window.py'])


# defining functionality for ok button in popup window

def call_two_functions():
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    tp.destroy()
    restart_button_function()


# defining Top level window
def toplevel_window_result_message(player):
    global tp
    tp = Toplevel(Player_root)
    tp_width = 240
    tp_height = 190
    tp.configure(bg="#567999")
    window_x = Player_root.winfo_x()
    window_y = Player_root.winfo_y()
    center_x = int(window_x + (tp_width / 4.2))
    center_y = int(window_y + (tp_height / 1.3))
    tp.geometry(f'{tp_width}x{tp_height}+{center_x}+{center_y}')
    tp.maxsize(tp_width, tp_height)
    tp.minsize(tp_width, tp_height)
    if game_win_condition:
        win_message_label = Label(tp, text=player + " has won the game", font="Arial 15 bold italic", bg="#567999",
                                  fg="white")
        win_message_label.pack(padx=15, pady=45)
    else:
        win_message_label = Label(tp, text="The game is a draw", font="Arial 15 bold italic", bg="#567999", fg="white")
        win_message_label.pack(padx=15, pady=45)
    ok_button_frame = Frame(tp, borderwidth=1, bg="black")
    ok_button_frame.pack(padx=int((tp_width / 2) - 30))
    ok_button = Button(ok_button_frame, text="OK", font="Arial 12", relief="raised", width=4, height=1, padx=10,
                       command=call_two_functions)
    ok_button.pack()
    tp.protocol("WM_DELETE_WINDOW", call_two_functions)
    tp.mainloop()


# checking if the player has won or not

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


# checking if the game is draw or not

def check_draw():
    global game_win_condition
    for i in game_board.keys():
        if game_board[i] == " ":
            return False
    game_win_condition = False
    return True


# Handling the mouse click event

def click(event):
    global turn, end_game
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

        if button["text"] == " ":
            if turn == "O":
                button["text"] = "O"
                game_board[buttonposition] = turn
                pygame.mixer.music.load("alu_sound.mp3")
                pygame.mixer.music.play()

                # check win

                if check_win(turn):
                    global Player1
                    Player1 += 1
                    set_player1_score()
                    end_game = True
                    pygame.mixer.music.load("Win windows sound.mp3")
                    pygame.mixer.music.play()
                    toplevel_window_result_message(turn)

                # check draw

                elif check_draw():
                    global Tied
                    Tied += 1
                    set_tied_score()
                    end_game = True
                    pygame.mixer.music.load("Draw windows sound.mp3")
                    pygame.mixer.music.play()
                    toplevel_window_result_message(turn)

                turn = "X"

            else:
                button["text"] = "X"
                game_board[buttonposition] = turn
                pygame.mixer.music.load("cross_sound.mp3")
                pygame.mixer.music.play()

                # check win

                if check_win(turn):
                    global Player2
                    Player2 += 1
                    set_player2_score()
                    end_game = True
                    pygame.mixer.music.load("Win windows sound.mp3")
                    pygame.mixer.music.play()
                    toplevel_window_result_message(turn)

                # check draw

                elif check_draw():
                    Tied += 1
                    set_tied_score()
                    end_game = True
                    pygame.mixer.music.load("Draw windows sound.mp3")
                    pygame.mixer.music.play()
                    toplevel_window_result_message(turn)

                turn = "O"

# creating main window

Player_root = Tk()

window_width = 350
window_height = 482

screen_width = Player_root.winfo_screenwidth()
screen_height = Player_root.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# window properties

Player_root.title("Tic-Tac-Toe")
Player_root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Player_root.minsize(window_width, window_height)
Player_root.maxsize(window_width, window_height)
Player_root.configure(bg="#457bad")

# tic tac toe topic frame

frame1 = Frame(Player_root, bg="#457bad", borderwidth=2)
frame1.grid(padx=(0, 88), pady=14)

back_button = Button(frame1, text="🡸", width=4, height=1, font="Arial 14 bold ", relief="solid", command=back_button,
                     bg="#457bad")
back_button.grid(padx=(0, 10), row=0, column=0)

label = Label(frame1, text="Tic-Tac-Toe", font="Arial 20", relief="solid", borderwidth=2, padx=2, pady=2)
label.grid(padx=(20, 0), row=0, column=1)

# mainframe of buttons

frame2 = Frame(Player_root, bg="black", borderwidth=3)
frame2.grid(padx=43, pady=7)

# label -- inside this all the subframes and buttons are included

label1 = Label(frame2)
label1.grid()

# Subframe and buttons -- inside sub-frames are the buttons

# ROW 1
# BUTTON 1

frame3 = Frame(label1, bg="grey", borderwidth=2)
frame3.grid(row=0, column=0, padx=10, pady=10)

button1 = Button(frame3, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button1.grid()
button1.bind("<Button-1>", click)

# BUTTON 2

frame4 = Frame(label1, bg="grey", borderwidth=2)
frame4.grid(row=0, column=1, padx=10, pady=10)

button2 = Button(frame4, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button2.grid()
button2.bind("<Button-1>", click)

# BUTTON 3

frame5 = Frame(label1, bg="grey", borderwidth=2)
frame5.grid(row=0, column=2, padx=10, pady=10)

button3 = Button(frame5, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button3.grid()
button3.bind("<Button-1>", click)

# ROW 2
# BUTTON 4

frame6 = Frame(label1, bg="grey", borderwidth=2)
frame6.grid(row=1, column=0, padx=10, pady=10)

button4 = Button(frame6, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button4.grid()
button4.bind("<Button-1>", click)

# BUTTON 5

frame7 = Frame(label1, bg="grey", borderwidth=2)
frame7.grid(row=1, column=1, padx=10, pady=10)

button5 = Button(frame7, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button5.grid()
button5.bind("<Button-1>", click)

# BUTTON 6

frame8 = Frame(label1, bg="grey", borderwidth=2)
frame8.grid(row=1, column=2, padx=10, pady=10)

button6 = Button(frame8, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button6.grid()
button6.bind("<Button-1>", click)

# ROW 3
# BUTTON 7

frame9 = Frame(label1, bg="grey", borderwidth=2)
frame9.grid(row=2, column=0, padx=10, pady=10)

button7 = Button(frame9, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button7.grid()
button7.bind("<Button-1>", click)

# BUTTON 8

frame10 = Frame(label1, bg="grey", borderwidth=2)
frame10.grid(row=2, column=1, padx=10, pady=10)

button8 = Button(frame10, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button8.grid()
button8.bind("<Button-1>", click)

# BUTTON 9

frame11 = Frame(label1, bg="grey", borderwidth=2)
frame11.grid(row=2, column=2, padx=10, pady=10)

button9 = Button(frame11, text=" ", height=2, width=4, font="Arial 17", relief="raised")
button9.grid()
button9.bind("<Button-1>", click)

# O and X input buttons list

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

# adding functionality to window close button

Player_root.protocol("WM_DELETE_WINDOW", reset_score_player)
Player_root.mainloop()
