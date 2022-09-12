from tkinter import *
import math
root = Tk() # root (main) window
top = Frame(root) # create frame
top.pack(side='top') # pack frame in main window
hwtext = Label(top, text='Hello, World! The sine of')
hwtext.pack(side='left')
r = StringVar() 
r.set('1.2') 
r_entry = Entry(top, width=6, textvariable=r)
r_entry.pack(side='left')
s = StringVar() 

def comp_s():
   global s
   s.set('%g' % math.sin(float(r.get()))) # construct string
compute = Button(top, text='equals', command=comp_s)
compute.pack(side='left')
s_label = Label(top, textvariable=s, width=18)
s_label.pack(side='left')
root.mainloop()