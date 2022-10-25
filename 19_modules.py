import collections
import time
import re
import sys

print(sys.path)

text = "mi numero de telefono es 311 123 121, el codigo de mi pais es 57, mi numero de la suerte es 3"
# ['311', '123', '121', '57', '3']
result = re.findall("[0-9]+", text)
print(result)

timestamp = time.time()
print(timestamp)


local = time.localtime()
time_local = time.asctime(local)
print(time_local)

numbers = [1, 2, 3, 2, 1, 2, 2, 3, 4, 5, 3, 21]
counter = collections.Counter(numbers)
print(counter)
