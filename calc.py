from tkinter import *



window = Tk()
window.geometry("400x500")
window.title("Calculator")





display = Entry(window,width=55,borderwidth=5)
display.grid(row=0, column=0, columnspan=5,)

#defntion when button clicked
def click(number):
	current = display.get()
	display.delete(0, END)
	display.insert(0,str(current) + str(number))
	
def clear():
	display.delete(0, END)
	

def add():
	first_number = display.get()
	global numbersum
	number1 = int(first_number)
	display.delete(0, END)

def equalto():
	second_number = display.get()
	display.delete(0, END)
	display.insert(0, numbersum + int(second_number))



#number_9

btn_pic9 = PhotoImage(file = 'img/9.png')

img_label9 = Label(image=btn_pic9)

btn9 = Button(window, image=btn_pic9, borderwidth=0,command=lambda: click(9))
btn9.grid(row=2,column=0)

#number_8

btn_pic8 = PhotoImage(file = 'img/8.png')

img_label8 = Label(image=btn_pic8)

btn8 = Button(window, image=btn_pic8, borderwidth=0,command=lambda: click(8))
btn8.grid(row=2,column=1)

#number_7

btn_pic7 = PhotoImage(file = 'img/7.png')

img_label7 = Label(image=btn_pic7)

btn7 = Button(window, image=btn_pic7, borderwidth=0,command=lambda: click(7))
btn7.grid(row=2,column=2)

#number_0

btn_pic0 = PhotoImage(file = 'img/0.png')

img_label0 = Label(image=btn_pic0)

btn0 = Button(window, image=btn_pic0, borderwidth=0,command=lambda: click(0))
btn0.grid(row=2,column=3)


#number_4

btn_pic4 = PhotoImage(file = 'img/4.png')

img_label4 = Label(image=btn_pic4)

btn4 = Button(window, image=btn_pic4, borderwidth=0,command=lambda: click(4))
btn4.grid(row=3,column=0)


#number_5

btn_pic5 = PhotoImage(file = 'img/5.png')

img_label5 = Label(image=btn_pic5)

btn5 = Button(window, image=btn_pic5, borderwidth=0,command=lambda: click(5))
btn5.grid(row = 3,column = 1)

#number_6

btn_pic6 = PhotoImage(file = 'img/6.png')

img_label6 = Label(image=btn_pic6)

btn6 = Button(window, image=btn_pic6, borderwidth=0,command=lambda: click(6))
btn6.grid(row=3, column = 2)

#sub

btn_pic_sub = PhotoImage(file = 'img/sub.png')

img_label_sub = Label(image=btn_pic_sub)

btn_sub = Button(window, image=btn_pic_sub, borderwidth=0,command=lambda:substract)
btn_sub.grid(row=3,column= 3)



#number_1

btn_pic1 = PhotoImage(file = 'img/1.png')

img_label1 = Label(image=btn_pic1)

btn1 = Button(window, image=btn_pic1, borderwidth=0,command=lambda: click(1))
btn1.grid(row=4,column=0)

#number_2

btn_pic2 = PhotoImage(file = 'img/2.png')

img_label2 = Label(image=btn_pic2)

btn2 = Button(window, image=btn_pic2, borderwidth=0,command=lambda: click(2))
btn2.grid(row=4,column=1)

#number_3

btn_pic3 = PhotoImage(file = 'img/3.png')

img_label3 = Label(image=btn_pic3)

btn3 = Button(window, image=btn_pic3, borderwidth=0,command=lambda: click(3))
btn3.grid(row = 4, column = 2)

#add

btn_pic_add = PhotoImage(file = 'img/add.png')

img_label_add = Label(image=btn_pic_add)

btn_add = Button(window, image=btn_pic_add, borderwidth=0,command=add)
btn_add.grid(row = 4, column = 3)


#clear

btn_pic_clear = PhotoImage(file = 'img/clear.png')

img_label_clear = Label(image=btn_pic_clear)

btn_clear = Button(window, image=btn_pic_clear, borderwidth=0,command=clear)
btn_clear.grid(row=5,column=0)

#division

btn_pic_div = PhotoImage(file = 'img/div.png')

img_label_div = Label(image=btn_pic_div)

btn_div = Button(window, image=btn_pic_div, borderwidth=0,command=divide)
btn_div.grid(row = 5, column = 1)


#mul

btn_pic_mul = PhotoImage(file = 'img/mul.png')

img_label_mul = Label(image=btn_pic_mul)

btn_mul = Button(window, image=btn_pic_mul, borderwidth=0,command=lambda:multiply)
btn_mul.grid(row=5,column=2)

#equal to 

btn_pic_equals = PhotoImage(file = 'img/equals.png')

img_label_equals = Label(image=btn_pic_equals)

btn_equals = Button(window, image=btn_pic_equals, borderwidth=0,command=equalto)
btn_equals.grid(row = 5, column = 3)



##

window.mainloop()