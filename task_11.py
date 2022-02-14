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
        if self.name_invalid(name):
            self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        if self.calories_invalid(calories):
            self._calories = calories

    def is_healthy(self):
        return self.calories < 200

    def is_delicious(self):
        return True
jelly=Dessert("Apple_Bean",201)
print(jelly.is_healthy())