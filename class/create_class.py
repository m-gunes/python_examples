class Developer():
    def __init__(self, name, last_name, salary, skill):
        self.name = name
        self.last_name = last_name
        self.salary = salary
        self.skill = skill

    def show_infos(self):
        print(
            '''
            DEVELOPER INFORMATIONS:
    
            name: {}
            last name: {}
            salary: {}
            skills: {}
    
            '''.format(self.name, self.last_name, self.salary, self.skill)
        )

    def salary_increase(self, percent):
        self.salary = self.salary + (self.salary * percent // 100)

    def add_skill(self, skill):
        self.skill.append(skill)

mustafa = Developer('mustafa', 'gunes', 10000, ['Javascript', 'Python', 'SQL', 'HTML', 'CSS'])

mustafa.show_infos()

mustafa.add_skill('C')
mustafa.show_infos()

mustafa.salary_increase(20)
mustafa.show_infos()

