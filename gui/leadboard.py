from tkinter import *

def leader():
	
	root = Tk()
	root.title('Arcade')
	root.resizable(False, False)
	root.geometry('400x500+{}+{}'.format(root.winfo_screenwidth()//2-200, root.winfo_screenheight()//2-250))
	
	label = Label(root, text = 'LeaderBoard', font='Helvetica 14', background="#555", foreground="#ccc")
	label.place(relx = 0.5, y=200, anchor="c", height=50, width=250, bordermode=OUTSIDE)
	

	back_butt = Button(root, text='Back', font='Helvetica 14', background="#555", foreground="#ccc", command=root.destroy)
	back_butt.place(x = 25, y=15, anchor="c", height=30, width=50, bordermode=OUTSIDE)


	root.mainloop()
