# основные принципы ООП(Абстарция).Наследование.Инкапсуляция.Полиморфизм.

class Junior:
    def __init__(self, language, soft_skills, laptop, salary):
        self.language = language
        self.soft = soft_skills
        self.laptop = laptop
        self.salary = salary

    def say_which_language(self):
        return f"I'm using {self.language}"

    def __str__(self):
        return f"Language: {self.language}\n" \
               f"Soft_skills: {self.soft}\n" \
               f"Laptop: {self.laptop}\n" \
               f"Salary: {self.salary}\n"


junior1 = Junior(language="Python", soft_skills="good enought",
                 laptop="gaming laptop", salary="300$")
#print(junior1)

class Middle(Junior):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable):
        super(Middle, self).__init__(language, soft_skills, laptop, salary)
        self.fast_resolving = fast_resolving
        self.reliable = reliable

    def __str__(self):
        return super(Middle, self).__str__() + f"Resolving: {self.fast_resolving}\n"\
                                               f"Reliable: {self.reliable}"

middle1 = Middle(language="Python", soft_skills="good enought",
                 laptop="gaming laptop", salary="3000$", fast_resolving="often", reliable="True")
#print(middle1.say_which_language())
#print(middle1)

class Senior(Middle):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable, architecture, leading_skills):
        super(Senior, self).__init__(language, soft_skills, laptop, salary, fast_resolving, reliable)
        self.architecture = architecture
        self.leading_skills = leading_skills
    def __str__(self):
        return super(Senior, self).__str__() + f"\nArchitecture: {self.architecture}\n"\
                                               f"Leading_skill: {self.leading_skills}"
senior1 = Senior(language="Python", soft_skills="good enought",
                 laptop="gaming laptop", salary="6000$", fast_resolving="often", reliable=True,
                 architecture=True, leading_skills=True)

print(senior1.say_which_language())
print(senior1)