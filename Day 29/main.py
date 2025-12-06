import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ["*", "^", ";", ":", "!", "~", "&", "%", "$", "#", "@", "(", ")", "[", "}", "{", "]"]

    password_letter = [random.choice(alphabets) for _ in range(random.randint(8, 10))]
    password_num = [str(random.randint(0, 9)) for _ in range(random.randint(2, 4))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_symbol + password_num + password_letter

    random.shuffle(password_list)      #shuffling the original list
    hard_password = "".join(password_list)
    my_password_entry.insert(0, hard_password)
    pyperclip.copy(hard_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    new_data = {
        my_website_entry.get(): {
            "email": my_Email_entry.get(),
            "password": my_password_entry.get()
        }
    }
    if len(my_website_entry.get()) == 0 or len(my_password_entry.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_confirm = messagebox.askokcancel(title=my_website_entry.get(), message=f"These are the details entered:"
                                                                 f"\nEmail: {my_Email_entry.get()}"
                                                                 f"\nWebsite: {my_website_entry.get()}"
                                                                 f"\nPassword: {my_password_entry.get()}"                                                        f"\n Is it ok to save?")
        if is_confirm:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                    my_password_entry.delete(0, "end")
                    my_website_entry.delete(0, "end")

# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    with open("data.json") as file:
        data = json.load(file)
        try:
            messagebox.showinfo(title="Password Info", message=f"Email: {data[my_website_entry.get()]["email"]}"
                                       f"\nPassword: {data[my_website_entry.get()]["password"]}")
        except KeyError:
            messagebox.showinfo(title="Error", message=f"This website password is not saved.")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message=f"No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #
windows = tkinter.Tk()
windows.title("Password Manger")
windows.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Entry
my_website_entry = tkinter.Entry(width=35)
my_website_entry.focus()
my_website_entry.grid(row=1, column=1, columnspan=2)

my_Email_entry = tkinter.Entry(width=35)
my_Email_entry.insert(0, "abhinavkesarwani45@gmail.com")
my_Email_entry.grid(row=2, column=1, columnspan=2)

my_password_entry = tkinter.Entry(width=21)
my_password_entry.grid(row=3, column=1)

#Label

website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password: ")
password_label.grid(row=3, column=0)

#Button

generate = tkinter.Button(text="Generate Password", command=pass_generator)
generate.grid(row=3, column=2)

add = tkinter.Button(text="Add", width=36, command=add_pass)
add.grid(row=4, column=1, columnspan=2)

search = tkinter.Button(text="Search", command=search, width=10)
search.grid(row=1, column=2)

windows.mainloop()