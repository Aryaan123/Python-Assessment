import tkinter
from tkinter import *
from tkinter.ttk import Combobox 
from PIL import ImageTk, Image
from tkinter import font
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

#This is piece of code that shows the combobox
text_team = Label(menu, text="Tottenham Hotspurs", font=("Times New Roman", 25), fg='black', bg='white' )
text_team.grid(row=0, column=0)


#This is to display the text description
text_description = Label(description, text="""Tottenham Hotspur, commonly known as Spurs, is a professional football club based in North London, 
England. Established in 1882, Tottenham Hotspur has grown to become one of the most iconic and
successful football clubs in the country. With a rich history and a passionate fanbase, the 
club has left an indelible mark on the world of football. Tottenham Hotspurs home stadium is 
the magnificent Tottenham Hotspur Stadium, which was opened in 2019. The stadium, with its 
impressive architecture and state-of-the-art facilities, has quickly become a symbol of the
clubs ambition and progress. It has a seating capacity of over 62,000, making it one of the 
largest stadiums in the country. Over the years, Tottenham Hotspur has achieved significant 
success both domestically and internationally. The club has won numerous trophies, including
the English League Championship, the FA Cup, and the UEFA Cup. Notably, in the 1960-61 season,
Tottenham Hotspur became the first English club in the 20th century to win the league and cup
double. One of the hallmarks of Tottenham Hotspurs success has been its commitment to nurturing
young talent and playing attractive, attacking football. The club has a renowned youth academy 
that has produced several notable players who have gone on to achieve great success both at the
club and international level. Spurs have also had the privilege of hosting some of the game's 
finest talents, including players like Jimmy Greaves, Glenn Hoddle, and Gareth Bale. Tottenham 
Hotspur has also enjoyed memorable European campaigns. In recent years, under the guidance 
of manager Mauricio Pochettino, the club reached the final of the UEFA Champions League in 
the 2018-2019 season. Although they narrowly missed out on the title, the team’s spirited 
performances and remarkable journey captivated fans worldwide. Off the pitch, Tottenham 
Hotspur has been involved in various community initiatives, aiming to make a positive impact
on society. The club's foundation works tirelessly to engage with local schools and charities,
using the power of football to inspire and improve lives. This commitment to social 
responsibility has further endeared the club to its fans and the wider community. The fanbase of 
Tottenham Hotspur is known for its unwavering loyalty and passionate support. Spurs fans, often 
referred to as "Yid Army," create a vibrant atmosphere at home games, cheering on their beloved 
team with fervor. The North London Derby against rival Arsenal is one of the most fiercely 
contested fixtures in English football and further fuels the passion and rivalry between 
the two clubs. As Tottenham Hotspur looks to the future, they continue to strive for success 
on all fronts. With talented players, a world-class stadium, and a dedicated fanbase, the club 
has the ingredients for continued prosperity. Under the stewardship of current manager Ange 
Postecoglou, Tottenham Hotspur aims to compete for major honors and bring glory to their loyal 
supporters. In conclusion, Tottenham Hotspur's rich history, commitment to youth development,
attractive style of play, and passionate fanbase have solidified the club's position as one 
of the giants of English football. As they continue to push for success, Spurs remain a force 
to be reckoned with, both domestically and on the European stage""", font=("Verdana", 12), fg='black', bg='white',anchor="w", justify="left")

text_description.grid(row=1, column=0)

#This is to display the squad list
squad_description = Label(squad, text="Squad List", font=("Time new Roman", 20), fg="black", bg="white", anchor="center")
squad_description.grid(row=1, column=2)

squad_list = Label(squad, text="Hugo Lloris \n Fraser Forster \n Brandon Austin \n Davinson Sanchez \n Emerson Royal \n Eric Dier \n Cristian Romero \n Pedro Porro \n Ben Davies \n Sergio Reguilon \n Djed Spence \n Oliver Skipp \n Pierre-Emile Hojbjerg \n Ivan Perisic \n Ryan Sessegnon \n Dejan kulusevski \n Rodrigo Bentancur \n Yves Bissouma \n James Maddison \n Son Heung-Min \n Richarlison \n Harry Kane", font=("Verdana",), fg="black", bg="white", anchor="center", padx=120)
squad_list.grid(row=2, column=2)

#Importing Logo
spurs_img = Image.open("Spurs.jpg")

#Resizing the Logo itself
resized_spurs = spurs_img.resize((115,226), Image.ANTIALIAS)
new_spurs = ImageTk.PhotoImage(resized_spurs)

#Posting the logo onto the GUI
image = Label(logo, image = new_spurs)
image.grid( row=0, column=0, sticky="ew")


root.mainloop()
