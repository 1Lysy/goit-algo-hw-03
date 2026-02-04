fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(2)
second = fh.read(3)
fh.write(second)
print(second)  # 'e'

fh.close()
