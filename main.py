# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def test():
    print("Please give a time in the format HH:MM...")
    time = input()
    split_time = time.split(":")
    hour_angle_from_12 = (float(split_time[0]) % 12 + float(split_time[1]) / 60) / 12.0 * 360
    minute_angle_from_12 = float(split_time[1]) / 60 * 360
    angle_between_hour_and_minute = hour_angle_from_12 - minute_angle_from_12
    print("your time is..." + time)
    print("hour angle is... " + str(hour_angle_from_12))
    print("minute angle is..." + str(minute_angle_from_12))
    print("angle between them is..." + str(angle_between_hour_and_minute))
    # Todo: make this adjust the hour angle based on the minutes?
    
test()