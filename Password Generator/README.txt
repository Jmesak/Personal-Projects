Password Generator Project

password_gen.exe is present in the dist folder

Function:
Via a GUI, at the press of a button a unique and random 11 character password is generated that includes 3 upper-case letters, 3 lower-case letters, 3 numbers, and 2 special characters.
A copy button is also present to copy the created password to clipboard.

Notable trouble-shooting/learning moments included:
- Using random.shuffle (list exclusive function) to create a function that can shuffle strings
- Using a separate variable to grab separate ranges from the ASCII table (as to my knowledge random.randint only accepts one range)
- Making the password variable global (so that the copy function would grab the updated password post-button press,
as it was otherwise unable to detect generated passwords)
- Learning tkinter to create a functional GUI
- Learning pyinstaller to create a .exe file from my .py project
    - Using --noconsole so cmd doesn't launch
    - Figuring out .ico files and using pyinstaller to replace the default .exe icon
- Uploading to my github repo (I haven't done this since I took MBB 243 - Intro Data Analysis for Molecular Bio & Biochem)
via the terminal
