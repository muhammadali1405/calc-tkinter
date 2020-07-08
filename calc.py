from tkinter import *


win=Tk()
win.geometry("400x500")
win.title("Calculator")



 
btn1 = Button(win)
btn2 = Button(win)
btn3 = Button(win)
btn_add = Button(win)
btn4 = Button(win)
btn5 = Button(win)
btn6 = Button(win)
btn_sub = Button(win)
btn7 = Button(win)
btn8 = Button(win)
btn9 = Button(win)
btn_mul = Button(win)
btn0 = Button(win)
btn_div = Button(win)
btn_equals = Button(win)
btn_clear = Button(win)




btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row = 1, column = 2)
btn_add.grid(row = 1, column = 3)
btn4.grid(row = 2, column = 0)
btn5.grid(row = 2,column = 1)
btn6.grid(row=2, column = 2)
btn_sub.grid(row=2,column= 3)
btn7.grid(row=3, column = 0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
btn_mul.grid(row=3,column=3)
btn0.grid(row=4,column=0)
btn_div.grid(row=4,column= 3)
btn_equals.grid(row=4,column = 1)
btn_clear.grid(row=4,column=2)

win.mainloop()