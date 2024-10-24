from tkinter import *
import subprocess
import pygame

pygame.mixer.init()


# Defining function

def call_player_v_player_score():
    Scoreboard_root.destroy()
    Scoreboard_root.quit()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'Player vs Player Score.py'])


def call_player_v_computer_score():
    Scoreboard_root.destroy()
    Scoreboard_root.quit()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'Player vs Computer Score.py'])


def back_button():
    Scoreboard_root.quit()
    Scoreboard_root.destroy()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'First_window.py'])


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

    global Scoreboard_root
    Scoreboard_root.quit()
    Scoreboard_root.destroy()


Scoreboard_root = Tk()

window_width = 280
window_height = 280

screen_width = Scoreboard_root.winfo_screenwidth()
screen_height = Scoreboard_root.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# window properties

Scoreboard_root.title("Tic-Tac-Toe")
Scoreboard_root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Scoreboard_root.minsize(window_width, window_height)
Scoreboard_root.maxsize(window_width, window_height)
Scoreboard_root.configure(bg="#457bad")

Topic_frame = Frame(Scoreboard_root, bg="#457bad")
Topic_frame.grid(padx=14, pady=14)

back_button = Button(Topic_frame, text="🡸", width=4, height=1, font="Arial 14 bold ", relief="solid",
                     command=back_button, bg="#457bad")
back_button.grid(padx=(0, 10), row=0, column=0)

score_label = Label(Topic_frame, text="Scores", font="arial 25 bold italic", bg="#457bad", fg="white")
score_label.grid(padx=(8, 0), row=0, column=1)

Player_vs_Player_score_button = Button(Scoreboard_root, text="Player vs Player", font="Arial 15",
                                       command=call_player_v_player_score)
Player_vs_Player_score_button.grid(padx=(49, 0), pady=20, row=1, column=0)

Player_vs_computer_score_button = Button(Scoreboard_root, text="Player vs Computer", font="Arial 15",
                                         command=call_player_v_computer_score)
Player_vs_computer_score_button.grid(padx=(48, 0), pady=20, row=2, column=0)

Scoreboard_root.protocol("WM_DELETE_WINDOW", reset_score_player)
Scoreboard_root.mainloop()
