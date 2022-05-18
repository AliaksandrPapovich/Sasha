import datetime
alltimes = input("Enter times in HH:MM\n").split()

for time in alltimes:
     hour, min = [int(i) for i in time.split(":")]
     print(hour, "hours and", min, "minutes")


