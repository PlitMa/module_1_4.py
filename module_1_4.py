from logging import currentframe
#верхний и нижний регистор#
name = input("Ведите своё имя: ")
print(name.upper())

name = input("Введите своё имя: ")
print(name.lower())

#замена слова#
print("Привет, спасибо что решил присоединиться к нам, заполните, пожалуйста, анкету: ".replace("Привет","Добрый час"))
print("Привет, спасибо что решил присоединиться к нам, заполните, пожалуйста, анкету: ".replace(" ",""))

#Программа приветствия#
name = input("Ваше ФИО: ")
C = input("Ваш город прожиывния: ")
current_year = 2024
date_of_birth = input("Ваш год рождения: ")
A = current_year - int(date_of_birth)
print("Добрый час, ", name)
print("Ваш город:",C)
print("Вам: ",A)
print("Рады привтствовать вас на нашем форуме")