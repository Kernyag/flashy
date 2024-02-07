from tkinter import *
from pandas import *
BACKGROUND_COLOR = "#B1DDC6"

#-------------------------------------- UI --------------------------------------#
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas: Card image
front_canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card_img = PhotoImage(file="images\card_front.png")
front_canvas.create_image(400, 263, image=front_card_img)
front_canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button_img = PhotoImage(file="images\wrong.png")
wrong_bt = Button(image=wrong_button_img, highlightthickness=0)
wrong_bt.grid(column=0, row=1)

right_button_img = PhotoImage(file="images\correct.png")
right_bt = Button(image=right_button_img, highlightthickness=0)
right_bt.grid(column=1, row=1)


window.mainloop()
