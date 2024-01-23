# Password Generator Project

![image](https://github.com/Jmesak/Personal-Projects/assets/33903604/ba62197e-b209-43ab-a32d-f8535780d17d)

password_gen.exe is present in the dist folder

**Function:**
Via a GUI, at the press of a button a unique and random 11 character password is generated that includes 3 upper-case letters, 3 lower-case letters, 3 numbers, and 2 special characters.
A copy button is also present to copy the created password to clipboard.

**Notable trouble-shooting/learning moments included:**
- Using random.shuffle (list exclusive function) to create a function that can shuffle strings
- Using a separate variable to grab separate ranges from the ASCII table (as to my knowledge random.randint only accepts one range)
- Making the password variable global (so that the copy function would grab the updated password post-button press,
as it was otherwise unable to detect generated passwords)
- Learning tkinter to create a functional GUI
- Learning pyinstaller to create a .exe file from my .py project
    - Using --noconsole so cmd doesn't launch
    - Creating .ico files and using pyinstaller to replace the .exe's default icon

```python
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
```
