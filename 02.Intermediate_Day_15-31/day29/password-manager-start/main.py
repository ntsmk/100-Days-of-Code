from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# todo write to the data inside data.txt. each data should be on a new line
# todo all fields will be cleared after "add" button use "delete" method

def save():
    f = open("data.txt", "a")
    f.write(f"{web_input.get()} | {email_input.get()} | {pass_input.get()}\n")
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

generate_button = Button(text="Generate Password")
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