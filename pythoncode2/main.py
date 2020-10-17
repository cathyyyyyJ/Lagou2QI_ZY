class Animal():
    def __init__(self,name,color,age,sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def sound(self):
        print("会叫")

    def run(self):
        print("会跑")


class cat(Animal):
    def __init__(self,name,color,age,sex,hair='短毛'):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.hair = hair

    def catch(self):
        print("会捉老鼠")

    def sound(self):
        print("喵喵叫")

class dog(Animal):
    def __init__(self,name,color,age,sex,hair='长毛'):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.hair = hair

    def watch(self):
        print("会看家")

    def sound(self):
        print("汪汪叫")
