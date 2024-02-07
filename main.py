from pandas import *
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

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
language_text = front_canvas.create_text(400, 150, text="German", font=FONT_LANGUAGE)
word_text = front_canvas.create_text(400, 263, text="Ich", font=FONT_WORD)

# Buttons
wrong_button_img = PhotoImage(file="images\wrong.png")
wrong_bt = Button(image=wrong_button_img, highlightthickness=0)
wrong_bt.grid(column=0, row=1)

right_button_img = PhotoImage(file="images\correct.png")
right_bt = Button(image=right_button_img, highlightthickness=0)
right_bt.grid(column=1, row=1)

window.mainloop()