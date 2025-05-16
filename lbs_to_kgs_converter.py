from tkinter import *

#Function that contains formula for converting
def lbs_to_kgs():
    lbs = float(lbs_input.get())
    kgs = lbs * 0.45359237
    rounded_kgs_number = round(kgs, 4)
    kgs_result_label.config(text=f"{rounded_kgs_number}")


#creating the window
display = Tk()
display.title("Lbs to Kgs Converter")
display.config(padx=70, pady=40)

lbs_input = Entry(width=7)
lbs_input.grid(column=1, row=0)

lbs_label = Label(text="Lbs")
lbs_label.grid(column=2, row=0)

is_equals_to_label = Label(text="is equal to")
is_equals_to_label.grid(column=0, row=1)

kgs_result_label = Label(text="0")
kgs_result_label.grid(column=1, row=1)

kgs_label = Label(text="Kgs")
kgs_label.grid(column=2, row=1)

button_to_calculate = Button(text="Calculate", command=lbs_to_kgs)
button_to_calculate.grid(column=1, row=2)


display.mainloop()