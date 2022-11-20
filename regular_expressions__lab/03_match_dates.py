#     3. Match Dates
# Write a program, which matches a date in the format
# "dd{separator}MMM{separator}yyyy".
# Use capturing groups in your regular expression.
# [('13', '/', 'Jul', '1928'), ('10', '-', 'Nov', '1934'), ('25', '.', 'Dec', '1937')]


import re

pattern = r'\b(\d{2})(\.|-|\/)([A-Z][a-z]{2})\2(\d{4})\b'
input_line = input()
output_line = re.findall(pattern, input_line)

result = []
for i in range(len(output_line)):
    result.append(" ".join(output_line[i]))

for dates in result:
    day, separator, month, year = dates.split(" ")
    print(f"Day: {day}, Month: {month}, Year: {year}")

#
# import re
#
# pattern = r'\b(\d{2})(\.|-|\/)([A-Z][a-z]{2})\2(\d{4})\b'
# input_line = input()
# output_line = re.findall(pattern, input_line)
#
# result = []
#
# for dates in output_line:
#     day, separator, month, year = dates.groups()
#     result.append(f"Day: {day}, Month: {month}, Year: {year}")
#
# print(", ".join(result))
