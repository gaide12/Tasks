class Dessert_descrypt:
    def __set_name__(self, owner, name):
        self.name='_'+name
    def __get__(self, instance, owner):
        return getattr(instance,self.name)
    def __set__(self, instance, value="default"):
        return setattr(instance,self.name, value)

class Dessert:
    name=Dessert_descrypt()
    calories=Dessert_descrypt()
    def __init__(self,name='default',calories=0):
        self.name=name
        self.calories=calories
    def is_healthy(self):
        return self.calories<200
    def is_delicious(self):
        return True

class  JellyBean(Dessert):
    flavor=Dessert_descrypt()
    def __init__(self,name='default',calories=0,flavor='usual'):
        super().__init__(name,calories)
        self.flavor=flavor
    def is_delicious(self):
        if self.flavor=="black licorice":
            return False
        else:
            return True
jelly=JellyBean("Apple_Bean",10,'black licorice')
jelly.flavor='apple'
print(jelly.is_delicious())