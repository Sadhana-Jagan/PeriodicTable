#main code
import pickle as p
import tkinter as tk

from functools import partial
win=tk.Tk()
h1=3
w1=3
canvas=tk.Canvas(win,height=700,width=990)
canvas.pack()
q=[0,1,2,3,4,5,6]
q1=[0,1,2,3]
def g1(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp1.dat','rb')
    a=p.load(f)
    for w in a:#w is all the data of one element, i is different elements
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1


def g2(g):
    wing2=tk.Toplevel(win)
    s=0
    f=open('grp2.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing2,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1
def g18(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp18.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
def gla(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grpla.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
def gac(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grpac.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
            
def g13(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp13.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
    

def g14(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp14.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
            
def g15(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp15.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 

def g16(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp16.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
            
def g17(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp17.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 

def g3(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp3.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
def g4(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp4.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 

def g5(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp5.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 

def g6(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp6.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 

def g7(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp7.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
            
def g8(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp8.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
            
def g9(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp9.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
            
def g10(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp10.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
            
def g11(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp11.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
        
def g12(g):
    wing1=tk.Toplevel(win)
    s=0
    f=open('grp12.dat','rb')
    a=p.load(f)
    for w in a:
        if s==g:
            for i in q:
                lbl1=tk.Label(wing1,text=str(w[i]))
                lbl1.pack(anchor='w')
            break
        else:
            s+=1 
            

lbl=tk.Label(win,text='The Periodic Table',font=('Arial',25),fg='red')
lbl.place(anchor='n',relx=0.5)
grp1=['H','Li','Na','K','Rb','Cs','Fr']
grp2=['Be','Mg','Ca','Sr','Ba','Ra']
x1=110
grp3=['Sc','Y','La','Ac']
grp4=['Ti','Zr','Hf','Rf']
grp5=['V','Nb','Pa','Db']
grp6=['Cr','Mo','W','Sg']
grp7=['Mn','Tc','Re','Bh']
grp8=['Fe','Ru','Os','Hs']
grp9=['Co','Rh','Ir','Mt']
grp10=['Ni','Pd','Pt','Ds']
grp11=['Cu','Ag','Au','Rg']
grp12=['Zn','Cd','Hg','Cn']
grp13=['B','Al','Ga','In','Tl','Nh']
grp14=['C','Si','Ge','Sn','Pb','Fl']
grp15=['N','P','As','Sb','Bi','Mc']
grp16=['O','S','Se','Te','Po','Lv']
grp17=['F','Cl','Br','I','At','Ts']
grp18=['He','Ne','Ar','Kr','Xe','Rn','Og']
lan=['Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu']
act=['Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr']
bg1=['#BBF677','#EDF243','#F5B041','#F1948A','#55D8CD']
grpp=[grp13,grp14,grp15,grp16,grp17]
grp=[grp3,grp4,grp5,grp6,grp7,grp8,grp9,grp10,grp11,grp12]
z=0
g=3
for i in range(1,8):
    b=tk.Button(win,text=grp1[i-1],height=h1,width=w1,bg='#DA5C8D',command=partial(g1,i-1))
    b.place(x=0,y=55*i)
    
for i in range(2,8):
    b=tk.Button(win,text=grp2[i-2],height=h1,width=w1,bg='#EA93B4',command=partial(g2,i-2))
    b.place(x=55,y=55*i)
for i in grp:
    for j in range(4,8):
        b=tk.Button(win,text=i[j-4],height=h1,width=w1,bg='#55C4E7',command=partial(eval('g'+str(g)),j-4))
        b.place(x=x1,y=55*j)
    x1+=55
    g+=1
x2=660
a=0
s=13
k=13
for i in grpp:
    for j in range(2,8):
        b=tk.Button(win,text=i[j-2],height=h1,width=w1,bg=bg1[a],command=partial(eval('g'+str(k)),j-2))
        b.place(x=x2,y=55*j)
    x2+=55
    a+=1
    k+=1
for i in range(1,8):
    b=tk.Button(win,text=grp18[i-1],height=h1,width=w1,bg='#BB8FCE',command=partial(g18,i-1))
    b.place(x=935,y=55*i)
x3=110    
for i in range(2,16):
    b=tk.Button(win,text=lan[i-2],height=h1,width=w1,bg='#A3E4D7',command=partial(gla,i-2))
    b.place(x=x3,y=495)
    x3+=55
x4=110
for i in range(2,16):
    b=tk.Button(win,text=act[i-2],height=h1,width=w1,bg='#AED6F1',command=partial(gac,i-2))
    b.place(x=x4,y=550)
    x4+=55
win.mainloop()
