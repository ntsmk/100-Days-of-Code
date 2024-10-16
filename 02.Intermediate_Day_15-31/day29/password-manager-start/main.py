from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

def generate():
    pass_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    pass_input.insert(0, password)

# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()

    if website == "" or password == "":
        messagebox.showinfo("Oops", "please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                        f"\n Password: {password} \n Is it ok to save?")

        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()

            web_input.delete(0, END)
            # email_input.delete(0, END)
            pass_input.delete(0, END)
            web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")

img_file = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
window.config(padx=50, pady=50)

canvas.create_image(100, 100, image=img_file)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "ntsmk@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)


window.mainloop()
