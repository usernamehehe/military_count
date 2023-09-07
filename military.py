from datetime import timedelta, date
import numpy as np

# 常備役only
date_entry = input("Enter the date in YYYY-MM-DD format: ")
year, month, day = map(int, date_entry.split("-"))
in_jail = date(year, month, day)
discount = int(input("Enter your discount days: "))
out_jail = in_jail + timedelta(days=111) - timedelta(days=discount)
# get weekdays
work_days = np.busday_count(in_jail, out_jail)

print("\n" + "You will be released on", out_jail)
print("You only have " + str(work_days) + " days in jail.")
