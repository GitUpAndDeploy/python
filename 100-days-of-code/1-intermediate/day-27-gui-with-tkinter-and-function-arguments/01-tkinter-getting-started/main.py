from tkinter import *

window = Tk()

window.title("GUI Test")
window.minsize(width=500, height=300)


# My label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# Will not show without this, packer packs a label on the screen
my_label.pack(side = "top")

# # Update a pre assigned value, similar to updating a dictionary
# # Option 1
# my_label["text"] = "New label like a dictionary"
# # Option 2
# my_label.config(text = "New label with config")


# def button_clicked():
#   print("Click detected")
#   my_label.config(text = "Button clicked")

# # Buttons
# button = Button(text = "Click me", command=button_clicked)
# button.pack()

# # Entry
# input = Entry()
# print(input.get())
# input.pack()

# Make the text field content as the label
def button_clicked():
  print("Click detected")
  new_text = input.get()
  my_label.config(text = new_text)

# Buttons
button = Button(text = "Click me", command=button_clicked)
button.pack()

# Entry
input = Entry()
input.pack()










window.mainloop()
