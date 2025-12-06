import tkinter

windows = tkinter.Tk()
#windows.minsize(width=100, height=100)
windows.title("Mile to Km Converter")
windows.config(padx=20, pady=20)

miles_entry = tkinter.Entry(width=20)
miles_entry.grid(row=0, column=1)
miles_entry.focus()

miles_label = tkinter.Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(row=0, column=2)

km_label = tkinter.Label(text="Km", font=("Arial",14,"bold"))
km_label.grid(row=1, column=2)

equal_label = tkinter.Label(text="is equal to",font=("Arial",14))
equal_label.grid(row=1, column=0)

km_label = tkinter.Label(text=0, font=("Arial", 14))
km_label.grid(row=1, column=1)

def converter():
    km = float(miles_entry.get()) * 1.609
    km_label.config(text=km)


calc_button = tkinter.Button(text="Calculate", command=converter)
calc_button.grid(row=2, column=1)

windows.mainloop()