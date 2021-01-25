# This code calculates the number of times integers have appear in the file data_files/regex_sum_1148020.txt
import re

data_file = open('/mnt/c/Users/sveeramr/Desktop/WebScraper/data_files/regex_sum_1148020.txt')

# mini way
print(sum(int(num) for num in re.findall('[0-9]+', data_file.read())))

# other way
data_file.seek(0, 0)
sum_calc = ['0']
for line in data_file:
    line = line.rstrip()
    sum_calc = sum_calc + re.findall("[0-9]+", line)
sum_of_numbers = 0
for number in sum_calc:
    sum_of_numbers = sum_of_numbers + int(number)
print(sum_of_numbers)        
    
