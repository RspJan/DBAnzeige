# -*- coding: utf-8 -*-
from Tkinter import *


def button_action():
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        welcome_label.config(text="Deine zuletzt verwendete Haltestelle wird nun geladen.")
    else:
        entry_text = "Nach der Haltestelle " + entry_text + " wird gesucht!" 
        welcome_label.config(text=entry_text)
	fenster.destroy()

fenster = Tk()
fenster.wm_geometry("620x85+20+20")
fenster.title("Bahnhof / Haltestelle auswählen")


my_label = Label(fenster, text="Gib einen Ort ein: ")

welcome_label = Label(fenster)

eingabefeld = Entry(fenster, bd=5, width=61)

fv = Button(fenster, text="Fernverkehr", command=button_action)
rv = Button(fenster, text="Regionalverkehr", command=button_action)
zv = Button(fenster, text="alle Züge", command=button_action)
bv = Button(fenster, text="Ortsverkehr", command=button_action)
av = Button(fenster, text="alle Linien", command=button_action)

my_label.grid(row = 0, column = 0)
eingabefeld.grid(row = 0, column = 1)
fv.place(x = 0, y = 30, width=120, height=30)
rv.place(x = 125, y = 30, width=120, height=30)
zv.place(x = 250, y = 30, width=120, height=30)
bv.place(x = 375, y = 30, width=120, height=30)
av.place(x = 500, y = 30, width=120, height=30)
welcome_label.place(x = 0, y = 62)

mainloop()
