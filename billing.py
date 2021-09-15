from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.title('biling slip')
root.title('1280x720')
bg_color='#4D0039'
#=================================Variable========================
c_name=StringVar()
c_phone=StringVar()
bill=IntVar()
item=StringVar()
Rate=IntVar()
Quantity=IntVar()
#bill_no=StringVar()
#x=random.randint(1000,9999)
#bill_no.set(str(x))

global l
l=[]

#=================================Function========================
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t Welcome Ravi Retails")
    textarea.insert(END,f"\n\n Bill Number : \t\t{bill.get()}")
    textarea.insert(END,f'\n Customer Name: \t\t{c_name.get()}')
    textarea.insert(END,f'\n Customer Number: \t\t{c_phone.get()}')
    textarea.insert(END,f'\n======================================\n')
    textarea.insert(END,'\n Product\t\t QTY\t\tPrice')
    textarea.insert(END,f'\n======================================\n')
    textarea.configure(font='arial 15 bold')

def additm():
    n=Rate.get()
    m=Quantity.get()*n
    l.append(m)
    if item.get()=='':
        messagebox.showerror('Error','Please Enter the item')
    else:
        textarea.insert((10.0+float(len(l)-1)), f'{item.get()}\t\t{Quantity.get()}\t\t{m}\n')

def gbill():
    if c_name.get()=='' or c_phone.get()=='' or bill.get()=='':
        messagebox.showerror('Error','Customer Details are must')
    else:
        tex=textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END,tex)
        textarea.insert(END,f"\n=====================================")
        textarea.insert(END,f"\nTotal pay bill Amount:\t\t\t{sum(l)}")
        textarea.insert(END,f"\n\n===================================")
        savebill()

def savebill():
    op=messagebox.askyesno('Save bill','Do you want to save bill')
    if op>0:
        bill_details=textarea.get(1.0,END)
        f1=open("bills/"+str(bill.get())+".txt",'w')
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo('Saved',f'Bill no: {bill.get()} Saved successfully')
    else:
        return

def clear():
    c_name.set('')
    c_phone.set('')
    bill.set('')
    item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()

def exit():
    op=messagebox.askyesno('Exit','Do you realy want to exit')
    if op>0:
     root.destroy()
    

#================================top section==================
title=Label(root,text='Billing Software',bg=bg_color,fg='white',font=('times new romman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

#+==================customer details==============================

F1=LabelFrame(root, text='Customer Details', font=('time new rommon',18,'bold'),relief=GROOVE,bd=10,bg=bg_color,fg='gold')
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1, text='Customer Name', font=('time new rommon',18,'bold'),bg=bg_color,fg='white')
cname_lbl.grid(row=0,column=0,padx=10,pady=5)
cname_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1, text='Phone No', font=('time new rommon',18,'bold'),bg=bg_color,fg='white')
cphone_lbl.grid(row=0,column=2,padx=10,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_phone)
cphone_txt.grid(row=0,column=3,padx=10,pady=5)

bill_lbl=Label(F1, text='Customer Name', font=('time new rommon',18,'bold'),bg=bg_color,fg='white')
bill_lbl.grid(row=1,column=0,padx=10,pady=5)
bill_txt=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=bill)
bill_txt.grid(row=1,column=1,padx=10,pady=5)

F2=LabelFrame(root, text='Product details', font=('time new rommon',18,'bold'),relief=GROOVE,bd=10,bg=bg_color,fg='gold')
F2.place(x=20,y=220,width=630,height=500)

itm=Label(F2,text='Product Name', font=('times new rommon',18,'bold'),bg=bg_color,fg='lightgreen')
itm.grid(row=0,column=0,padx=30,pady=20)
itm_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=item)
itm_txt.grid(row=0,column=1,padx=30,pady=20)


rate=Label(F2,text='Product Rate', font=('times new rommon',18,'bold'),bg=bg_color,fg='lightgreen')
rate.grid(row=1,column=0,padx=30,pady=20)
rate_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Rate)
rate_txt.grid(row=1,column=1,padx=30,pady=20)

quantity=Label(F2,text='Product Quantity', font=('times new rommon',18,'bold'),bg=bg_color,fg='lightgreen')
quantity.grid(row=2,column=0,padx=30,pady=20)
quantity_txt=Entry(F2,width=20,font='arial 15 bold',textvariable=Quantity)
quantity_txt.grid(row=2,column=1,padx=30,pady=20)

#===============================btn===========

btn1=Button(F2,text='Add item',font='arial 15 bold',padx=5,pady=10,bg='lime',width=10,command=additm)
btn1.grid(row=3,column=0,padx=10,pady=30)

btn2=Button(F2,text='Genrate Bill',font='arial 15 bold',padx=5,pady=10,bg='lime',width=10,command=gbill)
btn2.grid(row=3,column=1,padx=10,pady=30)

btn3=Button(F2,text='clear',font='arial 15 bold',padx=5,pady=10,bg='lime',width=10,command=clear)
btn3.grid(row=4,column=0,padx=10,pady=30)

btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,bg='lime',width=10,command=exit)
btn4.grid(row=4,column=1,padx=10,pady=30)

#================================bill Area==========================

F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=220,width=500,height=500)

bill_title=Label(F3,text='Bill Area',font='arial 15 bold',relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()

root.mainloop()
