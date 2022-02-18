class Dessert:
    def __init__(self, name='def', calories=0):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name='def'):
            self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
            self._calories = calories

    def is_healthy(self):
        if isinstance(self._calories, (int, float)) and self._calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True

class  JellyBean(Dessert):
    def __init__(self,name='default',calories=0,flavor='usual'):
        super().__init__(name,calories)
        self._flavor=flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor
    def is_delicious(self):
        if self._flavor=="black licorice":
            return False
        else:
            return True

jelly=JellyBean("lollypop",123,3)
jelly.flavor="black licorice"
print(jelly.flavor)
jelly.name='chupa chups'
print(jelly.name)
jelly.calories=199.9
print(jelly.__dict__)
print(jelly.is_healthy())
print(jelly.is_delicious())