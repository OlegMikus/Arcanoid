from tkinter import *
from game_main import game
import sqlite3


def login():

	# def name_chek(records):
	#
	# 	for record in records:
	# 		if record[1] == name.get():
	# 			return record
	# 	return True
	#
	# def log():
	# 	conn = sqlite3.connect('arcade_date.db')
	# 	c = conn.cursor()
	#
	# 	c.execute("SELECT *, oid FROM arcdata")
	# 	rec = c.fetchall()
	# 	print(rec)
	#
	# 	records = ''
	#
	# 	for record in rec:
	# 		records += str(record[0]) + '\t' + str(record[4]) + '\n'
	# 	lab = Label(top, text=records).pack()
	#
	# 	conn.commit()
	# 	conn.close()

	top = Toplevel()
	top.title('LogIn')
	top.resizable(False, False)
	top.geometry('400x500+{}+{}'.format(top.winfo_screenwidth() // 2 - 200, top.winfo_screenheight() // 2 - 250))

	name_label = Label(top, text="Name: ", font='Helvetica 11')
	name_label.place(relx = 0.25, y=170, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	name = Entry(top, font='Helvetica 14', bg='grey')
	name.place(relx = 0.5, y=200, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	
	password_label = Label(top, text="Password: ", font='Helvetica 11')
	password_label.place(relx=0.28, y=230, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	password = Entry(top, show='*', font='Helvetica 14', bg='grey')
	password.place(relx=0.5, y=260, anchor="c", height=30, width=250, bordermode=OUTSIDE)
	
	play_butt = Button(top, text='Play!', font='Helvetica 14', background="#555", foreground="#ccc", command=game)
	play_butt.place(relx=0.5, y=400, anchor="c", height=50, width=250, bordermode=OUTSIDE)

	back_butt = Button(top, text='Back', font='Helvetica 14', background="#555", foreground="#ccc", command=top.destroy)
	back_butt.place(x=25, y=15, anchor="c", height=30, width=50, bordermode=OUTSIDE)
