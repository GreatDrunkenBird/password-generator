import random
from tkinter import messagebox
from tkinter import *
import customtkinter

is_on = True


def switch():
    global is_on

    if is_on:
        on_button.config(image=off)
        is_on = False
    else:
        on_button.config(image=on)
        is_on = True


def generate_password():
    try:
        length = int(length_entry.get())
        if length > 20:
            messagebox.showerror(message="Password exceeds 20 characters")
            cont = False
        else:
            cont = True
    except:
        messagebox.showerror(message="Please key in the password length")
        return

    if cont is True:
        if is_on is True:  # Check if user allows repetition of characters
            password = random.sample(character_string, length)
        else:
            password = random.choices(character_string, k=length)
        password = ''.join(password)
        password_v = StringVar()
        password_v.set(password)
        password_label = Label(password_gen, font=('Ubuntu Mono', 12), bd=0,
                               bg="#deedfa", justify='center', textvariable=password_v)
        password_label.place(x=10, y=190, width=220)


# String containing letters, symbols and numbers
character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&abcdefghijklmnopqrstuvwxyz0123456789!#$%&"

# User interface
password_gen = Tk()
password_gen.geometry("240x240")
password_gen.configure(bg="white")
password_gen.title("Password Generator")

# Load switch images
on = PhotoImage(file="small_on.png")
off = PhotoImage(file="small_off.png")

# Title
title_label = Label(password_gen, bg="white",
                    text="Password Generator", font=('Ubuntu Mono', 12))
title_label.pack()

# Read length
length_label = Label(password_gen, bg="white", text="Password length: ")
length_label.place(x=50, y=50)
length_entry = Entry(password_gen, width=5)
length_entry.place(x=150, y=50)

# Read repetition
repeat_label = Label(password_gen, bg="white", text="No repetition")
repeat_label.place(x=50, y=90)
on_button = Button(password_gen, image=on, bd=0, bg="white",
                   borderwidth=0, command=switch)
on_button.place(x=135, y=90)

# Generate password
password_button = customtkinter.CTkButton(password_gen, text="Generate Password", command=generate_password)
password_button.place(x=50, y=140)

# Exit and close the app
password_gen.mainloop()
