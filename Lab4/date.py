#1 - substract 5 days from current date
import datetime
today = datetime.date.today()
print("Today is", today)
print("5 days ago it was", today - datetime.timedelta(days=5))


#2 - print yesterday, today, tomorrow
from datetime import timedelta, date
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#3 - drop microseconds from datetime
import datetime
x = datetime.datetime.now()
microban = x.replace(microsecond=0)
print("Before manipulations:", x)
print("After manipulations:", microban)
#alternative:
import datetime
x = datetime.datetime.now()
new_x = x - datetime.timedelta(microseconds=x.microsecond)
print(new_x)


#4 - date difference in seconds
import datetime
start_date = datetime.datetime.strptime(input('Enter Start date in the format y/m/d: '), '%Y/%m/%d')
end_date = datetime.datetime.strptime(input('Enter End date in the format y/m/d: '), '%Y/%m/%d')
diff = end_date - start_date
print("The difference between the dates in seconds:", diff.total_seconds())
