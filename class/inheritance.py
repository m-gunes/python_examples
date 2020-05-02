#  Yeni Employee veri tipi oluşturuyoruz.
class Employee:
    def __init__(self, name, last_name, title, salary):
        self.name = name
        self.last_name = last_name
        self.title = title
        self.salary = salary

    def show_infos(self):
        print('Employee informations:\n name: {}\n last name: {} \n title: {} \n salary: {}'
              .format(self.name, self.last_name, self.title, self.salary))

    def change_title(self, new_title):
        self.title = new_title


class Manager(Employee):
    pass  # simdilik gectik farkli ozellikler eklemeyi


#  Manager veri tipinden obje olusturmak
manager1 = Manager('mustafa', 'gunes', 'Front-end Developer', 15000)

manager1.show_infos()


class Manager(Employee):  # Employee class'indan inheritance(kalitim, miras) aliyoruz

    def __init__(self, name, last_name, title, salary, team=0):  # Sorumlu olduğu kişi sayısı ekliyoruz
        # 4 tane özelliği super sayesinde Employee class'inin init fonksiyonuyla hallediyoruz.
        super().__init__(name, last_name, title, salary)
        self.team = team  # Yeni eklenen özellik

    def show_infos(self):  # overriding
        print('Employee informations:\n name: {}\n last name: {} \n title: {} \n salary: {} \n team count: {}'
              .format(self.name, self.last_name, self.title, self.salary, self.team))

    def salary_increase(self, amount):
        self.salary += amount


manager3 = Manager('sibel', 'asar', 'gmy', 125000000, 350)
manager3.show_infos()
