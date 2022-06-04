
# importing Dependencies 

from tkinter import *

root = Tk()

root.geometry("500x500")
root.title('Notepad')
# ============================Functions=================



# ========================== Tool area =====================
tool = Frame(master = root,background = '#bdf2d5',height=50)
tool.pack(fill=X)

openbt = Button(master=tool , background='#112b3c',activebackground='#205375',text= 'OPEN', fg= 'white',width= 10,height = 1,activeforeground= 'white',relief= FLAT)
openbt.pack(ipadx=1,pady= 10,padx=5,side=LEFT)

savebt = Button(master=tool , background='#112b3c',activebackground='#205375',text= 'SAVE', fg= 'white',width= 10,height = 1,activeforeground= 'white',relief= FLAT)
savebt.pack(ipadx=1,pady= 10,padx=15,side=LEFT)

Voicebt = Button(master=tool , background='#112b3c',activebackground='#205375',text= 'VOICE..', fg= 'white',width= 10,height = 1,activeforeground= 'white',relief= FLAT)
Voicebt.pack(ipadx=1,pady= 10,padx=5,side=LEFT)

# ========================== Text area =====================

text_frame = Frame(master = root,background = 'yellow')
text_frame.pack(fill=BOTH)

note  =Text(master=text_frame,font=('Arial',10,'bold'))
note.pack(fill=BOTH)

root.mainloop()