from tkinter import *
from tkinter.ttk import Combobox 
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title("Sports Information")
root.geometry('1920x1080')

def switch_teams():
    print(var_select.get())


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
    
#Importing Logo
image = Label(logo, image = "")
image.grid( row=0, column=0, sticky="ew")


def save_user_info():
    global name
    global favourite_team

    name = name_entry.get().strip()
    favourite_team = favourite_team_entry.get().strip()

    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Input Error", "Error: Name can only contain letters.")
    elif not favourite_team.replace(" ", "").isalpha():
        messagebox.showerror("Input Error", "Error: Favorite Team can only contain letters.")
    else:
        messagebox.showinfo("Input Accept", "Your details have been saved")

        # Writing user information to the external text file
    with open("user_info.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Favourite Team: {favourite_team}\n")
        file.close()

#asking the user for their name and favourite team
name_label = Label(menu, text="Enter your name:")
name_label.grid(row=1, column=0, padx=2, pady=2)

name_entry = Entry(menu)
name_entry.grid(row=1, column=1, padx=2, pady=2)

favourite_team = Label(menu, text="Enter your favourite team:")
favourite_team.grid(row=2, column=0, padx=2, pady=2)

favourite_team_entry = Entry(menu)
favourite_team_entry.grid(row=2, column=1, padx=2, pady=2)

# Creating the Save User Info button
save_info_button = Button(menu, text="Save Info", command=save_user_info)
save_info_button.grid(column=2, row=1)

#Importing Logo
image = Label(logo, image = "")
image.grid( row=0, column=0, sticky="ew")

