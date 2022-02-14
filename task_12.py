class Dessert:
    @classmethod
    def name_invalid(cls,name):
        if not isinstance(name, str):
            raise TypeError('"name" должен быть string')

    @classmethod
    def calories_invalid(cls,calories):
        if not isinstance(calories, int):
            raise TypeError('"calories" должен быть int')

    def __init__(self, name, calories):
        self.name = 'def'
        self.calories=0
        if not self.name_invalid(name) and not self.calories_invalid(calories):
            self._name = name
            self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name='def'):
        if not self.name_invalid(name):
            self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        if not self.calories_invalid(calories):
            self._calories = calories

    def is_healthy(self):
        return self.calories < 200

    def is_delicious(self):
        return True

class  JellyBean(Dessert):
    @classmethod
    def flavor_invalid(cls, flavor):
        if not isinstance(flavor, str):
            raise TypeError('"flavor" должен быть str')

    def __init__(self,name='default',calories=0,flavor='usual'):
       if not self.flavor_invalid(flavor):
        super().__init__(name,calories)
        self._flavor=flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
     if not self.flavor_invalid(flavor):
        self._flavor = flavor
    def is_delicious(self):
        if self._flavor=="black licorice":
            return False
        else:
            return True

jelly=JellyBean()
jelly.name='123'
print(jelly.name)