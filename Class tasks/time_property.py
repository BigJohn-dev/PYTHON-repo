
class TimeWithProperties:

    def __int__(self, hour, minute, second):
        self.second = second
        self.minute = minute
        self.hour = hour

    @property
    def second(self):
        return self.second

    @second.setter
    def second(self, value):
        if value < 0 or value > 60:
            raise ValueError("Value must be between 0 and 60")
        self.second = value

