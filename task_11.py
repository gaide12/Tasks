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
        if isinstance(self._calories,(int,float)) and self._calories<200:
            return True
        else:
            return False

    def is_delicious(self):
        return True
jelly=Dessert("Apple_Bean","2")
#print(jelly.is_healthy())