class Dessert:
    @classmethod
    def calories_invalid(cls,calories):
        if not isinstance(calories, int):
            raise TypeError('"calories" должен быть int')

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
        if not self.calories_invalid(self.calories):
            return self.calories < 200

    def is_delicious(self):
        return True
jelly=Dessert("Apple_Bean","2")
#print(jelly.is_healthy())