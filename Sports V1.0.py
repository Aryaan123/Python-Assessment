from cgitb import text
import tkinter
from tkinter import *
from tkinter.ttk import Combobox 
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import json
root = Tk()
root.title("Sports Information")
root.geometry('800x500')

#creating the main frames with column and rows
root.grid_rowconfigure((0,1,2), weight=1)
root.grid_columnconfigure((0,1,2), weight=1)

#create the main grids
menu = Frame(root, bg='White', width=350, height=100, pady=3, highlightbackground="black", highlightthickness=2)
heading = Frame(root, bg='White', width=700, height=100, pady=3, highlightbackground="black", highlightthickness =2)
logo = Frame(root, bg='White', width=500, height=100, pady=3, highlightbackground="black", highlightthickness=2)
description = Frame(root, bg='White', width=1000, height=400, pady=3, highlightbackground="black", highlightthickness=2)
squad = Frame(root, bg='White', width=500, height=400, pady=3, highlightbackground="black", highlightthickness=2)

heading.grid_rowconfigure((0), weight=1)
heading.grid_columnconfigure((0,1,2), weight=1)

menu.grid_rowconfigure((0), weight=1)
menu.grid_columnconfigure((0,1,2), weight=1)

logo.grid_rowconfigure((0), weight=1)
logo.grid_columnconfigure((0), weight=1)

#layout of grids
menu.grid(row=0, column=0,  sticky="nesw")
heading.grid(row=0, column=1, sticky="nesw")
logo.grid(row=0, column=2, sticky="nesw")
description.grid(row=1, column=0, columnspan=2, rowspan=2, sticky="nesw")
squad.grid(row=1, column=2,  rowspan=2, sticky="nesw")

title = Label(heading, text="Sports Feed", font=("Times New Roman", 25), fg='black', bg='white')
title.grid(row=0, column=1)

text=tk.Text(width = 40, height=4, font=("Helvetica", 32))

#This function will display the whole Spurs information
def spurs():
    text_description = Label(description, text="""Tottenham Hotspur, commonly known as Spurs, is a professional football club based in North London, 
    \n England. Established in 1882, Tottenham Hotspur has grown to become one of the most iconic and 
    \n successful football clubs in the country. With a rich history and a passionate fanbase, the 
    \n club has left an indelible mark on the world of football. Tottenham Hotspurs home stadium is 
    \n the magnificent Tottenham Hotspur Stadium, which was opened in 2019. The stadium, with its 
    \n impressive architecture and state-of-the-art facilities, has quickly become a symbol of the 
    \n clubs ambition and progress. It has a seating capacity of over 62,000, making it one of the 
    \n largest stadiums in the country. Over the years, Tottenham Hotspur has achieved significant 
    \n success both domestically and internationally. The club has won numerous trophies, including 
    \n the English League Championship, the FA Cup, and the UEFA Cup. Notably, in the 1960-61 season, 
    \n Tottenham Hotspur became the first English club in the 20th century to win the league and cup
    \n double. One of the hallmarks of Tottenham Hotspurs success has been its commitment to nurturing 
    \n talent and playing attractive, attacking football. """, font=("Verdana", 12), fg='black', bg='white',anchor="w", justify="left")

    text_description.grid(row=1, column=0)
#Importing Logo
    spurs_img = Image.open("Spurs.jpg")
#Resizing the Logo itself
    resized_spurs = spurs_img.resize((110,220), Image.ANTIALIAS)
    new_spurs = ImageTk.PhotoImage(resized_spurs)
#Posting the logo onto the GUI
    image = Label(logo, image = new_spurs)
    image.grid( row=0, column=0, sticky="ew")

#This will display the starting XI of the team
    squad_description = Label(squad, text="Starting XI", font=("Time new Roman", 20), fg="black", bg="white", anchor="center")
    squad_description.grid(row=1, column=2)
    squad_list = Label(squad, text="""Hugo Lloris \n Davinson Sanchez  \n Eric Dier \n Cristian Romero \n Pedro Porro  \n Pierre-Emile Hojbjerg \n Ivan Perisic  \n Dejan kulusevski  \n James Maddison \n Son Heung-Min \n Harry Kane""", font=("Verdana",), fg="black", bg="white", anchor="center", padx=120)
    squad_list.grid(row=2, column=2)

#This is the command to exit the window
exit_button = Button(menu, text="Exit", command=root.destroy)
exit_button.grid(column=0, row=0)


def spurs_logo():
    #Importing Logo
    spurs_img = Image.open("Spurs.jpg")
#Resizing the Logo itself
    resized_spurs = spurs_img.resize((115,226), Image.ANTIALIAS)
    new_spurs = ImageTk.PhotoImage(resized_spurs)
#Posting the logo onto the GUI
    image = Label(logo, image = new_spurs)
    image.grid( row=0, column=0, sticky="ew")
    

def select_dropdown(event):
    selected_team = menu_var.get()
    if selected_team == "Spurs":
        spurs()

        
#This is piece of code that shows the combobox
menu_options = ["Spurs"]
menu_var = StringVar()
var_select = Combobox(menu, state="readonly", values = menu_options, textvariable= menu_var)
var_select.set("Select a Team")
var_select.grid(row=0, column=1)
var_select.bind("<<ComboboxSelected>>", select_dropdown)

text = tk.Text(description, wrap=tk.WORD)
text.grid(row=1, column=0)



root.mainloop()
