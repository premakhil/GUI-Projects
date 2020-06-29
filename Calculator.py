from tkinter import *
import tkinter.font as font
import re


root=Tk()
root.title('Calculator')



box=Entry(root,width=35,borderwidth=15)
box.grid(row=0,column=0,columnspan=3)


def click(a):
    current=box.get()
    box.delete(0,last=END)
    box.insert(0,str(current)+str(a))



def equal():
    second_num=box.get()
    box.delete(0,last=END)
    
    if math=='addition':

        box.insert(0,final+int(second_num))

    elif math=='subtraction':
        box.insert(0,final-int(second_num))


    elif math=='multiplication':
        box.insert(0,final*int(second_num))

    elif math=='division':
        box.insert(0,final/int(second_num))



def add():
    global final
    global math
    math='addition'
    n=box.get()
    box.delete(0,last=END)
    final=int(n)

def sub():
    global final
    global math
    math='subtraction'
    n=box.get()
    box.delete(0,last=END)
    final=int(n)

def mul():
    global final
    global math
    math='multiplication'
    n=box.get()
    box.delete(0,last=END)
    final=int(n)

def div():
    global final
    global math
    math='division'
    n=box.get()
    box.delete(0,last=END)
    final=int(n)


    

def clear():
    box.delete(0,last=END)


myFont = font.Font(family='Helvetica', size=10, weight='bold')


b0=Button(root,text='0',padx=30,pady=30,command=lambda : click(0))
b1=Button(root,text='1',padx=30,pady=30,command=lambda : click(1))
b2=Button(root,text='2',padx=30,pady=30,command=lambda : click(2))
b3=Button(root,text='3',padx=30,pady=30,command=lambda : click(3))
b4=Button(root,text='4',padx=30,pady=30,command=lambda : click(4))
b5=Button(root,text='5',padx=30,pady=30,command=lambda : click(5))
b6=Button(root,text='6',padx=30,pady=30,command=lambda : click(6))
b7=Button(root,text='7',padx=30,pady=30,command=lambda : click(7))
b8=Button(root,text='8',padx=30,pady=30,command=lambda : click(8))
b9=Button(root,text='9',padx=30,pady=30,command=lambda : click(9))
bequal=Button(root,text='=',padx=105,pady=30,command=equal)
bplus=Button(root,text='+',padx=30,pady=30,command= add)
bminus=Button(root,text='-',padx=30,pady=30,command=sub)
bmul=Button(root,text='*',padx=30,pady=30,command=mul)
bdiv=Button(root,text='/',padx=30,pady=30,command=lambda : click('/'))
bclear=Button(root,text='clear',padx=57,pady=30,command=clear)
b0['font']=myFont
b1['font']=myFont
b2['font']=myFont
b3['font']=myFont
b4['font']=myFont
b5['font']=myFont
b6['font']=myFont
b7['font']=myFont
b8['font']=myFont
b9['font']=myFont
bequal['font']=myFont
bminus['font']=myFont
bmul['font']=myFont
bdiv['font']=myFont
bplus['font']=myFont
bclear['font']=myFont

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
b4.grid(row=4,column=0)
b5.grid(row=4,column=1)
b6.grid(row=4,column=2)
b1.grid(row=5,column=0)
b2.grid(row=5,column=1)
b3.grid(row=5,column=2)
b0.grid(row=6,column=0)
bclear.grid(row=6,column=1,columnspan=2)
bequal.grid(row=7,column=0,columnspan=3)
bplus.grid(row=3,column=3)
bmul.grid(row=5,column=3)
bdiv.grid(row=6,column=3)
bminus.grid(row=4,column=3)



root.mainloop()
