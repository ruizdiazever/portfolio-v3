import datetime, zoneinfo
hour = datetime.datetime(2022, 11, 5, 2, 11, 35, tzinfo=zoneinfo.ZoneInfo(key='GMT'))

print(hour.strftime("%Y/%m/%d"))
