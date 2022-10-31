# code from index will need to be added to some page of project

from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import time

c = CurrencyRates()

# sample calls
print(c.get_rate('USD', 'INR'))
print(c.convert('USD', 'INR', 10.50))

# app sends request in the form of a tuple as in ('USD', 'USR', 10)
# first element is FROM, second element is TO, and third element is AMOUNT

# sample for testing conversion
convert_from = 'USD'
convert_to = 'INR'
convert_amount = 10

my_tuple = (convert_from, convert_to, convert_amount)

# write what is to be converted to convert.txt
file_convert = open('convert.txt', 'w')
file_convert.write(str(len(my_tuple)) + '\n')

for item in my_tuple:
    file_convert.write(str(item) + '\n')
file_convert.close()

time.sleep(1.0)

# read converted amount from converted.txt and convert to int
file_converted = open('converted.txt', 'r')
new_amount = file_converted.readline()

new_amount = float(new_amount)
new_amount = format(new_amount, '.2f')   # limit to two decimal places
file_converted.close()

# test print
print(new_amount)