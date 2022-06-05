
# importing Dependencies 

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox




# ============================Functions=================

def saveas():
    try:
        file = filedialog.asksaveasfile(defaultextension= '*.txt',filetypes=[('Text file','*.txt'),('Python file','.py'),('All file','*.*')])
        file.write(str(note.get('1.0',END)))
    except Exception as e :
        error = messagebox.askokcancel(title = 'ERROR:(',message=f'{e} Occured')
    finally:
        file.close()
    
def open():
    pass
def voice():
    pass
def exit():
    pass



root = Tk()

root.geometry("500x500")
root.title('Notepad')

# ========================== Tool area =====================
tool = Frame(master = root,background = '#bdf2d5',height=70,width=300)
tool.pack(fill=BOTH,side='top')

openbt = Button(master=tool , background='#ce9461',activebackground='#dea057',text= 'OPEN', fg= 'white',
                width= 10,height = 1,activeforeground= 'white',relief= FLAT,command= open
                )
openbt.pack(ipadx=1,pady= 10,padx=5,side=LEFT)

saveasbt = Button(master=tool , background='#ce9461',activebackground='#dea057',text= 'SAVE AS', fg= 'white',
                width= 10,height = 1,activeforeground= 'white',relief= FLAT,command= saveas
                )
saveasbt.pack(ipadx=1,pady= 10,padx=15,side=LEFT)


Voicebt = Button(master=tool , background='#ce9461',activebackground='#dea057',text= 'VOICE..', fg= 'white',
                width= 10,height = 1,activeforeground= 'white',relief= FLAT,command= voice
                )
Voicebt.pack(ipadx=1,pady= 10,padx=5,side=RIGHT)

exitbt = Button(master=tool , background='#ce9461',activebackground='#dea057',text= 'EXIT', fg= 'white',
                width= 10,height = 1,activeforeground= 'white',relief= FLAT,command= exit
                )
exitbt.pack(ipadx=1,pady= 10,padx=5,side=RIGHT)

# ========================== Text area =====================

note = Text(master= root,width=300,height = 300,bg='#e3fcbf',fg='#15133c',font=('Segoe UI',12),relief=FLAT,selectbackground='#ffe459',selectforeground='#152d35')
note.pack(fill='both',ipadx= 15,ipady=10)


root.mainloop()