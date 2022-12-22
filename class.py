class Hero:
    def __init__(self,name='tor',abyliti='force'):
        self.abyliti=abyliti
        self.name=name



class Hero1(Hero):

    def __str__(self):
        return f'{self.name}'
    def hero3(self):
        print(f'it is super_hero')


c=Hero1('tor')
c.hero3()
print(c)


