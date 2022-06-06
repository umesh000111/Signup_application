from cProfile import label
import code
from curses import window
import fractions
from tkinter import *
from curses import window
from tkinter import messagebox
import ast
from turtle import heading

window = Tk()
window.title("SignUp")
window.geometry("925x500+300+250")
window.configure(bg = '#fff')
window.resizable(False,False)

def signup():
	username = user.get()
	password = code.get()
	conform_password = conform_code()

	if password==conform_code:
		try:
			file=open("datasheet",'r+')
			d=file.read()
			r.ast.literal_eval(d)

			dict2 = {username:password}
			r.update(dict2)
			file.truncate(0)
			file.close()

			file=open('datasheet.txt','w')
			w=file.write(str(r)) 

			messagebox.showinfo('Singup','Sucessfully sign up')

		except:
			file=open('datasheet.txt','w')
			pp=str({'Username':'password'})
			file.write(pp)
			file.close()
	else:
		messagebox.showinfo('Invalied','Both password should match')

img = PhotoImage(file="img.png")
Label(window,image=img,border=0,bg="white").place(x=-80,y=0)

frame = Frame(window,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

heading = Label(frame,text="Sign up",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
heading.place(x=100,y=5)

#####--------------------------------------------------------------------
#
#   this block for take username block
#
#####----------------------------------------------------------------
def on_enter(e):
	user.delete(0,'end')
def on_leave(e):
	if user.get()=="":
		user.insert(0,"Username")
user = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)



Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

#####--------------------------------------------------------------------
#
#   this block for take password block
#
#####----------------------------------------------------------------
def on_enter(e):
	code.delete(0,'end')
def on_leave(e):
	if code.get()=="":
		code.insert(0,"password")
code = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)



Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

#####--------------------------------------------------------------------
#
#   this block for take Conform Password block
#
#####----------------------------------------------------------------
def on_enter(e):
	conform_code.delete(0,'end')
def on_leave(e):
	if conform_code.get()=="":
		conform_code.insert(0,"Conform Password")
conform_code = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
conform_code.place(x=30,y=200)
conform_code.insert(0,"Conform Password")
conform_code.bind("<FocusIn>",on_enter)
conform_code.bind("<FocusOut>",on_leave)



Frame(frame,width=295,height=2,bg="black").place(x=25,y=225)

######--------------------------
#
#     sing up button
#
#####-------------------------
Button(frame,width=39,pady=7,text="Sign up",bg="#57a1f8",fg="white",border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="I have an account?",fg="black",bg="white",font=("Microsoft Yahei UI Light",9))
label.place(x= 90,y=340)

singin=Button(frame,width=6,text="Sign in",border=0,bg="white",cursor="hand2",fg="#57a1f8")
singin.place(x= 200,y=340)

window.mainloop()