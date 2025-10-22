from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = ""
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)

    label_title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    # ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label_title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_title.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # if reps % 2 == 0:
        #     checkmarks.config(text=CHECKMARK)
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += CHECKMARK
        checkmarks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_title = Label(text="Timer", font=(
    FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, )
label_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="02-Intermediate/j_pomodoro_project/tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

checkmarks = Label(text="", font=(
    FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)
window.mainloop()
