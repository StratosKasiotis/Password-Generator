#----------INITIALIZATION----------#

import random
from tkinter import *
from tkinter import messagebox
import pyperclip

BACKGROUND_COLOR = "#EED5B7"

#----------FUNCTION_SETUP----------#

def pass_generator():
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "1234567889"
  symbols = "!@#$%^&*()/\_+-" #or any other symbols you might prefer
  use_for = lower_case + upper_case + numbers + symbols
  len_pass = 8 #you can change that if you prefer smaller or larger passwords
  password = "".join(random.sample(use_for,len_pass))
  # print(f"Generated Password is:  {password} \n")
  messagebox.showinfo(title="PASSWORD GENERATED", message=f"Your password is: {password}")
  # pyperclip.copy(password)

#----------UI_SETUP----------#

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=512, height=512)
# password_img = PhotoImage(file="password.png")
# canvas.create_image(256, 256, image=password_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

generate_button_image = PhotoImage(file="password.png")
generate_button = Button(image=generate_button_image, fg=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0, command=pass_generator)
generate_button.grid(row=0, column=0)


    
window.mainloop()   
