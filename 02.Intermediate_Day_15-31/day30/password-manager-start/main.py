from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    """
    generates password randomly
    :return:
    """
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
# todo if not, catches exception and show message "no data found" when search button is hit
# current status: when it matches it shows email address and password but exception is not in yet(#6,7)

def find_password():
    entered_website = web_input.get()
    with open("data.json", "r") as data_file:
        websites = json.load(data_file)
        for data in websites:
            if entered_website == data:
                messagebox.showinfo(data,
                                    f"Email: {websites[data]["email"]}\nPassword: {websites[data]["Password"]}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    take data from the field and save it as json file
    :return:
    """
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "Password": password,
        }
    }
    # error message for empty
    if website == "" or password == "":
        messagebox.showinfo("Oops", "please don't leave any fields empty")

    # if it is not empty, save it
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # writing data
                json.dump(new_data, data_file, indent=4)

        # if reading (try part) is successful
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # writing data
                json.dump(data, data_file, indent=4)
        # do it no matter issues or not
        finally:
            web_input.delete(0, END)
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

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=1)
web_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "ntsmk@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

window.mainloop()
