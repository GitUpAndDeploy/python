from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def miles_to_km():
  km = float(miles_input.get()) * 1.60934
  km_result_label.config(text = f"{km}")

calculate_button = Button(text = "Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
