
# importing Dependencies 

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import FileDialog

root = Tk()

root.geometry("500x500")
root.title('Notepad')
# ============================Functions=================

def save():
    pass
def open():
    pass
def voice():
    pass

# ========================== Tool area =====================
tool = Frame(master = root,background = '#bdf2d5',height=70,width=300)
tool.pack(fill=BOTH,side='top')

openbt = Button(master=tool , background='#ce9461',activebackground='#dea057',text= 'OPEN', fg= 'white',width= 10,height = 1,activeforeground= 'white',relief= FLAT)
openbt.pack(ipadx=1,pady= 10,padx=5,side=LEFT)

savebt = Button(master=tool , background='#ce9461',activebackground='#dea057',text= 'SAVE', fg= 'white',width= 10,height = 1,activeforeground= 'white',relief= FLAT)
savebt.pack(ipadx=1,pady= 10,padx=15,side=LEFT)

Voicebt = Button(master=tool , background='#ce9461',activebackground='#dea057',text= 'VOICE..', fg= 'white',width= 10,height = 1,activeforeground= 'white',relief= FLAT)
Voicebt.pack(ipadx=1,pady= 10,padx=5,side=RIGHT)

exitbt = Button(master=tool , background='#ce9461',activebackground='#dea057',text= 'EXIT', fg= 'white',width= 10,height = 1,activeforeground= 'white',relief= FLAT)
exitbt.pack(ipadx=1,pady= 10,padx=5,side=RIGHT)

# ========================== Text area =====================

note = Text(master= root,width=300,height = 300,bg='#e3fcbf',fg='#15133c',font=('Segoe UI',12),relief=FLAT,selectbackground='#ffe459',selectforeground='#152d35')
note.pack(fill='both',ipadx= 15,ipady=10)


root.mainloop()