class Dessert_descrypt:
    def __set_name__(self, owner, name):
        self.name='_'+name
    def __get__(self, instance, owner):
        return getattr(instance,self.name)
    def __set__(self, instance, value):
        return setattr(instance,self.name, value)

class Dessert:
    name=Dessert_descrypt()
    calories=Dessert_descrypt()
    def __init__(self,name="default_name",calories=0):
        self.name=name
        self.calories=calories
    def is_healthy(self):
        return self.calories<200
    def is_delicious(self):
        return True
ex1=Dessert()
ex1.name='Ice_cream'
print(ex1.name)
