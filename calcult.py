from tkinter import *

window = Tk() 
window.title("Калукулятор")
window.geometry("300x310") 
window['background'] = '#696969'


entry = Entry(window, width= 15, font= ("", 20), bg='gray', fg="white")  
entry.place(x=50, y=5)


def input_into_entry(sumbol):
    entry.insert(END, sumbol) 


def clear():
    entry.delete(0, END) 


def caunt_result():
    result = 0 
    text = entry.get()

    if '+' in text:
        spleted_text = text.split('+')  
        first = float(spleted_text[0])
        second = float(spleted_text[1]) 
        result = first+second
    if '-' in text:
        spleted_text = text.split('-')  
        first = float(spleted_text[0])
        second = float(spleted_text[1]) 
        result = first-second 
    if '/' in text:
        spleted_text = text.split('/')  
        first = float(spleted_text[0])
        second = float(spleted_text[1]) 
        result = first/second  
        
        
    if '*' in text:
        spleted_text = text.split('*')  
        first = float(spleted_text[0])
        second = float(spleted_text[1]) 
        result = first*second 
    
    clear()
    entry.insert(0, result)
   
    
def by():
    clear()
    entry.insert(1, 'By NikitaNim3453') 










btn1 = Button(window, bg="gray", fg= "white", text="1", command= lambda : input_into_entry('1'), font=("", 20))  
btn1.place(x="50", y="100", width="50", height="50")

btn2 = Button(window, bg="gray", fg= "white", text="2", command= lambda : input_into_entry('2'), font=("", 20)) 
btn2.place(x="100", y="100", width="50", height="50")

btn3 = Button(window, bg="gray", fg= "white", text="3", command= lambda : input_into_entry('3'), font=("", 20)) 
btn3.place(x="150", y="100", width="50", height="50")

btn4 = Button(window, bg="gray", fg= "white", text="4", command= lambda : input_into_entry('4'), font=("", 20)) 
btn4.place(x="50", y="150", width="50", height="50")

btn5 = Button(window, bg="gray", fg= "white", text="5", command= lambda : input_into_entry('5'), font=("", 20)) 
btn5.place(x="100", y="150", width="50", height="50")

btn6 = Button(window, bg="gray", fg= "white", text="6", command= lambda : input_into_entry('6'), font=("", 20)) 
btn6.place(x="150", y="150", width="50", height="50")

btn7 = Button(window, bg="gray", fg= "white", text="7", command= lambda : input_into_entry('7'), font=("", 20)) 
btn7.place(x="50", y="200", width="50", height="50")

btn8 = Button(window, bg="gray", fg= "white", text="8", command= lambda : input_into_entry('8'), font=("", 20)) 
btn8.place(x="100", y="200", width="50", height="50")

btn9 = Button(window, bg="gray", fg= "white", text="9", command= lambda : input_into_entry('9'), font=("", 20)) 
btn9.place(x="150", y="200", width="50", height="50")

btn0 = Button(window, bg="gray", fg= "white", text="0", command= lambda : input_into_entry('0'), font=("", 20)) 
btn0.place(x="100", y="250", width="50", height="50")

btn_plus = Button(window, bg="gray", fg= "white", text="+", command= lambda : input_into_entry('+'), font=("", 20)) 
btn_plus.place(x="200", y="100", width="50", height="50")

btn_minus = Button(window, bg="gray", fg= "white", text="-", command= lambda : input_into_entry('-'), font=("", 20)) 
btn_minus.place(x="200", y="150", width="50", height="50")

btn_divede = Button(window, bg="gray", fg= "white", text="/", command= lambda : input_into_entry('/'), font=("", 20)) 
btn_divede.place(x="200", y="50", width="50", height="50")

btn_multiply = Button(window, bg="gray", fg= "white", text="X", command= lambda : input_into_entry('*'), font=("", 20)) 
btn_multiply.place(x="200", y="200", width="50", height="50")

btn_result = Button(window, bg="gray", fg= "white", text="=", command= caunt_result, font=("", 20)) 
btn_result.place(x="200", y="250", width="50", height="50") 

btn_clear = Button(window, bg="gray", fg= "white", text="CE", command= clear, font=("", 20)) 
btn_clear.place(x="150", y="50", width="50", height="50")

btn_clear_1 = Button(window, bg="gray", fg= "white", text="<--", command= clear, font=("", 20))   
btn_clear_1.place(x='100', y='50', width='50', height='50')    

btn_dot = Button(window, bg="gray", fg= "white", text=".", command= lambda : input_into_entry('.'), font=("", 40)) 
btn_dot.place(x="150", y="250", width="50", height="50")

btn_by = Button(window, bg="gray", fg= "white", text="by", command= by, font=("", 20)) 
btn_by.place(x='50', y='50', width='50', height='50')


window.mainloop()
