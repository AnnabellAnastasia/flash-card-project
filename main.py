from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy')
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

# set up the canvas
canvas = Canvas(window, height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
# title label
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
# translation label
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black" )


canvas.grid(row=0, column=0, columnspan=2)


# set up right and wrong buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bd=0)
unknown_button.grid(row=1, column=0)


check_image = PhotoImage(file="images/right.png")
known_image = Button(image=check_image, highlightthickness=0, bd=0)
known_image.grid(row=1, column=1)
# set up flash card canvas
# canvas_flash_card = Canvas(window, height=326, width=450, highlightthickness=0)
# canvas_flash_card.grid(row=0, column=0,  columnspan=2, padx=20, pady=20)
# card_front_img = PhotoImage(file="images/card_front.png")
#
#



window.mainloop()