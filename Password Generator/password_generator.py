import random
from tkinter import messagebox
from tkinter import *

is_on = True


def switch():
    global is_on
    global repeat

    if is_on:
        on_button.config(image = off)
        is_on = False
        repeat = 0
    else:
        on_button.config(image = on)
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

  if cont == True:
    #Check if user allows repetition of characters
    if is_on == True:
      password = random.sample(character_string,length)
    else:
      password = random.choices(character_string,k=length)
    password=''.join(password)
    password_v = StringVar()
    password_v.set(password)
    password_label = Entry(password_gen,fg = "cyan", bd=0, bg="gray85", justify = 'center', textvariable=password_v, state="readonly")
    password_label.place(x=10, y=190, width=280)


#String containing letters, symbols and numbers
character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&"

#User interface
password_gen  = Tk()
password_gen.geometry("290x240")
password_gen.title("Password Generator")

#Load switch images
on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")

#Title
title_label = Label(password_gen, text="Password Generator", font=('Ubuntu Mono', 12))
title_label.pack()

#Read length 
length_label = Label(password_gen, text = "Password length: ")
length_label.place(x=20, y=30)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190, y=30)

#Read repetition
repeat_label = Label(password_gen, text = "No repetition")
repeat_label.place(x=20, y=70)
on_button = Button(password_gen, image = on, bd = 0,
                   command = switch)
on_button.place(x=155, y=60)

#Generate password
password_button = Button(password_gen, text = "Generate Password", command=generate_password)
password_button.place(x=70, y=130)

gen = Label(password_gen, text = "Generated Password:")
gen.place(x=80, y=170)

#Exit and close the app
password_gen.mainloop()