def spurs():
    text_spurs = Label(description, text="""Tottenham Hotspur, commonly known as Spurs, is a professional football club based in North London, 
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
    text_spurs.grid(row=1, column=0)

#This will display the starting XI of the team
    squad_spurs = Label(squad, text="Starting XI", font=("Time new Roman", 20), fg="black", bg="white", anchor="center")
    squad_spurs.grid(row=1, column=2)
    spurs_list = Label(squad, text="""Hugo Lloris \n Davinson Sanchez  \n Eric Dier \n Cristian Romero \n Pedro Porro  \n Pierre-Emile Hojbjerg \n Ivan Perisic  \n Dejan kulusevski  \n James Maddison \n Son Heung-Min \n Harry Kane""", font=("Verdana"), fg="black", bg="white", anchor="center", padx=120)
    spurs_list.grid(row=2, column=2)

#This will import the logo from the file
    spurs_img = Image.open("Spurs.jpg")
    #Resizing the Logo itself
    resized_spurs = spurs_img.resize((110,220), Image.ANTIALIAS)
    new_spurs = ImageTk.PhotoImage(resized_spurs)
    image.configure(image=new_spurs, bg='white')
    image.image = new_spurs
    
def chelsea():
    text_chelsea = Label(description, text="""Chelsea Football Club is a renowned and iconic professional football team based in London, England.
    \n Established in 1905, the club has since become one of the most successful and storied football 
    \n institutions in the world. The team's home ground is Stamford Bridge, a historic stadium 
    \n situated in the heart of Fulham, where passionate supporters gather to cheer for their beloved 
    \n Blues. Over the years, Chelsea has experienced numerous highs and lows, but it is their 
    \n triumphs and relentless pursuit of excellence that have etched their name in football folklore.
    \n The club's rise to prominence began in the late 20th century, but it was in the early 21st. 
    \n century when Chelsea truly asserted their dominance on the domestic and international stages.
    \n Under the ownership of Roman Abramovich, the club experienced an era of unprecedented success,
    \n winning multiple English Premier League titles, FA Cups, and League Cups. Notably, Chelsea 
    \n clinched their first-ever UEFA Champions League trophy in 2012, a momentous occasion that will 
    \n forever be etched in the memories of fans.Beyond the silverware, Chelsea has been defined by 
    \n their captivating style of play and a legacy of cultivating exceptional 
    \n talents.""", font=("Verdana", 12), fg='black', bg='white',anchor="w", justify="left")
    text_chelsea.grid(row=1, column=0)

    squad_chelsea = Label(squad, text="Starting XI", font=("Time new Roman", 20), fg="black", bg="white", anchor="center")
    squad_chelsea.grid(row=1, column=2)
    chelsea_list = Label(squad, text="""Kepa Arrizabalaga \n Reece James \n James Wesley \n Fofana \n Benoit Badiashile \n Ben Chilwell \n Enzo Fernandez \n Conor Gallagher \n Mykhailo Mudryk \n Christopher Nkunku \n Armando Broja \n Romelu Lukaku.""", font=("Verdana"), fg="black", bg="white", anchor="center", padx=120)
    chelsea_list.grid(row=2, column=2)

    chelsea_img = Image.open("Chelsea.jpg")
    #Resizing the Logo itself
    resized_chelsea = chelsea_img.resize((250,280), Image.ANTIALIAS)
    new_chelsea = ImageTk.PhotoImage(resized_chelsea)
    image.configure(image=new_chelsea, bg='white')
    image.image = new_chelsea

def liverpool():
    text_liverpool = Label(description, text=""" Liverpool is a vibrant and historic city located in the northwest of England, renowned for its rich 
    \n cultural heritage, maritime history, and passionate football fandom. Situated along the banks of the 
    \n River Mersey, Liverpool has long been a major port city, playing a crucial role in the 
    \n industrial revolution and transatlantic trade during the 18th and 19th centuries. Today, 
    \n it stands as a thriving metropolis that blends the old and the new, captivating visitors with its 
    \n unique charm. One of Liverpool's most prominent features is its strong association with 
    \n The Beatles, the iconic British rock band that revolutionized the music industry 
    \n in the 1960s. The city pays homage to this musical legacy with numerous attractions, including the famous 
    \n Cavern Club, where the Fab Four once performed, and the Beatles Story museum, which takes 
    \n visitors on an immersive journey through their extraordinary career. In addition to 
    \n its musical heritage, Liverpool is celebrated for its remarkable architectural landmarks. The city's 
    \n waterfront, designated as a UNESCO World Heritage site, boasts an array of stunning buildings, 
    \n including the Royal Liver Building, the Cunard Building, and the Port of 
    \n Liverpool Building, collectively known as the Three Graces,  which symbolize the city's maritime 
    \n significance.""" , font=("Verdana", 12), fg='black', bg='white',anchor="w", justify="left")
    text_liverpool.grid(row=1, column=0)

    squad_liverpool = Label(squad, text="Starting XI", font=("Time new Roman",20), fg="black", bg="white", anchor="center")
    squad_liverpool.grid(row=1,column=2)
    liverpool_list = Label(squad, text = """Alisson Becker \n Trent Alexander-Arnold \n Virgil van Dijk \n Ibrahima Konate \n Andrew Robertson \n Thiago Alacantra \n Alexis Mac Allister \n Dominik Szoboszlai \n Mohamed Salah \n Luis Diaz \n Darwin Nunez""", font=("Verdana"), fg="black", bg="white",anchor="center",padx=120)
    liverpool_list.grid(row=2,column=2)

    liverpool_img = Image.open("Liverpool.jpg")
    #Resizing the Logo itself
    resized_liverpool = liverpool_img.resize((190,280), Image.ANTIALIAS)
    new_liverpool = ImageTk.PhotoImage(resized_liverpool)
    image.configure(image=new_liverpool, bg='white')
    image.image = new_liverpool

def man_united():
    text_united = Label(description, text="""Manchester United, commonly known as Man United or simply United, is one of the most iconic 
    \n and historically significant football clubs in the world. Based in Old Trafford, Greater Manchester, 
    \n England, the club has a rich and storied legacy that spans well over a century. Founded 
    \n in 1878 as Newton Heath LYR Football Club, it wasn't until 1902 that the team adopted the 
    \n name Manchester United. Since then, the club has gone on to become one of the most successful 
    \n and widely supported football clubs globally. Throughout its illustrious history, Manchester 
    \n United has amassed an impressive trophy cabinet, boasting numerous domestic and 
    \n international accolades. With a record 20 English Premier League titles, 12 FA Cups, and 5 League Cups, 
    \n the club's domestic dominance is unparalleled. Moreover, United has triumphed on the European 
    \n stage, clinching 3 UEFA Champions League titles and 1 UEFA Europa League trophy. 
    \n These achievements have cemented Manchester United's status as one of the most successful clubs in 
    \n English and European football history. The club's success has been characterized by some of the 
    \n game's most legendary players who have donned the iconic red jersey. """ , font=("Verdana", 12), fg='black', bg='white',anchor="w", justify="left")
    text_united.grid(row=1, column=0)

    squad_united = Label(squad, text="Starting XI", font=("Time new Roman",20), fg="black", bg="white", anchor="center")
    squad_united.grid(row=1,column=2)
    united_list = Label(squad, text = """Andre Onana \n Luke Shaw \n Lisandro Martinez \n Raphael Varane \n Diogo Dalot \n Mason Mount \n Casemiro \n Bruno Fernandes \n Jadon Sancho \n Marcus Rashford \n Antony""", font=("Verdana"), fg="black", bg="white",anchor="center",padx=120)
    united_list.grid(row=2,column=2)

    united_img = Image.open("Manchester United.jpg")
    #Resizing the Logo itself
    resized_united = united_img.resize((200,260), Image.ANTIALIAS)
    new_united = ImageTk.PhotoImage(resized_united)
    image.configure(image=new_united, bg='white')
    image.image = new_united


def man_city():
    text_city = Label(description, text="""Manchester City Football Club, commonly known as Man City, is a prominent English football 
    \n team hailing from the city of Manchester. Established in 1880, the club has experienced a rich 
    \n history with its fair share of ups and downs, ultimately emerging as one of the most successful 
    \n and formidable clubs in modern football. Their home ground is the iconic Etihad Stadium,
    \n where passionate fans congregate to witness scintillating displays of skill and determination.
    \n In recent decades, Manchester City has undergone a transformation that has seen them rise 
    \n to prominence both domestically and internationally. Under the ownership of the Abu Dhabi 
    \n United Group since 2008, the club has enjoyed substantial financial backing, leading to significant 
    \n investments in players, facilities, and coaching staff. This financial injection sparked a 
    \n remarkable period of success for the club.During this period, Man City secured several 
    \n Premier League titles, cementing their status as one of the top teams in English football. Their 
    \n playing style, characterized by fluid attacking football, intricate passing, and high pressing, 
    \n has been masterminded by renowned managers such as Pep Guardiola, who has left an indelible mark 
    \n on the club's philosophy.""" , font=("Verdana", 12), fg='black', bg='white',anchor="w", justify="left")
    text_city.grid(row=1, column=0)

    squad_city = Label(squad, text="Starting XI", font=("Time new Roman",20), fg="black", bg="white", anchor="center")
    squad_city.grid(row=1,column=2)
    city_list = Label(squad, text = """Ederson \n Ruben Dias \n Alymeric Laporte \n Manuel Akanji \n Kyle Walker \n Rodri \n John Stones \n Bernado Silva \n Jack Grealish \n Kevin De Bruyne \n Erling Haaland.""", font=("Verdana"), fg="black", bg="white",anchor="center",padx=120)
    city_list.grid(row=2,column=2)

    city_img = Image.open("Manchester City.jpg")
    #Resizing the Logo itself
    resized_city = city_img.resize((200,230), Image.ANTIALIAS)
    new_city = ImageTk.PhotoImage(resized_city)
    image.configure(image=new_city, bg='white')
    image.image = new_city


def arsenal():
    text_arsenal = Label(description, text="""Arsenal Football Club, commonly known as Arsenal, is one of the most iconic and historically 
    \n significant football teams in the world. Based in London, England, the club was founded in 1886 by workers 
    \n from the Royal Arsenal armaments factory, and it has since become an integral part of 
    \n English football culture. Throughout its illustrious history, Arsenal has experienced both 
    \n remarkable successes and periods of transition. The club's glory days are associated with the tenure 
    \n of Arsene Wenger, a highly respected and influential manager who guided Arsenal to three 
    \n Premier League titles and seven FA Cup victories during his remarkable 22-year 
    \n reign, which lasted from 1996 to 2018. The team's style of play under Wenger was admired for its 
    \n emphasis on attacking football and nurturing young talents, earning Arsenal the moniker 
    \n The Invincibles  during the 2003-2004 season when they went unbeaten in the Premier League. This 
    \n achievement remains one of the most significant milestones in English football history. 
    \n Arsenal's home ground is the iconic Emirates Stadium, a state-of-the-art venue with a capacity of over 
    \n 60,000 spectators..""" , font=("Verdana", 12), fg='black', bg='white',anchor="w", justify="left")
    text_arsenal.grid(row=1, column=0)

    squad_arsenal = Label(squad, text="Starting XI", font=("Time new Roman",20), fg="black", bg="white", anchor="center")
    squad_arsenal.grid(row=1,column=2)
    arsenal_list = Label(squad, text = """Aaron Ramsdale \n Oleksander Zinchenko \n Jurrien Timber \n William Saliba \n Ben White \n Declan Rice \n Martin Odegaard \n Kai Havertz \n Gabriel Martinelli \n Bukayo Saka \n Gabriel Jesus""", font=("Verdana"), fg="black", bg="white",anchor="center",padx=120)
    arsenal_list.grid(row=2,column=2)

    arsenal_img = Image.open("Arsenal.jpg")
    #Resizing the Logo itself
    resized_arsenal = arsenal_img.resize((200,230), Image.ANTIALIAS)
    new_arsenal = ImageTk.PhotoImage(resized_arsenal)
    image.configure(image=new_arsenal, bg='white')
    image.image = new_arsenal


def select_dropdown(event):
    selected_team = menu_var.get()
    if selected_team == "Spurs":
        spurs()
    elif selected_team == "Arsenal":
        arsenal()
    elif selected_team == "Chelsea":
        chelsea()
    elif selected_team == "Liverpool":
        liverpool()
    elif selected_team == "Manchester United":
        man_united()
    elif selected_team == "Manchester City":
        man_city()

#This is the command to exit the window
exit_button = Button(menu, text="Exit", command=root.destroy)
exit_button.grid(column=0, row=0)        


#This is piece of code that shows the combobox
menu_options = ["Arsenal","Chelsea","Liverpool", "Manchester City", "Manchester United", "Spurs"]
menu_var = StringVar()
var_select = Combobox(menu, state="readonly", values = menu_options, textvariable= menu_var)
var_select.set("Select a Team")
var_select.grid(row=0, column=1)
var_select.bind("<<ComboboxSelected>>", select_dropdown)




root.mainloop()
