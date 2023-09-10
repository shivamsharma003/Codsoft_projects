from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Game Rock paper and scissor")
root.configure(background="Black")


image_rock = ImageTk.PhotoImage(Image.open("rock_right.png"))
image_paper = ImageTk.PhotoImage(Image.open("paper_right.png"))
image_scissor = ImageTk.PhotoImage(Image.open("scissor_right.png"))

image_rock1 = ImageTk.PhotoImage(Image.open("rock_left.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper_left.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor_left.png"))

label_player = Label(root, image=image_paper)
label_computer = Label(root, image=image_paper1)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

computer_score = Label(root, text=0, font=("Arial", 60, "bold"), fg="blue")
player_score = Label(root, text=0, font=("Arial", 60, "bold"), fg="red")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

player_indicator = Label(
    root, font=("Arial", 35, "bold"), text="PLAYER", bg="orange", fg="blue"
)
computer_indicator = Label(
    root, font=("Arial", 35, "bold"), text="COMPUTER", bg="orange", fg="blue"
)

computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)


def msg_updation(a):
    final_message["text"] = a


def computer_update():
    final = int(computer_score["text"])
    final += 1
    computer_score["text"] = str(final)


def player_update():
    final = int(player_score["text"])
    final += 1
    player_score["text"] = str(final)


def winner_check(p, c):
    if p == c:
        msg_updation("It's a Tie")
    elif p == "rock":
        if c == "paper":
            msg_updation("Computer Wins !!")
            computer_update()
        else:
            msg_updation("Player Wins !!")
            player_update()

    elif p == "paper":
        if c == "scissor":
            msg_updation("Computer Wins !!")
            computer_update()
        else:
            msg_updation("Player Wins !!")
            player_update()

    elif p == "scissor":
        if c == "rock":
            msg_updation("Computer Wins !!")
            computer_update()
        else:
            msg_updation("Player Wins !!")
            player_update()

    else:
        pass


to_select = ["rock", "paper", "scissor"]


def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock1)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper1)
    else:
        label_computer.configure(image=image_scissor1)

    if a == "rock":
        label_player.configure(image=image_rock)
    elif a == "paper":
        label_player.configure(image=image_paper)
    else:
        label_player.configure(image=image_scissor)

    winner_check(a, choice_computer)


final_message = Label(root, font=("Arial", 20, "bold"), bg="red", fg="white")
final_message.grid(row=3, column=2, pady=(20, 30))


button_R = Button(
    root,
    width=16,
    height=3,
    text="ROCK",
    font=("Arial", 20, "bold"),
    bg="Sky Blue",
    fg="yellow",
    command=lambda: choice_update("rock"),
).grid(row=2, column=1)

button_P = Button(
    root,
    width=16,
    height=3,
    text="PAPER",
    font=("Arial", 20, "bold"),
    bg="red",
    fg="yellow",
    command=lambda: choice_update("paper"),
).grid(row=2, column=2)

button_S = Button(
    root,
    width=16,
    height=3,
    text="SCISSOR",
    font=("Arial", 20, "bold"),
    bg="Orange",
    fg="yellow",
    command=lambda: choice_update("scissor"),
).grid(row=2, column=3)


root.mainloop()
