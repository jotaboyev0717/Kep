from datetime import datetime
import re

text = input()
pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"
found_dates = re.findall(pattern, text)

if len(found_dates) >= 2:
    try:
        d1 = datetime.strptime(found_dates[0], "%d.%m.%Y")
        d2 = datetime.strptime(found_dates[1], "%d.%m.%Y")
        diff = abs((d2 - d1).days)
        print(diff)
    except ValueError:
        print(0)
else:
    print(0)