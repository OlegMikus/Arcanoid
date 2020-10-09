from tkinter import *
import sqlite3
from game_main import game
from re import *


def get_address(address):
	pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
	is_valid = pattern.match(address)
	if is_valid:
		return True
	else:
		return False


def register():

	def clean():
		email.delete(0, END)
		name.delete(0, END)
		password.delete(0, END)
		confirm.delete(0, END)

	def delete():
		conn = sqlite3.connect('arcade_date.db')
		c = conn.cursor()
		c.execute("DELETE FROM arcdata WHERE oid=" + del_box.get())
		conn.commit()
		conn.close()

	def name_chek(records):

		for record in records:
			if record[1] == name.get():
				return False
		return True

	def reg():

		conn = sqlite3.connect('arcade_date.db')
		c = conn.cursor()
		c.execute("SELECT *, oid FROM arcdata")
		rec = c.fetchall()
		if password.get() == confirm.get() and get_address(email.get()) and name_chek(rec):
			c.execute("INSERT INTO arcdata VALUES (:email, :nama, :password, :score)",
					{
						'email': email.get(),
						'nama': name.get(),
						'password': password.get(),
						'score': game()
					})
			conn.commit()
			conn.close()
			top.destroy()

		else:
			warning = Label(top, text='Wrong input data, please try again')
			warning.place(relx=0.5, y=400, anchor="c", height=50, width=250, bordermode=OUTSIDE)
			clean()
		print(rec)

	top = Toplevel()
	top.title('LogIn')
	top.resizable(False, False)
	top.geometry('400x500+{}+{}'.format(top.winfo_screenwidth() // 2 - 200, top.winfo_screenheight() // 2 - 250))

	email_label = Label(top, text="Email: ", font='Helvetica 11')
	email_label.place(relx = 0.25, y=60, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	email = Entry(top, font='Helvetica 14', bg='grey')
	email.place(relx = 0.5, y=90, anchor="c", height=30, width=250, bordermode=OUTSIDE)

	name_label = Label(top, text="Name: ", font='Helvetica 11')
	name_label.place(relx = 0.25, y=120, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	name = Entry(top, font='Helvetica 14', bg='grey')
	name.place(relx = 0.5, y=150, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	
	password_label = Label(top, text="Password: ", font='Helvetica 11')
	password_label.place(relx = 0.28, y=180, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	password = Entry(top, show="*",font='Helvetica 14', bg='grey')
	password.place(relx = 0.5, y=210, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	
	confirm_label = Label(top, text="Confirm your password: ", font='Helvetica 11')
	confirm_label.place(relx = 0.39, y=240, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	confirm = Entry(top, show="*",font='Helvetica 14', bg='grey')
	confirm.place(relx = 0.5, y=270, anchor="c", height=30, width=250, bordermode=OUTSIDE)

	play_butt = Button(top, text='Play!', font='Helvetica 14',
					   background="#555", foreground="#ccc", command = reg)
	play_butt.place(relx = 0.5, y=350, anchor="c", height=50, width=250, bordermode=OUTSIDE)

	back_butt = Button(top, text='Back', font='Helvetica 14',
					background="#555", foreground="#ccc", command=top.destroy)
	back_butt.place(x = 25, y=15, anchor="c", height=30, width=50, bordermode=OUTSIDE)


	del_box = Entry(top, font='Helvetica 14', bg='grey')
	del_box.place(relx = 0.5, y=310, anchor="c", height=30, width=250, bordermode=OUTSIDE)

	delete_bt = Button(top, text='delete', command=delete)
	delete_bt.place(relx=0.5, y=450, anchor="c", height=50, width=250, bordermode=OUTSIDE)
