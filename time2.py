'''
script: cis131_assignment_Account_Class_Read_only
action: A class that stors a time in 12 hr format (hh:mm:ss) and allows each value to be changed or called individualy, while only using the seconds since midnight to represent the info
Date:   9/29/2025
'''


class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self._totalSeconds = hour*3600 + minute*60 + second #set totalSeconds to each one converted to seconds

    @property
    def hour(self):
        """Return the hour."""
        return self._totalSeconds // 3600   #integer divide by 3600 to convert seconds to hours

    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._remainingSeconds = self._totalSeconds % 3600      #the remainer is the remaining seconds
        self._totalSeconds = self._remainingSeconds+hour*3600   #set totalseconds to remainingSeconds + converted hours to seconds

    @property
    def minute(self):
        """Return the minute."""
        return (self._totalSeconds % 3600) // 60    #integer divide the remaining seconds by 60

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        
        self._remainingHours = (self._totalSeconds // 3600)*3600    #first give the remainning hours, then convert to seconds
        self._remainingSeconds = (self._totalSeconds % 3600) % 60   #first find the remaining seconds from hours, then find the remaining seconds from the minutes
        self._totalSeconds = self._remainingHours + self._remainingSeconds+ minute *60  #set totalSconds

    @property
    def second(self):
        """Return the second."""
        return (self._totalSeconds % 3600) % 60     #first find the remaining seconds from hours, then find the remaining seconds from the minutes

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')
        
        self._remainingHours = (self._totalSeconds // 3600)*3600            #first give the remainning hours, then convert to seconds
        self._remainingMinutes = ((self._totalSeconds % 3600) //60) * 60    #first give the remainning hours, then find the remaining minutes, then convert to seconds
        self._totalSeconds = self._remainingHours + self._remainingMinutes+ second  #set totalSeconds

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

