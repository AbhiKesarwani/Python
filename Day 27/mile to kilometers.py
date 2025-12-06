import tkinter

windows = tkinter.Tk()
windows.title("Mile to Km converter")
windows.minsize(width = 300, height= 300)

#Miles Entry
input = tkinter.Entry(width=10)
input.place(x=100,y=100)
mile_label = tkinter.Label(text="Miles",font=("Calibri",14))
mile_label.place(x=150,y=100)



def km_converter():
    miles = float(input.get())
    km = round(miles * 1.609,2)
    output_label.config(text=f"{km}")

#button
calculate_button = tkinter.Button(text="Calculate",command=km_converter)
calculate_button.place(x=100,y=200)

#km output-Entry
output_label = tkinter.Label(font=("Calibri", 14))
output_label.place(x=100, y=150)
km_label = tkinter.Label(text = "Km",font=("Calibri",14))
km_label.place(x=150,y=150)
#output.insert(END, int=)





windows.mainloop()