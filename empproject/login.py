from functools import partial
from admin import *
from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
from UserPanal import *
from utility import *
class Login(Frame):
	def __init__(self,master):
		super().__init__(master)	
		self.l1=Label(self,bg='light blue',bd=2,text='User Name',font=('algerian',12))
			
		self.l2=Label(self,bg='light blue',bd=2,text='Password',font=('algerian',12))
		eobj=Util()	
		self.t1=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		self.t2=Entry(self,bg='light blue',show='*',bd=3,font=('olephant',12,'bold'),justify='center')
			
		self.b1=Button(self,font=('algerian',13),bd=2,bg='gray',text='login',padx=8,pady=5,command=lambda:eobj.check(self.t1.get(),self.t2.get()))
		#partial(eobj.check,self.t1.get(),self.t2.get()))
		
		
		self.columnconfigure(0, pad=5)
		self.columnconfigure(1, pad=5)
		
		
		self.rowconfigure(0, pad=5)
		self.rowconfigure(1, pad=5)
		self.rowconfigure(2, pad=5)
			
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
			
		self.l2.grid(row=1,column=0)
		self.t2.grid(row=1,column=1)
			
		self.b1.grid(columnspan=2)
			
		self.pack()
	
root=Tk()
obj=Login(root)
root.title('Login Form')
root.geometry('500x150')
root.mainloop()
			
			
			
			
			
			
			
			
			