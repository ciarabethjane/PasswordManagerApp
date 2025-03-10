# References used to make this project
# Udemy Course - 100 Days of Code: The Complete Python Pro Bootcamp
# Writing to an existing CSV file: https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/
# Message Boxes: https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/

from tkinter import *
from tkinter import messagebox
from csv import writer
import random
from random import choice, randint, shuffle

# --- PASSWORD GENERATOR ------------------------------- #
def passwordGen():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']

    numOfLetters = random.randint(8,10)
    numOfSymbols = random.randint(2,4)
    numOfNumbers = random.randint(2,4)

    passLetters = [random.choice(letters) for _ in range(numOfLetters)]
    passSymbols = [random.choice(symbols) for _ in range(numOfSymbols)]
    passNumbers = [random.choice(numbers) for _ in range(numOfNumbers)]

    password_list = passLetters + passSymbols + passNumbers
    shuffle(password_list)

    random.shuffle(password_list)

    "".join(password_list)
    pwordEntry.insert(0, password_list)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def addButton():
    site = siteEntry.get()
    uname= emailEntry.get()
    password = pwordEntry.get()

    if len(site) == 0 or len(uname) == 0 or len(password) == 0:
        detailsAvail = messagebox.showerror("Error", "Not all fields contain information")
    else:
        details = [site, uname, password]
        userSave = messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {uname} \nPassword: {password} \nDo you want to save this information?")
        if userSave:
            with open('PasswordManager\data.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(details)
                siteEntry.delete(0,END)
                pwordEntry.delete(0,END)
                f_object.close()






# ---------------------------- UI SETUP ------------------------------- # 

root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

myCanvas = Canvas(height=200, width=200)
logoImage = PhotoImage(file="logo.png")
myCanvas.create_image(100, 100, image=logoImage)
myCanvas.grid(row=0, column=1, rowspan=1, columnspan=1)

siteLabel = Label(root, text="Website:")
siteLabel.grid(row=1, column=0, rowspan=1, columnspan=1)
siteEntry = Entry(root, width=35)
siteEntry.grid(row=1, column=1, rowspan=1, columnspan=2)
siteEntry.focus()

emailLabel = Label(root, text="Email/Username:")
emailLabel.grid(row=2, column=0, rowspan=1, columnspan=1)
emailEntry = Entry(root, width=35)
emailEntry.grid(row=2, column=1, rowspan=1, columnspan=2)
emailEntry.insert(0, "emailaddress@email.com")

pwordLabel = Label(root, text="Password:")
pwordLabel.grid(row=3, column=0, rowspan=1, columnspan=1)
pwordEntry = Entry(root, width=21)
pwordEntry.grid(row=3, column=1, rowspan=1, columnspan=1)
pwordButton = Button(root, text="Generate Password", command=passwordGen, activebackground="blue", activeforeground="white", width=15)
pwordButton.grid(row=3, column=2, rowspan=1, columnspan=1)

addButton = Button(root, text="Add", command=addButton , activebackground="blue", activeforeground="white", width=36)
addButton.grid(row=4, column=1, rowspan=1, columnspan=2)




root.mainloop()