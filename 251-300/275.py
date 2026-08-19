from datetime import datetime

a = input().strip()
date = datetime.strptime(a, "%d.%m.%Y")
print(date.isoweekday())