
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

import tkinter
import math
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    windows.after_cancel(timer)   #stopped timer
    timer_label.config(text="Timer", fg=GREEN)   #changing timer label
    canvas.itemconfig(timer_text,text="00:00")   #changing canvas time
    marks=""
    check_marks.config(text=marks)   #changing check marks
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        timer_count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        timer_count_down(WORK_MIN*60)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def timer_count_down(count):
    count_min = count//60
    count_sec = count%60
    if count_sec < 10:   #Dynamic Typing
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = windows.after(1000,timer_count_down,count-1)     #1000 is a time in milliseconds
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for check in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
windows = tkinter.Tk()
windows.title("Pomodoro Technique")
windows.config(bg=YELLOW,padx=100,pady=50)
#windows.minsize(width=500,height=500)


timer_label = tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=("Arial black",50,"bold"))
timer_label.grid(column=1,row=0)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,122,text="00:00",fill="white",font=(FONT_NAME,24,"bold"))
canvas.grid(row=1,column=1)

start_button = tkinter.Button(text="Start",bg=YELLOW,font=("Calibri",20,"italic"), highlightthickness=0,command=start_timer)
start_button.grid(row=3,column=0)

reset_button = tkinter.Button(text="Reset",bg=YELLOW,font=("Calibri",20,"italic"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=3,column=2)

check_marks = tkinter.Label(font = (20),bg=YELLOW,fg=GREEN)
check_marks.grid(row=3,column=1)
windows.mainloop()