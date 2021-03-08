#from functools import partial
from admin import *
from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
from UserPanal import *
#from Attendence import *
class Util:
	empno=0
	def check(self,userid,passwd):
		#print(userid,passwd)
		con=connect(db='employee',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		try:
			i=cur.execute("select usertype,userid from login where userid='%s' and passwd='%s'"%(userid,passwd))
			rs=cur.fetchall()
			if rs[0][0]=='admin':
				r1=Tk()
				ob1=Admin(r1)
				r1.title('Admin Form')
				r1.geometry('600x100')
				r1.mainloop()
			else:
				r10=Tk()
				Util.empno=rs[0][1]
				#print(Util.empno)
				ob1=MyPanel(r10)
				r10.title('User Form')
				r10.geometry('600x100')
				r10.mainloop()
		except Exception as ex:
			print(ex)
			msg.showerror('Error Info','either username or password is wrong')