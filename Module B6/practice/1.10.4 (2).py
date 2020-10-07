class Man:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Guest(Man):
    def setRole(self, role):
        self.role = role

    def status(self):
        try:
            return f'{self.name}, г. {self.city}, статус "{self.role}"'
        except:
            return f'Не задан статус у гостя {self.name}'

guest_1 = Guest('Иван Петров', 'Москва')
guest_1.setRole('Наставник')

guest_2 = Guest('Николай Иванов', 'Саратов')

print(guest_1.status())
print(guest_2.status())
