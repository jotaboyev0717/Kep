from datetime import datetime

start = datetime(1, 1, 1)
now = datetime.now()

diff = now - start

print(int(diff.total_seconds()))