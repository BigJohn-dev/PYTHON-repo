
class TimeWithProperties:
    def __init__(self, second=0, minute=0, hour=0):
        self.second = second
        self.minute = minute
        self.hour = hour

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if 0 > value > 60:
            raise ValueError("Seconds must be between 0 and 59")
        self._second = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if 0 > value > 60:
            raise ValueError("Minute must be between 0 and 59")
        self._minute = value

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if 0 > value > 23:
            raise ValueError("Hours must be between 0 and 23")
        self._hour = value

    def __str__(self):
        return f'Time({self.hour:02}:{self.minute:02}:{self.second:02})'

time1 = TimeWithProperties()
time1.hour = 12
print(time1)

file_path = r"C:\Users\Dell\OneDrive\Documents\Python Works\Class tasks\time_property.py"