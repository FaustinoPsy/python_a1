from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from matplotlib import image


#criar janela
jan= Tk()
jan.title('SisTecNew')
jan.geometry('600x300')
jan.configure(background='white')
jan.resizable(width=False,height=False)
jan.attributes("-alpha",0.85)
#imagens
logo = PhotoImage(file="img/logo.png")


#widgets
leftFrame= Frame(jan,width=200,height=300, bg='MIDNIGHTBLUE',relief='raise')
leftFrame.pack(side=LEFT)

RightFrame= Frame(jan,width=397,height=300, bg='MIDNIGHTBLUE',relief='raise')
RightFrame.pack(side=RIGHT)

LogoLabel = Label(leftFrame, image=logo, bg='MIDNIGHTBLUE')

LogoLabel.place(x=50,y=100)

userLabel = Label(RightFrame, text="usuário:", font=("Century Gothic", 20), bg='MIDNIGHTBLUE',fg="white")
userLabel.place(x=5,y=100)

userInput= ttk.Entry(RightFrame, width=30)
userInput.place(x=150,y=110)

passLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg='MIDNIGHTBLUE',fg="white")
passLabel.place(x=5,y=150)

passInput= ttk.Entry(RightFrame, width=30)
passInput.place(x=150,y=160)

LoginButton = ttk.Button(RightFrame,text="Login",width=30)
LoginButton.place(x=150,y=200)


CadButton = ttk.Button(RightFrame,text="Cadastrar",width=20)
CadButton.place(x=190,y=240)


jan.mainloop()