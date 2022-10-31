# CS361_CurrencyConversion

Documentation included in files as well.

HOW TO REQUEST DATA:

NOTE-- run the file converter.py first so that it is ready to receive data
in terminal: python converter.py

Code contained in index.py will need to be added to the page from which you want your currency converted. There are sample calls to show how data will
be written to a text and requested from converter.py. Data will be requested in the form of a tuple with the first element (string) indicating FROM which currency,
the second element (string) indicating TO which currency, and the third element (float) indicating the AMOUNT to be converted. 

example: convert_tuple = ('USD', 'INR', 10.50)

This will be written to convert.txt with each element written to a new line.

converter.py will then read this data from convert.txt and turn it back into the form of our original tuple. converter.py will make appropriate conversions
and then write the converted value to converted.txt. With our example of convert_tuple = ('USD', 'INR', 10.50), converter.py will write 865.835845643654
to converted.txt in the form of a string.


HOW TO RECEIVE DATA:

After following the steps above, the converted.txt file willl contain the string 865.835845643654. In order to receive this, index.py contains code to open the
converted.txt file and convert the string to a float, rounding to two decimal places. Resulting float will be stored in variable new_amount. The converted.txt 
file will then be closed. At this point, the resulting float may be inserted wherever necessary. 
