from tkinter import *
import tkinter.messagebox as msg
from datetime import datetime

date=datetime.now().date()
with open(r'C:\\Users\\sk454\\OneDrive\\Desktop\\coding\\tkinter\\my projects\\days_count.txt','r') as f:
    lines=f.readlines()
success_days=len(lines)
def check():
    global is_complete,unchecked_list
    unchecked_list=[]
    is_complete=True
    for values in value_list:
        if values.get()!=1:
            temp_unchecked_valueIndex=value_list.index(values)
            unchecked_list.append(lst[temp_unchecked_valueIndex])
            is_complete=False
        else:
            pass
    if is_complete:
        msg.showinfo('praise','you did a great job, reward yourself')
        for items0 in value_list:
            items0.set(0)
        with open(r'C:\\Users\\sk454\\OneDrive\\Desktop\\coding\\tkinter\\my projects\\days_count.txt','a') as f0:
            f0.write(f'\n{date}  done - 1')
    elif len(unchecked_list)<=4:
        msg.showinfo('work for success',f'try completing {unchecked_list}')
    else:
        msg.showinfo('disappointment','exam is ahead do your work or you will fail')

def show_success():
    msg.showinfo('sucess rate',f'congratulations! you have completed {success_days} days successfully')

root=Tk()
root.title('ROUTINE')
root.geometry('444x333')

menu0=Menu(root)
m1=Menu(menu0,tearoff=0)
m1.add_command(label='success days',command=show_success)
menu0.add_cascade(label='options',menu=m1)
root.config(menu=menu0)

check_value0=IntVar()
check_value1=IntVar()
check_value2=IntVar()
check_value3=IntVar()
check_value4=IntVar()
value_list=[check_value0,check_value1,check_value2,check_value3,check_value4]
lst=['physics 1 hour','maths 1 hour','biology tuition work','learning code on youtube','code creating small projects']
for i,items in enumerate(lst):
    check_buttonValue=Checkbutton(root,text=items,variable=value_list[i]).pack(anchor='w')
Button(root,text='submit',command=check).pack(anchor='w')

root.mainloop()
