from datetime import datetime
import locale

# locale.setlocale(locale.LC_ALL, '')
print(locale.setlocale(locale.LC_ALL, 'tr_TR'))

# print(*dir(datetime), sep='\n')

# get now

date_now = datetime.now()

print(date_now)

year = date_now.year
month = date_now.month
day = date_now.day
hour = date_now.hour
minute = date_now.minute
second = date_now.second
microsecond = date_now.microsecond

print(*[year, month, day, hour, minute, second, microsecond], sep='\n')

## ctime()

print('________ctime()________')

ct = datetime.ctime(date_now)
print(ct)


## strftime()

# Yıl bilgisini almak için : %Y
#
# Ay ismini almak için : %B
#
# Gün ismini almak için : %A
#
# Saat bilgisini almak için : %X
#
# Gün bilgisini almak için : %D

print('________strftime()________')
strf = datetime.strftime(date_now, '%X %A -- %B ___%Y ')
print(strf)

# https://docs.python.org/2/library/time.html


print('________timestamp()__fromtimestamp()________')

## timestamp() and fromtimestamp()

second = datetime.timestamp(date_now)
print(second)

date_obj = datetime.fromtimestamp(second)
print(date_obj)

BC = datetime.fromtimestamp(0)
print(BC)


## iki tarih arasindaki farki bulmak

print('________different two date________')

future_date = datetime(2023,9,7)
now = datetime.now()

diff = future_date - now
print(diff)
print(diff.days, 'gun kalmis')
