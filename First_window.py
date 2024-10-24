from tkinter import *
import pygame
import subprocess

pygame.mixer.init()


def call_player_v_player():
    first_root.quit()
    first_root.destroy()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'Player_vs_Player.py'])


def call_player_v_computer():
    first_root.quit()
    first_root.destroy()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'Player_vs_computer.py'])


def call_score():
    first_root.quit()
    first_root.destroy()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'Scoreboard_window.py'])


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

    global first_root
    first_root.quit()
    first_root.destroy()


first_root = Tk()

window_width = 350
window_height = 482

screen_width = first_root.winfo_screenwidth()
screen_height = first_root.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# window properties

first_root.title("Tic-Tac-Toe")
first_root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
first_root.minsize(window_width, window_height)
first_root.maxsize(window_width, window_height)
first_root.configure(bg="#457bad")

frame1 = Frame(first_root, bg="black", borderwidth=2)
frame1.pack(pady=44)

label = Label(frame1, text="Tic-Tac-Toe", font="Arial 20", padx=2, pady=4)
label.pack()

playervsplayer_button = Button(first_root, text="Play with friends", padx=2, pady=3, width=17, height=1,
                               font="Arial 17 ", command=call_player_v_player)
playervsplayer_button.pack(pady=20)

playervscomp_button = Button(first_root, text="Play with Computer", padx=2, pady=3, width=17, height=1,
                             font="Arial 17 ", command=call_player_v_computer)
playervscomp_button.pack(pady=20)

score_button = Button(first_root, text="Score Board", padx=2, pady=3, width=15, height=1, font="Arial 17 ",
                      command=call_score)
score_button.pack(pady=20)

first_root.protocol("WM_DELETE_WINDOW", reset_score_player)
first_root.mainloop()
