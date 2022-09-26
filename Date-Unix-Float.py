import datetime
from time import sleep

date_float = 0.0
date_article = "1970-01-02"
# while date_float < 1663958730.0:
#     date_float=(datetime.datetime.timestamp(
#         datetime.datetime.now(datetime.timezone.utc).astimezone()))
#     print("%.0f" % date_float)
#     #print(str(date_float).split('.')[0])
#     sleep(1)

date_float = datetime.datetime.timestamp(
    datetime.datetime.strptime(date_article, '%Y-%m-%d'))

print(date_float)
