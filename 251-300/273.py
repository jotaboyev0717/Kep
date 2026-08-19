a = input()
data = a.split(':')
if int(data[0]) < 12:
    print('A.M.')
else:
    print('P.M.')