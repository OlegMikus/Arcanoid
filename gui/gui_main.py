from tkinter import *
from log import login
from register import register
from leadboard import leader
#from PIL import ImageTk, Image


root = Tk()
root.title('Arcade')
root.resizable(False, False)
root.geometry('400x500+{}+{}'.format(root.winfo_screenwidth()//2-200, root.winfo_screenheight()//2-250))

log_butt = Button(root, text='Log in & Play!', font='Helvetica 14', background="#555", foreground="#ccc", command=login)
log_butt.place(relx=0.5, y=220, anchor="c", height=50, width=250, bordermode=OUTSIDE)

reg_butt = Button(root, text='Sign in & Play!', font='Helvetica 14', background="#555", foreground="#ccc", command=register)
reg_butt.place(relx=0.5, y=280, anchor="c", height=50, width=250, bordermode=OUTSIDE)
#
# lead_board_butt = Button(root, text='Leader Board', font='Helvetica 14', background="#555", foreground="#ccc", command=leader)
# lead_board_butt.place(relx=0.5, y=340, anchor="c", height=50, width=250, bordermode=OUTSIDE)
#
exit_butt = Button(root, text='Exit', font='Helvetica 14', background="#555", foreground="#ccc", command=root.quit)
exit_butt.place(relx=0.5, y=400, anchor="c", height=50, width=250, bordermode=OUTSIDE)

root.mainloop()
