#Lesson 3 - Module and Package - datetime 套件
help("datetime")
'''
CLASSES
    builtins.object  (datetime是個python內建的套件)
        date
            datetime
        time
        timedelta
        tzinfo
            timezone
'''

'''
A. datetime.date:
class date(builtins.object)
     |  date(year, month, day) --> date object
     |   
因此datetime.date等於是在呼叫datetime這個套件中的date模組，他是一個class，其下有很多method


B. datetime.timedelta:
class timedelta(builtins.object)
     |  Difference between two datetime values.
因此datetime.timedelta等於是在呼叫datetime這個套件中的date模組，他是一個class，其下有很多method


C. datetime.date.isoformat:
	 |  
     |  isoformat(...)
     |      Return string in ISO 8601 format, YYYY-MM-DD.
     |  
datetime是套件，而date模組是一個class，其下有很多method，
isoformat()就是他其中一個method，所以datetime.date.isoformat等於是在呼叫套件中的模組中的isoformat()
'''
def print_next_day():
	import datetime
	today=datetime.date.today()
	TimeRange = datetime.timedelta(days=1)
	print(today + TimeRange)
	
print_next_day()
