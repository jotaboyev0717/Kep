from datetime import datetime, timedelta

today = datetime.now()
future_date = today + timedelta(days=100)
print(future_date.strftime("%d-%m-%Y %H:%M:%S"))