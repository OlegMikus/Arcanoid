from tkinter import *
from register import register
import sqlite3

def login():

	def click():
		conn = sqlite3.connect('users.db')




		#text = name.get()
		#text1 = password.get()
		#label = Label(root, text=text)
		#label.pack()

		#label1 = Label(root, text=text1)
		#label1.pack()

	root = Tk()
	root.title('Arcade')
	root.resizable(False, False)
	root.geometry('400x500+{}+{}'.format(root.winfo_screenwidth()//2-200, root.winfo_screenheight()//2-250))
	



	name_label = Label(root, text="Name: ", font='Helvetica 11')
	name_label.place(relx = 0.25, y=170, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	name = Entry(root, font='Helvetica 14', bg='grey')
	name.place(relx = 0.5, y=200, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	
	password_label = Label(root, text="Password: ", font='Helvetica 11')
	password_label.place(relx = 0.28, y=230, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	password = Entry(root, show="*",font='Helvetica 14', bg='grey')
	password.place(relx = 0.5, y=260, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	

	play_butt = Button(root, text='Play!', font='Helvetica 14', background="#555", foreground="#ccc", command=click)
	play_butt.place(relx = 0.5, y=400, anchor="c", height=50, width=250, bordermode=OUTSIDE)

	back_butt = Button(root, text='Back', font='Helvetica 14', background="#555", foreground="#ccc", command=root.destroy)
	back_butt.place(x = 25, y=15, anchor="c", height=30, width=50, bordermode=OUTSIDE)


	root.mainloop()
