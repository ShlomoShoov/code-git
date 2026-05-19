# 7. Aliased import. Write a one-line program that imports datetime.datetime under the alias dt and
# prints the current date and time.

from datetime import datetime as dt

print(f'time and date now are: {dt.now()}' )