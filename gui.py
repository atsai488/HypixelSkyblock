from skyblock import *
import tkinter
import customtkinter
import time

#system settings

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Skyblock Profile Loader")

profileList = []

def individualProfile(choice):
    profileNum = choice[8:9]
    players = choice[10:len(choice)-1]
    clearScreen()
    
    title = customtkinter.CTkLabel(app, text="Profile: " + profileNum)
    title.pack(padx = 10, pady = 10)
    
    playerNames = customtkinter.CTkLabel(app, text = players)
    playerNames.pack(padx = 10)
    profileNum = int(profileNum)
    moneybal = getPlayerMoney(data, profileNum)
    money = customtkinter.CTkLabel(app, text = getPlayerMoney(data, moneybal))
    money.pack(padx = 10)
    
    
    
    back = customtkinter.CTkButton(app, text="Back", command = setUp)
    back.pack()
    
    


#returns string list of players
def selectionMenu():  
    global data 
    data = skyblockProfile(link.get())
    profileList = skyblockMates(data)
    clearScreen()
    title = customtkinter.CTkLabel(app, text="Choose a profile")
    title.pack(padx = 10, pady=10)
    
    profiles = customtkinter.CTkComboBox(app, values=profileList, hover=True, command = individualProfile)
    profiles.pack(padx = 10, pady= 10)

    
    
    
def clearScreen():
    for widget in app.winfo_children():
        widget.destroy()    








#UI
def setUp():
    clearScreen()
    title = customtkinter.CTkLabel(app, text="Insert Minecraft Username")
    title.pack(padx = 10, pady=10)
    global link
    global username
    username = tkinter.StringVar() 
    link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=username)
    link.pack()

    finished = customtkinter.CTkLabel(app, text="")
    finished.pack(padx = 10, pady =10)

    process = customtkinter.CTkButton(app, text="GO", command=selectionMenu)
    process.pack(padx = 10, pady = 10)

    
    
    
    

if __name__ == '__main__':
    setUp()
    app.mainloop()