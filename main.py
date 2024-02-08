import pandas as ps
from tkinter import *
import random as rd
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
word_to_learn = {}

try:
    words_df = ps.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_df = ps.read_csv("data/de_100.csv")
finally:
    words_dc = words_df.to_dict(orient="records")

#-------------------------------------- TO_LEARN --------------------------------------#

def to_learn():
    global word_to_learn, timer
    window.after_cancel(timer)
    word_to_learn = rd.choice(words_dc)
    canvas.itemconfig(image_card, image=front_card_img)
    canvas.itemconfig(language_text, text="German", fill="black")
    canvas.itemconfig(word_text, text=word_to_learn["German"], fill="black")
    timer = window.after(3000, flip)

#-------------------------------------- CORRECT --------------------------------------#

# If the word is knonw delete it from the list and create a list of still unknown words
def correct():
    #print(word_to_learn)
    words_dc.remove(word_to_learn)
    #print(words_dc)
    words_stil_unkown_df = ps.DataFrame(words_dc)
    words_stil_unkown_df.to_csv("data/words_to_learn.csv", index=False)
    to_learn()


#-------------------------------------- FLIP THE CARD --------------------------------------#

# Function witch flips the card
def flip():
        canvas.itemconfig(language_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=word_to_learn["English"], fill="white")
        canvas.itemconfig(image_card, image=back_card_img)

#-------------------------------------- UI --------------------------------------#
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip)

# Canvas: Card image
canvas = front_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images\card_front.png")
back_card_img = PhotoImage(file="images\card_back.png")
image_card = front_canvas.create_image(400, 263, image=front_card_img)
front_canvas.grid(column=0, row=0, columnspan=2)
language_text = front_canvas.create_text(400, 150, text="", font=FONT_LANGUAGE)
word_text = front_canvas.create_text(400, 263, text="", font=FONT_WORD)

# Buttons
wrong_button_img = PhotoImage(file="images\wrong.png")
wrong_bt = Button(image=wrong_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=to_learn)
wrong_bt.grid(column=0, row=1)

right_button_img = PhotoImage(file="images\correct.png")
right_bt = Button(image=right_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=correct)
right_bt.grid(column=1, row=1)

to_learn()

window.mainloop()

