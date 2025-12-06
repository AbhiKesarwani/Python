import tkinter
from  tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list =[]
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
import pandas
def password_saver():
    website_output=website_entry.get()
    password_output=password_entry.get()
    email_output = email_entry.get()

    if website_output == "" or email_output == "" or password_output=="":
        messagebox.showwarning(title="OOPS",message="Please don't leave any field empty")

    else:
        is_yes = messagebox.askyesno(title="Confirm",message=f"Are you want to save your email and password?\nEmail: {email_output}\nPassword: {password_output}")
        if is_yes:
            with open("password_file.txt",mode="a") as file:
                data = file.write(f"{website_output}| {email_output} | {password_output}\n")
            website_entry.delete(0,"end")  #delete according to index
            password_entry.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = tkinter.Canvas(width=200,height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry=tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_entry=tkinter.Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"abhinavkesarwani38@gmail.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry=tkinter.Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password = tkinter.Button(text="Generate Password",command=generate_password)
generate_password.grid(row=3,column=2)

add= tkinter.Button(text="Add",width=36,command=password_saver)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()
