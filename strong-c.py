from tkinter import *
import math

# click enter to make work
# change ** to ^ or do other math module
# 3 buttons, one copies just text, one copies just answer, one copies both


root = Tk()
root.title("Calculator!")
root.configure(bg="dark grey")
root.geometry("485x220")
# root.resizable(width=False, height=False)


def enterb(x):
    answer.config(state='normal')
    answer.delete(0, END)

    try:
        (eval(screen.get()) * 0)

    except Exception:
        answer.insert(0, "Enter Calculations Correctly")
        answer.config(state='disabled')
        return

    answer.insert(0, round(eval(screen.get()), 4))
    root.clipboard_clear()
    root.clipboard_append(eval(screen.get()))
    root.update()

    answer.config(state='disabled')


def equals1():
    answer.config(state='normal')
    answer.delete(0, END)

    # screen.get().replace("^", "**")

    try:
        (eval(screen.get()) * 0)

    except Exception:
        answer.insert(0, "Enter Calculations Correctly")
        answer.config(state='disabled')
        return

    answer.insert(0, round(eval(screen.get()), 4))
    root.clipboard_clear()
    root.clipboard_append(screen.get())
    root.update()

    answer.config(state='disabled')


def equals2():
    answer.config(state='normal')
    answer.delete(0, END)

    # screen.get().replace("^", "**")

    try:
        (eval(screen.get()) * 0)

    except Exception:
        answer.insert(0, "Enter Calculations Correctly")
        answer.config(state='disabled')
        return

    answer.insert(0, round(eval(screen.get()), 4))
    root.clipboard_clear()
    root.clipboard_append(eval(screen.get()))
    root.update()

    answer.config(state='disabled')


def equals3():
    answer.config(state='normal')
    answer.delete(0, END)

    # screen.get().replace("^", "**")

    try:
        (eval(screen.get()) * 0)

    except Exception:
        answer.insert(0, "Enter Calculations Correctly")
        answer.config(state='disabled')
        return

    answer.insert(0, round(eval(screen.get()), 4))
    root.clipboard_clear()
    root.clipboard_append(screen.get() + " = " + str(round(eval(screen.get()), 4)))
    root.update()

    answer.config(state='disabled')


screen = Entry(root, width=63, borderwidth=10, state='normal', font="times 10")
answer = Entry(root, width=63, borderwidth=10, state='disabled', font="times 10")
b1 = Button(root, text="Copy:Input", padx=13, pady=0, bg="grey", font="times 15", command=equals1)
b2 = Button(root, text="Copy:Answer", padx=10, pady=0, bg="grey", font="times 15", command=equals2)
b3 = Button(root, text="Copy:Both", padx=12, pady=0, bg="grey", font="times 15", command=equals3)
text1 = Label(root, text="Guleds Great Calculator!", padx=101, pady=10, bg="black", fg="yellow", font="times 20 underline")
textexp = Label(root, text='Clicking any button or the "Enter" key will generate an answer, use ** for exponent', padx=16, pady=10, bg="black", fg="yellow", font="times 10")
text2 = Label(root, text="Input:", padx=22, pady=10, bg="black", fg="yellow", font="times 10")
text3 = Label(root, text="Answer:", padx=15, pady=10, bg="black", fg="yellow", font="times 10")
text4 = Label(root, text="Buttons:", padx=14, pady=10, bg="black", fg="yellow", font="times 10")


screen.bind("<Return>", enterb)

screen.grid(row=7, column=2, padx=1, pady=1, columnspan=3)
answer.grid(row=9, column=2, padx=1, pady=1, columnspan=3)
b1.grid(row=10, column=2, padx=1, pady=1)
b2.grid(row=10, column=3, padx=1, pady=1)
b3.grid(row=10, column=4, padx=1, pady=1)
text1.grid(row=4, column=1, padx=1, pady=1, columnspan=4)
textexp.grid(row=5, column=1, padx=1, pady=1, columnspan=4)
text2.grid(row=7, column=1, padx=1, pady=1)
text3.grid(row=9, column=1, padx=1, pady=1)
text4.grid(row=10, column=1, padx=1, pady=1)


root.mainloop()
