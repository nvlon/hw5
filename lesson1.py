class Human:
    #атрибуты уровня класса
    head=1
    body=1
    #функция ,конструктор
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #метод
    def run (self):
       print(f'{self.name} is run ')
#hum -обьект
hum=Human('Алдияр', 18)
hum.run()






# Наследование,полиморфизм

# инкапсуляция


# супер класс
class Robot:
    brain=True
    def __init__(self,name,model,color,destination):
        self.name=name
        self.model=model
        self.color=color
        self.dest=destination


    def __str__(self):
        return f'name is {self.name}\n' \
               f'color is {self.color}\n' \
               f'model is {self.model}'
    def desti(self):
        print(self.dest)

robot=Robot('Влад','А4','blue','снимать видео')
print(robot)
print(robot.desti())

# дочерний класс
class Robot2(Robot):
    brain = False
    def __init__(self,name, model, color, destination,fly):
        super().__init__(name, model, color, destination)
        Robot.__init__(self,name, model, color, destination)
        self.fly=fly
    def desti(self):
        self.fly=False
        print(self.fly)

robot2=Robot2('termonator','T1001','pink','отбирает одежду',True)
print(robot2.fly)
robot2.desti()
print(robot2.fly)

robot.desti()
robot2.desti()
print(robot2.brain,robot.brain)

class Robot3(Robot2):
    def desti(self):
        print(self,' теперь летает')


MegaTron=Robot3('TRANSformer','Desipticon','RED','WARS',False)
MegaTron.desti()


class Human:
    # атрибуты уровня класса
    head = 1
    body = 1
    hands = 2

    # метод :конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'head is {self.head}'


hum=Human('Алдияр',18)
Robot3.desti(hum.age)






#
# # инкапсуляция
# # git clone
#
# class Emirlan:
#     head=1
#     hands=2
#     foots=2
#     def __init__(self,name='Emirlan',age=18):
#         self.__name=name
#         self._age=age
#     def __str__(self):
#         return f'{self.__name} ' \
#                f'{self._age}'
#
#     def run(self):
#         self.__run()
#         self.__g()
#         print(self._age - 1)
#         print(self.__name)
#
#
#     def __run(self):
#         print(self.__name, 'run')
#
#     def __g(self):
#         pass
#
# e=Emirlan()
# e.run()
#
# print(e._age)
# e._age=11
# e._Emirlan__name='name'
# print(e._age)
# # print(e._Emirlan__name)
# e.__name='name'
# # print(dir(e))
# r='qwertyu'
# print(dir(e))





# инкапсуляция
# git clone

class Emirlan:
    head=1
    hands=2
    foots=2
    def __init__(self,name='Emirlan',age=18):
        self.__name=name
        self.__age=age
    def __str__(self):
        return f'{self.__name} ' \
               f'{self.__age}'

    @property
    def emirlan(self):
        return f'{self.__name} {self.__age}'
    @emirlan.setter
    def emirlan(self,name,age):
        self.__name=name
        self.__age=age

    def run(self):
        self.__run()
        self.__g()
        print(self.__age - 1)
        print(self.__name)


    def __run(self):
        print(self.__name, 'run')

    def __g(self):
        pass



e=Emirlan()
e.run()


e._age=11
e._Emirlan__name='name'
print(e._age)
# print(e._Emirlan__name)
e.__name='name'
# print(dir(e))
r='qwertyu'
# print(dir(e))


amir=Emirlan('Emirlan',0)

print(amir.emirlan)





# множественное наследование
from lesson3 import Emirlan
class O:...
class A(O):...
class B(O):...
class C(O):...
class D(O):...
class E(O):...

class K1(A,B,C):...
class K2(B,D):...
class K3(C,D,E):...


class Z(K1,K2,K3):...

# print(Z.mro())



class One:
    def __init__(self,name):
        self.name=name

class Tho():
    def __init__(self,age):
        self.age=age
    def f(self):
        print('Амир молчит')

class Tho2(One):
    def F(self):
        print('Амир говорит')


class Three(Tho2,Tho):
    # def __init__(self, name,age):
    #     Tho.__init__(self,age)
    #     Tho2.__init__(self,name)

    def __str__(self):
        return f'{self.name}'


c=Three('name')
print(c)



# 1 встроенный
# import math
# p=9
# print(math.sqrt(p))
# from math import pi as aldiyar
# print(math.pi)
# print(aldiyar)
#
# # 2 свои модули
# import lesson4
# from lesson4 import Emirlan
#
# a=Emirlan('Байэль',12)
# a.run()
# 3 взаимствованные чужие
import colorama

print(colorama.Fore.MAGENTA)
print("ghjk")
print(colorama.Style.BRIGHT)