import tkinter


def button_press():
    print("hhh")


def title_change():
    mile = int(input_data.get())
    print(mile + 9)
    calculated_label.config(text=round(mile * 1.609344, 2))
    print("kkk")


window = tkinter.Tk()
window.title("Mile to Km")
window.minsize(width=400, height=178)

miles_label = tkinter.Label(text='Miles', font=('Arial', 14, "bold"))
miles_label.grid(column=3, row=1)
miles_label.config(padx=22, pady=22)
km_label = tkinter.Label(text='Km', font=('Arial', 14, "bold"))
km_label.grid(column=3, row=2)

calculated_label = tkinter.Label(text='0', font=('Arial', 14, "bold"))
calculated_label.grid(column=2, row=2)

is_equal_label = tkinter.Label(text='is equal to', font=('Arial', 14, "bold"))
is_equal_label.grid(column=1, row=2)
is_equal_label.config(padx=22, pady=22)

calculate_button = tkinter.Button(width=10, height=1, bg='blue', command=title_change)
calculate_button.grid(column=2, row=3)
calculate_button.config(padx=20)
input_data = tkinter.Entry(width=10)
input_data.grid(column=2, row=1)
input_data.config(bg="red")
a = input_data.get()
# my_label.config(text="change")
# new_button = tkinter.Button(width=3, height=2, bg='blue', command=title_change)
# new_button.grid(column=3, row=0)


window.mainloop()
