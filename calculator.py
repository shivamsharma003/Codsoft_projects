from tkinter import *

number_1=number_2=operator=None

def digits(digit):
    current= result_label['text']
    new=current+str(digit)
    result_label.config(text=new)
    
def clear():
    result_label.config(text='')

def get_operator(op):
    global number_1,operator

    number_1=int(result_label['text'])
    operator=op
    result_label.config(text='')

def result():
    global number_1,number_2,operator

    number_2=int(result_label['text'])

    if operator=='+':
        result_label.config(text=str(number_1+number_2))
    elif operator=='-':
        result_label.config(text=str(number_1-number_2))
    elif operator=='*':
        result_label.config(text=str(number_1*number_2))
    else:
        result_label.config(text=str(round(number_1/number_2,2)))
        

    

root=Tk()
root.title('Calculator')
root.geometry('260x370')
root.resizable(0,0)
root.configure(background='black')

result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=10,pady=(50,25),sticky='w')
result_label.config(font=('Arial',30,'bold'))

Button_7=Button(root,text='7',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(7))
Button_7.grid(row=1,column=0)
Button_7.config(font=('Arial',14))


Button_8=Button(root,text='8',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(8))
Button_8.grid(row=1,column=1)
Button_8.config(font=('Arial',14))


Button_9=Button(root,text='9',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(9))
Button_9.grid(row=1,column=2)
Button_9.config(font=('Arial',14))


Button_add=Button(root,text='+',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:get_operator('+'))
Button_add.grid(row=1,column=3)
Button_add.config(font=('Arial',14))



Button_4=Button(root,text='4',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(4))
Button_4.grid(row=2,column=0)
Button_4.config(font=('Arial',14))


Button_5=Button(root,text='5',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(5))
Button_5.grid(row=2,column=1)
Button_5.config(font=('Arial',14))


Button_6=Button(root,text='6',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(6))
Button_6.grid(row=2,column=2)
Button_6.config(font=('Arial',14))


Button_sub=Button(root,text='-',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:get_operator('-'))
Button_sub.grid(row=2,column=3)
Button_sub.config(font=('Arial',14))


Button_1=Button(root,text='1',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(1))
Button_1.grid(row=3,column=0)
Button_1.config(font=('Arial',14))


Button_2=Button(root,text='2',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(2))
Button_2.grid(row=3,column=1)
Button_2.config(font=('Arial',14))


Button_3=Button(root,text='3',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:digits(3))
Button_3.grid(row=3,column=2)
Button_3.config(font=('Arial',14))


Button_mul=Button(root,text='*',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:get_operator('*'))
Button_mul.grid(row=3,column=3)
Button_mul.config(font=('Arial',14))


Button_clr=Button(root,text='C',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:clear())
Button_clr.grid(row=4,column=0)
Button_clr.config(font=('Arial',14))


Button_0=Button(root,text='0',bg='#ed7c0b',fg='white',width=5,height=2)
Button_0.grid(row=4,column=1)
Button_0.config(font=('Arial',14))


Button_equals=Button(root,text='=',bg='#ed7c0b',fg='white',width=5,height=2,command=result)
Button_equals.grid(row=4,column=2)
Button_equals .config(font=('Arial',14))


Button_div=Button(root,text='/',bg='#ed7c0b',fg='white',width=5,height=2,command=lambda:get_operator('/'))
Button_div.grid(row=4,column=3)
Button_div.config(font=('Arial',14))


root.mainloop()
