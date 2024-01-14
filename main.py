from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

# creating a window
root = Tk()
root.resizable(False, False)
root.title("Головоломка для самых умных")
# color
back = "#373737"
fore = "#AFAFAF"
# window geometry
WIDTH = 422
HEIGHT = 730
POS_X = (root.winfo_screenwidth() // 2) - (WIDTH // 2)
POS_Y = (root.winfo_screenheight() // 2) - (HEIGHT // 2)
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
# set the background color
root["bg"] = back
# button VIEW COLLECTED
seeButton = Button(root, text="Посмотреть, как должно быть", width=47)
seeButton.place(x=10, y=600)
# seeButton.bind("<Button-1>", seeStart)
# seeButton.bind("<ButtonRelease>", seeEnd)
# button START GAME
startButton = Button(root, text="СТАРТ", width=47)
startButton.place(x=10, y=640)
# startButton["command"] = startNewRound
# reset button
resetButton = Button(root, text="Сброс", width=47)
resetButton.place(x=10, y=680)
# resetButton["command"] = resetPictures
# number of moves made and record
textSteps = Label(root, bg=back, fg=fore)
textSteps.place(x=10, y=550)
textRecords = Label(root, bg=back, fg=fore)
textRecords.place(x=10, y=570)
# difficulty label
Label(root, bg=back, fg=fore, text="Сложность:").place(x=267, y=550)
# name of difficulty levels
itemDiff = [
    "Только начал",
    "Немного почитал",
    "Знаю print()",
    "Понял сортировку",
    "Изучил лабиринт",
    "Гик!",
]
# drop-down menu
diffCombobox = ttk.Combobox(root, width=15, values=itemDiff, state="readonly")
diffCombobox.place(x=270, y=570)
# diffCombobox.bind("<<ComboboxSelected>>", lambda e: refreshText())
diffCombobox.current(0)

image = BooleanVar()
image.set(True)
radio01 = Radiobutton(
    root,
    text="Космос      ",
    variable=image,
    value=True,
    activebackground=back,
    bg=back,
    fg=fore,
)
radio02 = Radiobutton(
    root,
    text="Природа  ",
    variable=image,
    value=False,
    activebackground=back,
    bg=back,
    fg=fore,
)
# radio01["command"] = isCheckImage
# radio02["command"] = isCheckImage
radio01.place(x=150, y=540)
radio02.place(x=150, y=568)

# start game
root.mainloop()
