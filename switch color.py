from tkinter import *
root=Tk()
root.maxsize(200,200)
def f1():

    global color
    if color=='light':
        root.config(bg='black')
        color='dark'
    else:
        root.config(bg='white')
        color='light'
    
        
color='light'    
x=Button(root,text='switch',font='Algerian14', bg='black',fg='white',command=f1).pack()

root.mainloop()
