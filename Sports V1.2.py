from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox 
from PIL import ImageTk, Image
import json
from tkinter import Toplevel, Label, Entry, Button

root = Tk()
root.title("Sports Information")
root.geometry('1920x1080')

#this helps read from the json file
with open("teams.json", "r") as pp:
    team_list = json.load(pp)
    pp.close()

#this function will clear all information about a team
def clear_all():
    description_lbl.config(text="")
    squad_list.config(text="")
    image.config(image="")

def select_dropdown(event):
    selected_team = menu_var.get()
    selected_team = selected_team.lower()
    info = team_list[selected_team]
    description_txt = info[0]
    team_txt = info[1]
    description_lbl.config(text=description_txt)
    squad_list.config(text=team_txt)

    #This will import the logo from the file
    image_logo = Image.open(f"{selected_team}.jpg")
    #Resizing the Logo itself
    resized_image = image_logo.resize((150,210), Image.ANTIALIAS)
    resized_image = ImageTk.PhotoImage(resized_image)
    image.configure(image=resized_image, bg='white')
    image.image = resized_image

#creating the main frames with column and row
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

menu.grid_rowconfigure((0,1,2,3), weight=1)
menu.grid_columnconfigure((0,1), weight=1)

logo.grid_rowconfigure((0), weight=1)
logo.grid_columnconfigure((0), weight=1)

description.grid_rowconfigure((0), weight=1)
description.grid_columnconfigure((0), weight=1)

squad.grid_rowconfigure((0,1), weight=1)
squad.grid_columnconfigure((0), weight=1)

#layout of grids
menu.grid(row=0, column=0,  sticky="nesw")
heading.grid(row=0, column=1, sticky="nesw")
logo.grid(row=0, column=2, sticky="nesw")
description.grid(row=1, column=0, columnspan=2, rowspan=2, sticky="nesw")
squad.grid(row=1, column=2,  rowspan=2, sticky="nesw")

#this is the heading for the squad list
squad_heading = Label(squad, text="Starting XI", font=("Time new Roman", 20), fg="black", bg="white", anchor="center")
squad_heading.grid(row=0, column=0, sticky="n")

#these labels are going to help change the description
description_lbl = Label(description, text="" "", font=("Verdana", 12), fg='black', bg='white', justify="left")
description_lbl.grid(row=0, column=0, sticky = "w")

#this will help change the squad list
squad_list = Label(squad, text="", font=("Verdana",), fg="black", bg="white", anchor="center", padx=120)
squad_list.grid(row=1, column=0, sticky = "n")
    

title = Label(heading, text="Sports Feed", font=("Times New Roman", 25), fg='black', bg='white')
title.grid(row=0, column=1)

#Importing Logo
image = Label(logo, image = "")
image.grid( row=0, column=0, sticky="ew")

#this is the options of the different favourite teams
favourite_team_options = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton Town", "Manchester City", "Manchester United", "Newcastle", "Nottingham Forest", "Sheffield United", "Spurs", "West Ham", "Wolves"]

#This is piece of code that shows the combobox
menu_options = ["Arsenal","Chelsea","Liverpool", "Manchester City", "Manchester United", "Spurs"]
menu_var = StringVar()
var_select = Combobox(menu, state="readonly", values = menu_options, textvariable= menu_var)
var_select.set("Select a Team")
var_select.grid(row=0, column=0, rowspan=3, columnspan=3)
var_select.bind("<<ComboboxSelected>>", select_dropdown)

def get_user_details():
    global user_details_window

    # Create a new Toplevel window
    user_details_window = Toplevel(root)
    user_details_window.title("User Details")
    user_details_window.geometry("300x200")

    # Create labels and entry fields for user details
    name_label = Label(user_details_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = Entry(user_details_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    

    favourite_team_label = Label(user_details_window, text="Favorite Team:")
    favourite_team_label.grid(row=1, column=0, padx=5, pady=5)
    favourite_team_entry = Combobox(user_details_window, state="readonly", values=favourite_team_options)
    favourite_team_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a button to save user details and link it to the `save_user_info` function
    save_details_button = Button(user_details_window, text="Save", command=lambda: save_user_info(name_entry.get(), favourite_team_entry.get()))
    save_details_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

def save_user_info(name, favourite_team):
    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Input Error", "Error: Name can only contain letters.")
    else:
        messagebox.showinfo("Input Accept", "Your details have been saved")

        # Writing user information to the external text file
        with open("user_info.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Favourite Team: {favourite_team}\n")
            file.close()



get_details_button = Button(menu, text="Get User Details", command=get_user_details)
get_details_button.grid(column=0, row=2, columnspan=2)

#This is the command to exit the window
exit_button = Button(menu, text="Exit", command=root.destroy)
exit_button.grid(column=0, row=2)    

#This command is to clear all the details of the different teams
clear_all_button = Button(menu, text="Clear All", command=clear_all)
clear_all_button.grid(column=1, row=2)

root.mainloop()