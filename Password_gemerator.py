from tkinter import *
import random

root = Tk()
root.title("Password Generator")
root.geometry("400x200")
root.configure(background="Sky Blue")

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*_-+="

ch = alphabets + numbers + symbols

label_ch = Label(
    root, text="Number of characters", background="Sky Blue", font=("Arial", 12)
).pack(padx=10)
ch_length = Entry(root, font="Arial 14")
ch_length.pack(padx=10)


def generate_password():
    length = ch_length.get()
    password = "".join(random.sample(ch, int(length)))
    label_password.config(text="Generated Password: " + password)


Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Verdana", 12),
    background="Orange",
).pack(padx=10)
label_password = Label(root, font=("Arial", 12), background="Sky Blue")
label_password.pack()


root.mainloop()
