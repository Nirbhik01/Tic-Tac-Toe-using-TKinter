from tkinter import *
import subprocess
import pygame

pygame.mixer.init()

# Defining function
def back_button():
    Player_v_Computer_score_root.quit()
    Player_v_Computer_score_root.destroy()
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
    subprocess.call(['python', 'Scoreboard_window.py'])


def get_total_games():
    file = open("Player_vs_Computer_score.txt", "r")
    w = file.readlines()
    x = w[0]
    y = x.split("-")
    z = y[-1]
    file.close()
    return z


def get_total_player_wins():
    file = open("Player_vs_Computer_score.txt", "r")
    w = file.readlines()
    x = w[1]
    y = x.split("-")
    z = y[-1]
    file.close()
    return z


def get_total_computer_wins():
    file = open("Player_vs_Computer_score.txt", "r")
    w = file.readlines()
    x = w[2]
    y = x.split("-")
    z = y[-1]
    file.close()
    return z


def get_total_tied():
    file = open("Player_vs_Computer_score.txt", "r")
    w = file.readlines()
    x = w[3]
    y = x.split("-")
    z = y[-1]
    file.close()
    return z


def get_player_wins():
    file = open("Player_vs_Computer_score.txt", "r")
    w = file.readlines()
    x = w[5]
    y = x.split("-")
    z = y[-1]
    file.close()
    return z


def get_computer_wins():
    file = open("Player_vs_Computer_score.txt", "r")
    w = file.readlines()
    x = w[6]
    y = x.split("-")
    z = y[-1]
    file.close()
    return z


def get_tied():
    file = open("Player_vs_Computer_score.txt", "r")
    w = file.readlines()
    x = w[7]
    y = x.split("-")
    z = y[-1]
    file.close()
    return z


def reset_score():
    pygame.mixer.music.load("restart button sound.mp3")
    pygame.mixer.music.play()
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

    global Player_wins_label
    Player_wins_label.destroy()

    global Computer_wins_label
    Computer_wins_label.destroy()

    global Tied_label
    Tied_label.destroy()

    global reset_score_button
    reset_score_button.destroy()

    get_player_wins()
    player_win_label_function()

    get_computer_wins()
    computer_wins_label_function()

    get_tied()
    tied_label_function()

    reset_button_function()


def player_win_label_function():
    global recent_games_score_frame
    global Player_wins_label
    Player_wins_label = Label(recent_games_score_frame, text=f"Player - {get_player_wins()}", font="Arial 14 bold",
                              bg="#457bad", fg="white")
    Player_wins_label.grid(row=0, column=0, sticky="w")


def computer_wins_label_function():
    global recent_games_score_frame
    global Computer_wins_label
    Computer_wins_label = Label(recent_games_score_frame, text=f"Computer - {get_computer_wins()}",
                                font="Arial 14 bold", bg="#457bad", fg="white")
    Computer_wins_label.grid(row=1, column=0, sticky="w")


def tied_label_function():
    global recent_games_score_frame
    global Tied_label
    Tied_label = Label(recent_games_score_frame, text=f"Tied - {get_tied()}", font="Arial 14 bold", bg="#457bad",
                       fg="white")
    Tied_label.grid(row=2, column=0, sticky="w")


def reset_button_function():
    global Player_v_Computer_score_root
    global reset_score_button
    reset_score_button = Button(Player_v_Computer_score_root, text="Reset Score", font="arial 16", command=reset_score)
    reset_score_button.pack(pady=(20, 0))


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

    global Player_v_Computer_score_root
    Player_v_Computer_score_root.quit()
    Player_v_Computer_score_root.destroy()


Player_v_Computer_score_root = Tk()

window_width = 350
window_height = 550

screen_width = Player_v_Computer_score_root.winfo_screenwidth()
screen_height = Player_v_Computer_score_root.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# window properties

Player_v_Computer_score_root.title("Tic-Tac-Toe")
Player_v_Computer_score_root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
Player_v_Computer_score_root.minsize(window_width, window_height)
Player_v_Computer_score_root.maxsize(window_width, window_height)
Player_v_Computer_score_root.configure(bg="#457bad")

Topic_frame = Frame(Player_v_Computer_score_root, bg="#457bad")
Topic_frame.pack(padx=(0, 65), pady=14)

back_button = Button(Topic_frame, text="🡸", width=4, height=1, font="Arial 14 bold", relief="solid",
                     command=back_button, bg="#457bad")
back_button.grid(padx=(0, 20), pady=(2, 0), row=0, column=0)

score_label = Label(Topic_frame, text="Scores", font="arial 25 bold italic", bg="#457bad", fg="white")
score_label.grid(padx=(8, 0), row=0, column=1)

Total_scores_frame = Frame(Player_v_Computer_score_root, bg="#457bad")
Total_scores_frame.pack(padx=40, pady=(5, 0), anchor="w")

total_games_label = Label(Total_scores_frame, text=f"Total games - {get_total_games()}", font="Arial 14 bold",
                          bg="#457bad", fg="white")
total_games_label.grid(row=0, column=0, sticky="w")

total_Player_wins_label = Label(Total_scores_frame, text=f"Player Wins - {get_total_player_wins()}",
                                font="Arial 14 bold", bg="#457bad", fg="white")
total_Player_wins_label.grid(row=1, column=0, sticky="w")

total_Computer_wins_label = Label(Total_scores_frame, text=f"Computer Wins - {get_total_computer_wins()}",
                                  font="Arial 14 bold", bg="#457bad", fg="white")
total_Computer_wins_label.grid(row=2, column=0, sticky="w")

total_tied_label = Label(Total_scores_frame, text=f"Games Tied - {get_total_tied()}", font="Arial 14 bold",
                         bg="#457bad", fg="white")
total_tied_label.grid(row=3, column=0, sticky="w")

recent_games_topic_label = Label(Player_v_Computer_score_root, text="Recent Games: \n", font="arial 16 bold",
                                 bg="#457bad", fg="white")
recent_games_topic_label.pack(pady=(10, 0))

recent_games_score_frame = Frame(Player_v_Computer_score_root, bg="#457bad")
recent_games_score_frame.pack(padx=40, anchor="w")

get_player_wins()
player_win_label_function()

get_computer_wins()
computer_wins_label_function()

get_tied()
tied_label_function()

reset_button_function()

Player_v_Computer_score_root.protocol("WM_DELETE_WINDOW", reset_score_computer)
Player_v_Computer_score_root.mainloop()
