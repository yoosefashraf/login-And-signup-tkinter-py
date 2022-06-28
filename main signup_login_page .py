from tkinter import *
from tkinter import messagebox
import ast
#  Window app
log = Tk()
log.title("emt")
log.geometry('925x500+300+200')
log.configure(bg='#fff')
log.resizable(False,False)

def signin():
  username=user.get()
  password=code.get()

  file = open('emtsheet.txt','r')
  d = file.read()
  r= ast.literal_eval(d)
  file.close()

  # print(r.keys())
  # print(r.values())

  if username in r.keys() and password==r[username]:
    screen= Toplevel(log)
    screen.title("App")
    screen.geometry('925x500+300+200')
    screen.config(bg="white")

    Label(screen,text='Github@"yoosefashraf"',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

    screen.mainloop()
  
  else:
    messagebox.showerror('Invalid','invalid username or password')
# Screen 2 
def signup_command():
  window = Toplevel(log)
  window.title("emt")
  window.geometry('925x500+300+200')
  window.configure(bg='#fff')
  window.resizable(False,False)
  
  def signup():
      username=user.get()
      password=code.get()
      conform_password=conform_code.get()
      if password==conform_password:
          try:
            file=open('emtsheet.txt','r+')
            d = file.read()
            r=ast.literal_eval(d)
            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()
            file=open('emtsheet.txt','w')
            w = file.write(str(r))
            messagebox.showinfo('Signup','Sucessfully sign up')
  
          except:
             file=open('emtsheet.txt','w')
             pp = str({'Username':'password'})
             file.write(pp)
             file.close()
  
      else:
        messagebox.showerror('Invalid','Both Password should match')       
  def sign():
  
    window.destroy()
  # image setting
  img = PhotoImage(file='img/sign.png')
  Label(window,image=img,bg='white').place(x=50,y=90)
  frame=Frame(window,width=350,height=390,bg='white')
  frame.place(x=480,y=50)
  # Word Sign in  setting
  heading = Label(frame,text='Sign up To Emt Products',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',19,'bold'))
  heading.place(x=20,y=5)
  
            # username
            # User NAme Setting 
  def on_enter(e):
       user.delete(0,'end')
  def on_leave(e):
      if user.get()=='':
           user.insert(0,'Username')
  
  user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
  user.place(x=30,y=80)
  user.insert('0', 'Username')
  user.bind('<FocusIn>',on_enter)
  user.bind('<FocusOut>',on_leave)
  Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
  
  # password
  def on_enter(e):
    code.delete(0,'end')
  def on_leave(e):
    if code.get()=='':
      code.insert(0,'Password')
  
  code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
  code.place(x=30,y=150)
  code.insert('0', 'Password')
  code.bind('<FocusIn>',on_enter)
  code.bind('<FocusOut>',on_leave)
  
  
  Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
  
  # conform password
  def on_enter(e):
      conform_code.delete(0,'end')
  def on_leave(e):
    if conform_code.get()=='':
       conform_code.insert(0,'Conform Password')
  conform_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
  conform_code.place(x=30,y=220)
  conform_code.insert('0', 'Conform Password')
  conform_code.bind('<FocusIn>',on_enter)
  conform_code.bind('<FocusOut>',on_leave)
  
  
  Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
  
            # Button sign in and label
  
  Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
  label = Label(frame,text="I have an account",fg='black',bg='white',font=('Microsoft YaHei UI Light',9)) 
  label.place(x=90,y=340)
  
  sign_in = Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
  
  
  sign_in.place(x=200,y=340)
  
  window.mainloop()   
 
# Set Image 
img = PhotoImage(file='img/login.png')
Label(log,image=img,bg='white').place(x=50,y=50)

frame=Frame(log,width=350,height=350,bg='white')
frame.place(x=480,y=70)

# Word Sign in  setting
heading = Label(frame,text='Sign in To Emt Products',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',19,'bold'))
heading.place(x=20,y=5)

# User NAme Setting 
def on_enter(e):
  user.delete(0,'end')
def on_leave(e):
  name=user.get()
  if name=='':
    user.insert(0,'Username')


user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert('0', 'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


# password Setting 
def on_enter(e):
  code.delete(0,'end')
def on_leave(e):
  name=code.get()
  if name=='':
    code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert('0', 'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

# Button sign in and label

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',11)) 
label.place(x=50,y=270)
if True:  
  # log.close
  sign_up = Button(frame,width=5,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)

sign_up.place(x=215,y=270)



log.mainloop()