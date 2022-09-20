from tkinter import *
import random 

#Список числ которые показыватся в виджете 
numbers_list = [1,2,3,4,5,6,7,8,9,10]

#Для того что бы кнопка писала числа
def clicked():  
    numbers.configure( text=random.choice(numbers_list))  
#Создание окна и настройка параметров
window = Tk()  
window.resizable( width=False, height=False )
window.title("random numbers")  
window.geometry('400x250') 

#Делаем виджет в котором будет появлятся числа
numbers = Label(window, text="", font=("Arial Bold", 50))  
numbers.place(x=175, y=50)

#Создание кнопки
btn = Button(window, text=" Клик! ", command=clicked,bg="grey",font=("Arial Bold", 10))  
btn.place(x=170, y=150)

#Цикл 
window.mainloop()
