from tkinter import *
import subprocess
import pygame

pygame.mixer.init()


# Defining function

# get scores function is facing runtime errors
def get_player1_score():
    fs = open("Player_vs_Player_score.txt", "r")
    w = fs.readlines()
    x = w[0]  # index of line.
    j = x.split("-")
    a = j[-1]
    fs.close()
    return a


def get_player2_score():
    fs = open("Player_vs_Player_score.txt", "r")
    w = fs.readlines()
    x = w[1]
    m = x.split("-")
    b = m[-1]
    fs.close()
    return b


def get_tied_score():
    fs = open("Player_vs_Player_score.txt", "r")
    w = fs.readlines()
    x = w[2]  # index of line.
    n = x.split("-")
    c = n[-1]
    fs.close()
    return c


def reset_score():
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
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

    global o_label
    o_label.destroy()

    global x_label
    x_label.destroy()

    global tied_label
    tied_label.destroy()

    global reset_score_button
    reset_score_button.destroy()

    get_player1_score()
    player1_label()

    get_player2_score()
    player2_label()

    get_tied_score()
    Tied_label()

    reset_button()

def back_button():
    Player_v_Player_score_root.quit()
    Player_v_Player_score_root.destroy()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'Scoreboard_window.py'])


def player1_label():
    global score_frame
    global o_label
    o_label = Label(score_frame, text=f'Player1 - {get_player1_score()}', font="Arial 15 bold", bg="#457bad",
                    fg="white")
    o_label.pack(padx=60)


def player2_label():
    global score_frame
    global x_label
    x_label = Label(score_frame, text=f'Player2 - {get_player2_score()}', font="Arial 15 bold", bg="#457bad",
                    fg="white")
    x_label.pack(padx=60)


def Tied_label():
    global score_frame
    global tied_label
    tied_label = Label(score_frame, text=f'Tied - {get_tied_score()}', font="Arial 15 bold", bg="#457bad", fg="white")
    tied_label.pack()


def reset_button():
    global reset_score_button
    reset_score_button = Button(score_frame, text=f'Reset Score', font="Arial 15", command=reset_score)
    reset_score_button.pack(pady=15)


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

    global Player_v_Player_score_root
    Player_v_Player_score_root.quit()
    Player_v_Player_score_root.destroy()


Player_v_Player_score_root = Tk()

window_width = 280
window_height = 280

screen_width = Player_v_Player_score_root.winfo_screenwidth()
screen_height = Player_v_Player_score_root.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# window properties

Player_v_Player_score_root.title("Tic-Tac-Toe")
Player_v_Player_score_root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Player_v_Player_score_root.minsize(window_width, window_height)
Player_v_Player_score_root.maxsize(window_width, window_height)
Player_v_Player_score_root.configure(bg="#457bad")

Topic_frame = Frame(Player_v_Player_score_root, bg="#457bad")
Topic_frame.pack(padx=(0, 50), pady=(14, 5))

back_button = Button(Topic_frame, text="🡸", width=4, height=1, font="Arial 14 bold ", relief="solid",
                     command=back_button, bg="#457bad")
back_button.grid(padx=(0, 5), row=0, column=0)

score_name_label = Label(Topic_frame, text="Scores", font="arial 25 bold italic", bg="#457bad", fg="Black")
score_name_label.grid(padx=(8, 0), row=0, column=1)

score_frame = Frame(Player_v_Player_score_root, bg="#457bad")
score_frame.pack(padx=(10, 0), pady=(5, 0), anchor="center")

get_player1_score()
player1_label()

get_player2_score()
player2_label()

get_tied_score()
Tied_label()

reset_button()

Player_v_Player_score_root.protocol("WM_DELETE_WINDOW", reset_score_player)
Player_v_Player_score_root.mainloop()
