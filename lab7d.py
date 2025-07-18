#!/usr/bin/env python3
# Student ID: lbudhathoki

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, format_time, time_to_sec,
                            change_time, sum_times, valid_time
    """

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Allows print(t1) to display formatted time"""
        return self.format_time()

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        """Convert the time object to seconds since midnight"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def change_time(self, seconds):
        """Modify the time object by adding seconds (in place)"""
        total_seconds = (self.time_to_sec() + seconds) % 86400
        updated = sec_to_time(total_seconds)
        self.hour = updated.hour
        self.minute = updated.minute
        self.second = updated.second
        return None

    def sum_times(self, t2):
        """Add another time object and return the sum as a new Time object"""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def valid_time(self):
        """Check if the time attributes are valid"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True

def sec_to_time(seconds):
    """Convert seconds since midnight to a Time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

