# This will read from the convert.txt file
# Then make the conversion and write to converted.txt file

from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

if __name__ == '__main__':

    while True:
        file_convert = open('convert.txt', 'r')
        line = file_convert.readline()
        file_convert.close()

        if not line:
            continue

        else:
            file_convert = open('convert.txt', 'r')
            convert_tuple = ()

            # the first line will be the number of items to put back in the tuple
            number_elements = int(file_convert.readline())

            i = 0
            while i < number_elements:
                element = file_convert.readline()
                if (element != ''):
                    if i < 2:
                        element = element.replace('\n', '')
                        convert_tuple = convert_tuple + (str(element),)
                    else:
                        convert_tuple = convert_tuple + (float(element),)
                i += 1
        
            file_convert.close()

        # convert amount and write to converted.txt
            c = CurrencyRates()
            data = c.convert(convert_tuple[0], convert_tuple[1], convert_tuple[2])
            # round to two decimal places
            data = format(data, '.2f')

            file_converted = open('converted.txt', 'w')
            # print(data)
            file_converted.write(str(data))
            file_converted.close()

