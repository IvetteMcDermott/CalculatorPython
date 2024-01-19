from tkinter import *

# Creates the window
root = Tk()

root.title('First calculator Tk')
root.geometry("320x270")
root.configure(background='#9ccddb')

# remove titlebar
root.overrideredirect(True)

# allows to move the window around, will be drag from the title label
def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


# create the fake bar
title_bar = Frame(root, relief='raised', bd=1)
title_bar.grid(row=0, column=0, columnspan=11)
font_size = 14
title_label = Label(title_bar, text='            Calculator with Python              ', bg='#5790ab', fg='#072d44', pady=4, font=('Helvetic', font_size))
title_label.grid(row=0, column=0)

# bind the titlebar for move
title_label.bind('<B1-Motion>', move_app)

# btn that allows to close the window
btn_close=Button(root, text='X', width=3, command=root.destroy, justify='left', bg='#072d44', fg='#d0d7e1')
btn_close.grid(row=0, column=4, padx=5)

# TRANSPARENCY if want to set some 
# root.attributes("-alpha", 0.9)


e = Entry(root, width=15, borderwidth=2, font=1.05, justify='right')
e.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="ewns")

# btn properties examples
# button = root.Button(
#                    bd=10,
#                    bg="grey",
#                    fg="red",
#                    command=quit,
#                    activeforeground="Orange",
#                    activebackground="blue",
#                    font="Andalus",
#                    height=2,
#                    highlightcolor="purple",
#                    justify="right",
#                    padx=10,
#                    pady=10,
#                    relief="groove",
#                    )


# func to clear e
def clear_e():
    e.delete(0, END)

# func to collect the entry
def button_click(number):
    current= e.get()
    clear_e()
    e.insert(0, str(current) + str(number))
    return

# func to validate nums
def nums_exist(x):
    if x == '' or x is None:
        e.insert(0, 'ERROR')
        e.after(3000, clear_e)
    else:
        pass

# func add 
def btn_add():
    # get the first number and check is valid
    n1 = e.get()
    nums_exist(n1)
    # assign global variables so that can be use in next function
    global num_1
    global operator
    operator = '+'
    num_1 = int(n1)
    # clear the e so the second number for the op can be entry
    clear_e()

def btn_subt():
    # get the first number and check is valid
    n1 = e.get()
    nums_exist(n1)
    # assign global variables so that can be use in next function
    global num_1
    global operator
    operator = '-'
    num_1 = int(n1)
    # clear the e so the second number for the op can be entry
    clear_e()

def btn_mult():
    # get the first number and check is valid
    n1 = e.get()
    nums_exist(n1)
    # assign global variables so that can be use in next function
    global num_1
    global operator
    operator = '*'
    num_1 = int(n1)
    # clear the e so the second number for the op can be entry
    clear_e()

def btn_div():
    # get the first number and check is valid
    n1 = e.get()
    nums_exist(n1)
    # assign global variables so that can be use in next function
    global num_1
    global operator
    operator = '/'
    num_1 = int(n1)
    # clear the e so the second number for the op can be entry
    clear_e()

def result():
    # get the second number and check is valid
    n2 = e.get()
    nums_exist(n2)
    num_2 = int(n2)
    # clear the e so the result  for the op can be entry
    clear_e()
    # global that allows to use the result as n1 and continue chained ops 
    global result
    # conditional for the op to process
    if operator == '+':
        result = int(num_1) + int(num_2)
        e.insert(0, result)
    elif operator == '-':
        result = int(num_1) - int(num_2)
        e.insert(0, result)
    elif operator == '*':
        result = int(num_1) * int(num_2)
        e.insert(0, result)
    elif operator == '/':
        result = int(num_1) / int(num_2)
        e.insert(0, result)
    else:
        e.insert(0, 'ERROR')


# Buttons

btn_1 = Button(root, text="1", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(1))
btn_2 = Button(root, text="2", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(2))
btn_3 = Button(root, text="3", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(3))

btn_4 = Button(root, text="4", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(4))
btn_5 = Button(root, text="5", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(5))
btn_6 = Button(root, text="6", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(6))

btn_7 = Button(root, text="7", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(7))
btn_8 = Button(root, text="8", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(8))
btn_9 = Button(root, text="9", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(9))

btn_0 = Button(root, text="0", padx=53, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click(0))
btn_dot = Button(root, text=". ", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=lambda: button_click('.'))

# functional buttons
btn_clear = Button(root, text="C", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=clear_e)

btn_equal = Button(root, text="=", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=result)

btn_adding = Button(root, text="+", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=btn_add)
btn_subtraction = Button(root, text=" -", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=btn_subt)
btn_multiplication = Button(root, text=" *", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=btn_mult)
btn_division = Button(root, text=" /", padx=18, pady=4, bg='#5790ab', bd=1, fg='#d0d7e1', activebackground='#064469', font=("Helvetica"), command=btn_div)

# btns grid
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)

btn_0.grid(row=5, column=0, columnspan=2)
btn_dot.grid(row=5, column=2)

btn_equal.grid(row=5, column=4, rowspan=2)

btn_clear.grid(row=2, column=4)

btn_adding.grid(row=2, column=3)
btn_subtraction.grid(row=3, column=3)
btn_multiplication.grid(row=4, column=3)
btn_division.grid(row=5, column=3)

# Run the app's main loop or nothing happens
root.mainloop()