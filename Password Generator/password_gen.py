#Jonathan Mesak
#01/09/2024

import random
from tkinter import *

#function to shuffle characters in a string (.string function can only shuffle lists)
def shuffle_string(string):
        temp_list = list(string)
        random.shuffle(temp_list)
        return ''.join(temp_list)

password = ''

#Random 9 character password gennerator
def button_press():
        low_case_1 = chr(random.randint(97,122))
        low_case_2 = chr(random.randint(97,122))
        low_case_3 = chr(random.randint(97,122))
        up_case_1 = chr(random.randint(65,90))
        up_case_2 = chr(random.randint(65,90))
        up_case_3 = chr(random.randint(65,90))
        number_1 = chr(random.randint(48,57))
        number_2 = chr(random.randint(48,57))
        number_3 = chr(random.randint(48,57))

        allowed_chars = [33] + list(range(35, 39)) + list(range(63, 65))
        spec_char_1 = chr(random.choice(allowed_chars))
        spec_char_2 = chr(random.choice(allowed_chars))

        unshuf_pass = low_case_1 + low_case_2 + low_case_3 + up_case_1 + up_case_2 + up_case_3 + number_1 + number_2 + number_3 + spec_char_1 + spec_char_2
        global password
        password = shuffle_string(unshuf_pass)
        label_password.config(text=password)

def copy():
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()

#GUI colours
white = '#ffffff'
navyblue = '#213152'
grey = '#1f1f1f'
darkblue = '#141b33'

#Window Attributes
window = Tk()
window.geometry('600x400')
window.resizable(width = False, height = False)
window.title('Random Password Generator')
window.wm_attributes('-toolwindow', 'True') #Removes tkinter favicon from top bar

#Framing for buttons/labels
frame = Frame(window, bg = grey, pady = 20, padx = 20)
frame.pack(fill=BOTH, expand=True)
frame.columnconfigure(0, weight = 1)
frame.rowconfigure(0, weight = 1)
frame.rowconfigure(1, weight = 1)
frame.rowconfigure(2, weight = 1)

#Password Generator button
button = Button(frame,
                text = 'Generate \n Password',
                command = button_press,
                font = ('Helvetica', 35, 'bold'),
                bg = navyblue,
                fg = white,
                activebackground = darkblue,
                activeforeground = white,
                border = 0,
                cursor = 'hand2'
                )

#Outputed Password
label_password = Label(frame,
                       text = password, 
                       font = ('Helvetica', 35, 'bold'),
                       fg = white,
                       bg = frame.cget('bg'),
                       height = 2,
                       border = 0
                       )

copy_button = Button(frame,
                     text = 'Copy To ClipBoard',
                     command = copy,
                     font = ('Helvetica', 10, 'bold'),
                     bg = navyblue,
                     fg = white,
                     activebackground = darkblue,
                     activeforeground = white,
                     border = 0,
                     cursor = 'hand2'
                     )

button.grid(column = 0, row = 0)
label_password.grid(column = 0, row = 1)
copy_button.grid(column = 0, row = 2)

window.mainloop()       