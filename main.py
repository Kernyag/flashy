import pandas as ps
from tkinter import *
import random as rd
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

#-------------------------------------- CHOOSE A WORD --------------------------------------#
words_df = ps.read_csv("data/de_100.csv")
words_dc = words_df.to_dict(orient="records")

def select_word():
    random_index = rd.randint(0, len(words_dc))
    random_word = words_dc[random_index]["German"]
    canvas.itemconfig(language_text, text="German")
    canvas.itemconfig(word_text, text=random_word)


#-------------------------------------- UI --------------------------------------#
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas: Card image
canvas = front_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images\card_front.png")
front_canvas.create_image(400, 263, image=front_card_img)
front_canvas.grid(column=0, row=0, columnspan=2)
language_text = front_canvas.create_text(400, 150, text="", font=FONT_LANGUAGE)
word_text = front_canvas.create_text(400, 263, text="", font=FONT_WORD)

# Buttons
wrong_button_img = PhotoImage(file="images\wrong.png")
wrong_bt = Button(image=wrong_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=select_word)
wrong_bt.grid(column=0, row=1)

right_button_img = PhotoImage(file="images\correct.png")
right_bt = Button(image=right_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=select_word)
right_bt.grid(column=1, row=1)

select_word()

window.mainloop()

