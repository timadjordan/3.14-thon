bill = input("Please input the price of your meal. $")
tax = .0625*bill
tip = .2*(bill+tax)
total = bill+tax+tip

print "Your tip is: $%s, and your total is: $%s." % (round(tip, 2), round(total, 2))

from datetime import datetime
diem=datetime.now()
year=diem.year
month=diem.month
day=diem.day
hour=diem.hour
minutes=diem.minute
morning="AM"
evening="PM"

if minutes<10:
	minutes="0"+str(minutes)
else:
	minutes=minutes

if hour>12:
	meridian="PM"
else:
	meridian="AM"

if hour>12:
	hour=hour-12
else:
	hour=hour


print "The current time is %s:%s %s and today's date is %s/%s/%s" % (hour, minutes, meridian, month, day, year)


make_me_true=5>3
print make_me_true