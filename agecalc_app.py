
from PIL import Image, ImageTk
import datetime
import tkinter as tk
from tkinter import ttk 


window = tk.Tk()

window.geometry("500x600")

window.title("Age calculator")

label1 = tk.Label(text = "Year")
label2 = tk.Label(text = "Month")
label3 = tk.Label(text = "Day")
label4 = tk.Label(text = "Name")

label1.grid(column=0,row=10)
label2.grid(column=0,row=12)
label3.grid(column=0,row=14)
label4.grid(column=0,row=16)

label1_entry = tk.Entry()
label1_entry.grid(column=1,row=10)

label2_entry = tk.Entry()
label2_entry.grid(column=1, row=12)

label3_entry = tk.Entry()
label3_entry.grid(column=1, row=14)

label4_entry = tk.Entry()
label4_entry.grid(column=1,row=16)


def calculate_age():
	print(label1_entry.get())
	print(label2_entry.get())
	print(label3_entry.get())
	print(label4_entry.get())
	print("Button was clicked")
	you = person("You", datetime.date(int(label1_entry.get()), 
											int(label2_entry.get()), 
											int(label3_entry.get())))
	print(you.age())
	text_answer = tk.Text(master = window, height=20,width=30)
	text_answer.grid(column =1, row=20)
	answer_text = "{name} are {age} years old".format(name = you.name, age = you.age())
	text_answer.insert(tk.END, answer_text )


calculate_button = tk.Button(text = "Calculate", command=calculate_age)
calculate_button.grid(column=1,row=18)





#image = Image.open("/Users/andrewlastrapes/Desktop/Old pictures /Chicago 2012/Pics/120509_003.jp")
#image.thumbnail(100,100, image.ANTIALIAS)
#photo = ImageTk.PhotoImage(image)
#label_image = tk.label(image=photo)
#label_image.grid(column=1, row=0)





class person():
	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate

	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year
		return age




window.mainloop()