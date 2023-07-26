
# Создать класс "Проект":
# - название,
# - дата начала,
# - дата dead-line,
# - список имён программистов, которые над ним работают.
# Дата (DateTime) начала должна браться автоматически при создании объекта проекта.
# Реализовать метод str(self)
# Список программистов на проекте тоже нужно обработать, чтобы он выводился красиво в str.
#
# Создать методы класса:
# 1. Изменение даты (DateTime) окончания проекта
# 2. Добавление программиста на проект
# 3. Метод увольнения программиста с проекта.


import datetime

class Project:

    def __init__(self, name_project, date_begining, date_dedline, list_people):
        self.nameProject = name_project
        self.dateBegining = date_begining
        self.dateDedline = date_dedline
        self.listPeople = list_people


    def __str__(self):
        return f'Название проекта: {self.nameProject}\n' \
               f'Дата начала: {self.dateBegining}\n' \
               f'Дата ded-line через: {self.dateDedline}\n' \
               f'Список программистов: {self.listPeople}\n'

    def change_ded_line(self, new_ded_line):
        self.dateDedline = new_ded_line

    # def add_people(self, new_people):
    #     self.listPeople.split(' ').insert(new_people)

    # def remove_people(self, del_people):
    #     self.listPeople.split(' ').remove(del_people)

project1 = Project('Кофейня', datetime.datetime.now(), '5 дней', '\nИванов\nПетров\nСидоров')

print(project1)

project1.change_ded_line('10 дней')

print(project1)

# project1.add_people('Курочкин')
# project1.remove_people('Петров')
# print(project1)









# Это пример с урока!

# class User:
#
#     def __init__(self, first_name, sur_name, last_name, age, phone, email):
#         self.firstName = first_name
#         self.surName = sur_name
#         self.lastName = last_name
#         self.age = age
#         self.phone = phone
#         self.email = email
#
#     def change_phone(self, new_phone):
#         self.phone = new_phone
#
#     def __str__(self):
#         return f'Имя: {self.firstName}\n' \
#                f'Фамилия: {self.surName}\n' \
#                f'Отчество: {self.lastName}\n' \
#                f'Возраст: {self.age}\n' \
#                f'Телефон: {self.phone}\n' \
#                f'Email: {self.email}\n'
#
# user1 = User('Иван', 'Иванов', 'Иванович', 30, '+7-99-454-88-77', 'ivan@mail.com')
#
# print(user1)
#
# user1.change_phone('+7-29-454-88-11')
#
# print(user1)
#
# user2 = User('Петр', 'Петров', 'Петрович', 35, '+7-29-123-88-55', 'potr@mail.com')
#
# # print(user1, end='\n\n')
# print(user2)
