'''
script: cis131_lab_modifying_internal_data_representation
action: A class that stores a time in 12 hr format (hh:mm:ss) and allows each value to be changed or called individualy, while only using the seconds since midnight to represent and retain the info
Date:   9/29/2025
    Ammended 10/7/2025, added code to test the class
'''
from IPython import embed
class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self._total_seconds = hour*3600 + minute*60 + second #set total_seconds to the total seconds in hour, minute, second

    @property
    def hour(self):
        """Return the hour."""
        return self._total_seconds // 3600   #integer divide by 3600 to convert seconds to hours

    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._remainingSeconds = self._total_seconds % 3600      #the remainer is the remaining seconds
        self._total_seconds = self._remainingSeconds+hour*3600   #set total_seconds to remainingSeconds + converted hours to seconds

    @property
    def minute(self):
        """Return the minute."""
        return (self._total_seconds % 3600) // 60    #integer divide the remaining seconds by 60

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        
        self._remainingHours = (self._total_seconds // 3600)*3600    #first give the remainning hours, then convert to seconds
        self._remainingSeconds = (self._total_seconds % 3600) % 60   #first find the remaining seconds from hours, then find the remaining seconds from the minutes
        self._total_seconds = self._remainingHours + self._remainingSeconds+ minute *60  #set total_seconds

    @property
    def second(self):
        """Return the second."""
        return (self._total_seconds % 3600) % 60     #first find the remaining seconds from hours, then find the remaining seconds from the minutes

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')
        
        self._remainingHours = (self._total_seconds // 3600)*3600            #first give the remainning hours, then convert to seconds
        self._remainingMinutes = ((self._total_seconds % 3600) //60) * 60    #first give the remainning hours, then find the remaining minutes, then convert to seconds
        self._total_seconds = self._remainingHours + self._remainingMinutes+ second  #set total_seconds
    
    @property
    def total_seconds(self): 
        return self._total_seconds

    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""
        self.hour = hour        #call the hour property
        self.minute = minute    #call the minute property
        self.second = second    #call the second property

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' + 
                f'second={self.second})')

    def __str__(self):
        """Return Time string in 12-hour clock format."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) + 
                f':{self.minute:0>2}:{self.second:0>2}' + 
                (' AM' if self.hour < 12 else ' PM'))

# make a time object
t = Time(20,32,14)

# print time
print(f'The time is {t}')

# print the hour, minute, second
print(f'The hour is {t.hour}')
print(f'The minute is {t.minute}')
print(f'The second is {t.second}')
print(f'There are {t.total_seconds} seconds since midnight')
print('')

# change hour minute second individually
print(f'Changing the hours minutes and seconds individualy:')
t.hour = 3
t.minute = 4
t.second = 12
print(f'The new time is {t}')
print('')

# change time with set_time
print(f'Setting time by using set_time:')
t.set_time(4,7,39)
print(f'The newest time is {t}')
print('')

# attempt to enter an invalid number
try:
    print('Attempting to set the seconds above 60:')
    t.second = 345
except Exception as e:
    print(e)