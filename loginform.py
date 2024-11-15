from tkinter import *

def login_successful():
    print("Login Successful!")

def check_credentials():
    entered_username = tun.get('1.0', END)[:-1]
    entered_password = tpw.get('1.0', END)[:-1]

    
    if entered_username and entered_password:
        login_successful()
    else:
        print("Incorrect username and password!")

# Main window setup
window = Tk()
window.title("login Window")
window.geometry("400x400")

# Labels and text fields
un = Label(window,text="Username:")
pw = Label(window,text="Password:")

tun = Text(window,height=2,width=20)
tpw = Text(window,height=2,width=20)

# Button and function
btn = Button(window,text="Login", command=check_credentials)

# Placement of elements in the grid
un.grid(column=0,row=0)
tun.grid(column=1,row=0)
pw.grid(column=0,row=1)
tpw.grid(column=1,row=1)
btn.grid(column=0,row=2)

window.mainloop()
