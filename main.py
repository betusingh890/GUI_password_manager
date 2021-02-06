import tkinter
import random

bg_color = "#f7f6e7"
color2 = "#e1bc91"
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
characters = ['!', '@', '$', '&']
options = [alphabets, numbers, characters]


def invalid_action():
    window_invalid = tkinter.Tk()
    window_invalid.config(bg=bg_color, width=230, height=100)
    window_invalid.title("Invalid selection")
    label_invalid = tkinter.Label(window_invalid)
    label_invalid.config(text="You cant leave any field blank")
    label_invalid2 = tkinter.Label(window_invalid)
    label_invalid2.config(text="if you want to save the data")
    label_invalid.place(x=20, y=20)
    label_invalid2.place(x=20, y=50)


def save_data():
    username_ = username.get()
    platform_ = platform.get()
    password_ = password.get()
    if username_ == "" or platform_ == "" or password_ == "":
        invalid_action()
    else:
        dictionary = {platform_: {"username": username_,
                                  "password": password_}}
        with open("data.json", 'a') as file:
            file.write(str(dictionary))


def lenth_taker_window():
    global pass_lenth
    global window_lenth
    window_lenth = tkinter.Tk()
    window_lenth.config(bg=bg_color, width=350, height=200)
    window_lenth.title("Length of Password")
    lenth_label = tkinter.Label(window_lenth)
    lenth_label.config(text="Enter length of password:", font=("Courier", 20, "bold"))
    lenth_label.place(x=10, y=20)
    pass_lenth = tkinter.Entry(window_lenth)
    pass_lenth.focus()
    pass_lenth.place(x=30, y=70)
    done = tkinter.Button(window_lenth)
    done.config(text="Done", font=("Courier", 25, "bold"), command=get_length)
    done.place(x=80, y=120)


def get_length():
    global password_lenth
    password_lenth = pass_lenth.get()
    window_lenth.destroy()
    password_generator()


def password_generator():
    global random_pass
    random_pass = ""
    password_generated = []
    for i in range(0, int(password_lenth)):
        selected_list = random.choice(options)
        selected_character = random.choice(selected_list)
        password_generated.append(selected_character)

    for item in password_generated:
        item = str(item)
        random_pass += item
    password.insert(0, random_pass)

    return random_pass


display = tkinter.Tk()
display.title("Password Manager")
display.config(bg=bg_color, width=700, height=600)

username_label = tkinter.Label()
username_label.config(text="Username/emailid", font=("Courier", 25, "bold"), bg=bg_color)
username_label.place(x=20, y=280)

username = tkinter.Entry()
username.config(width=30, bg=color2)
username.place(x=340, y=280)

platform_label = tkinter.Label()
platform_label.config(text="Name of Platform", font=("Courier", 25, "bold"), bg=bg_color)
platform_label.place(x=20, y=340)

platform = tkinter.Entry()
platform.config(width=30, bg=color2)
platform.place(x=340, y=340)

password_label = tkinter.Label()
password_label.config(text="Password", font=("Courier", 25, "bold"), bg=bg_color)
password_label.place(x=20, y=400)

password = tkinter.Entry()
password.place(x=170, y=405)
password.config(width=25, bg=color2)
password.focus()

generate_button = tkinter.Button()
generate_button.config(text="Generate", font=("Courier", 25, "bold"), command=lenth_taker_window)
generate_button.place(x=460, y=400)

save_button = tkinter.Button()
save_button.config(text="Save", font=("Courier", 30, "bold"), command=save_data)
save_button.place(x=200, y=470)

canvas = tkinter.Canvas()
canvas.config(bg=bg_color, highlightthickness=0)
photo = tkinter.PhotoImage(file="logo.png")
canvas.create_image((160, 100), image=photo)
canvas.place(x=170, y=30)

display.mainloop()
