Password Generator Project

This is my first personal coding project (non-school).

An 11 character password is generated that includes 3 upper-case letters, 3 lower-case letters, 3 numbers, and 2 special characters.

Notable trouble-shooting/learning moments included:
- Using random.shuffle (list exclusive function) to create a function that can shuffle strings
- using a separate variable to grab separate ranges from the ASCII table (as to my knowledge random.randint only accepts one range)
- Making the password variable global (so that the copy function would grab the updated password post-button press,
instead of being restrincted to the empty variable)
- Learning tkinter to create a functional GUI
- Learning pyinstaller to create a .exe file from my .py project
    - Using --noconsole so cmd doesn't launch
    - Figuring out .ico files and using pyinstaller to replace the default .exe icon
- Uploading to my github repo (I haven't done this since I took MBB 243 - Intro Data Analysis for Molecular Bio & Biochem)
via the terminal