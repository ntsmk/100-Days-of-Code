from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# todo set up the logo image as it is shown in the video.
window = Tk()
window.title("Password manager")

img_file = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
window.config(padx=20, pady=20)

canvas.create_image(100, 100, image=img_file)
canvas.grid(column=0, row=0)


window.mainloop()