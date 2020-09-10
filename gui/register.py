from tkinter import *

def register():
	
	def submit():
		conn = sqlite3.connect('users_book.db')

		c.cour







	root = Tk()
	root.title('Arcade')
	root.resizable(False, False)
	root.geometry('400x500+{}+{}'.format(root.winfo_screenwidth()//2-200, root.winfo_screenheight()//2-250))
	



	name_label = Label(root, text="Name: ", font='Helvetica 11')
	name_label.place(relx = 0.25, y=120, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	name = Entry(root, font='Helvetica 14', bg='grey')
	name.place(relx = 0.5, y=150, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	
	password_label = Label(root, text="Password: ", font='Helvetica 11')
	password_label.place(relx = 0.28, y=180, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	password = Entry(root, show="*",font='Helvetica 14', bg='grey')
	password.place(relx = 0.5, y=210, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	
	confirm_label = Label(root, text="Confirm your password: ", font='Helvetica 11')
	confirm_label.place(relx = 0.39, y=240, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	confirm = Entry(root, show="*",font='Helvetica 14', bg='grey')
	confirm.place(relx = 0.5, y=270, anchor="c", height=30, width=250, bordermode=OUTSIDE)

	

	play_butt = Button(root, text='Play!', font='Helvetica 14', background="#555", foreground="#ccc", command=root.destroy)
	play_butt.place(relx = 0.5, y=400, anchor="c", height=50, width=250, bordermode=OUTSIDE)

	back_butt = Button(root, text='Back', font='Helvetica 14', background="#555", foreground="#ccc", command=root.destroy)
	back_butt.place(x = 25, y=15, anchor="c", height=30, width=50, bordermode=OUTSIDE)

	root.mainloop()
