
# importing Dependencies 

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from turtle import title


# =========================== Global Variable=====================
font_size = 12
font_color = (colorchooser.askcolor(title = 'Pick a color'))[1]
# ============================Functions=================

def exit():
    if note.get('1.0', END):
        savmsg  = messagebox.askokcancel(title= "SAVE FILE",message='save the file before exiting')
        if savmsg:
            saveas()
            root.destroy()
        else:
            root.destroy()


def saveas():
    try:
        file = filedialog.asksaveasfile(defaultextension= '*.txt',filetypes=[('Text file','*.txt'),('Python file','.py'),('All file','*.*')])
        file.write(str(note.get('1.0',END)))
    except Exception as e :
        error = messagebox.askokcancel(title = 'ERROR:(',message=f'{e} Occured')
    finally:
        file.close()
    
def open():
    if note.get('1.0',END):
        savmsg  = messagebox.askokcancel(title= "SAVE FILE",message='save the file before exiting')
        
        if savmsg:
            saveas()
        else:

            try:  
                file = filedialog.askopenfile(defaultextension='*.txt')
                note.delete('1.0',END)
                note.insert('1.0',file.read())
            except FileNotFoundError:
                msg = messagebox.askokcancel(title="File cannot open",message= "Check whether the file is existed")
            except AttributeError:
                return None


def voice():
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

note = Text(master= root,width=300,height = 300,bg='#e3fcbf',fg='#15133c',font=('Segoe UI',font_size),relief=FLAT,selectbackground='#ffe459',selectforeground='#152d35')
note.pack(fill='both',ipadx= 15,ipady=10)


root.mainloop()