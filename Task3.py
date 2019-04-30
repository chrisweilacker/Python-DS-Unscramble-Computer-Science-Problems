"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
numberList = []
numBangladoreFLCalled = 0

for call in calls:
  if call[0][0:5:]== "(080)":
    if call[1][0:5:] == "(080)": numBangladoreFLCalled += 1
      
    if call[1][0] == "(": numberList.append(call[1][1:call[1].find(')'):])
    if call[1][0:3:] == "140" : numberList.append("140")
    if call[1][5] == " ": numberList.append(call[1][0:4:])
    
#Remove Duplicates
codeSet = set(numberList)
#Convert back to List and Sort
sortedCodes = list(codeSet)
sortedCodes.sort()

#Print the codes
print("The numbers called by people in Bangalore have codes:")
for code in sortedCodes:
  print(code)

percentBFL = round( (numBangladoreFLCalled/len(numberList) ) * 100, 2)
print(f"{percentBFL} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

'''
I believe this code is O(6n + n log n) or approximately O(n).  It will go through and check each call if it was made from bangladore it would make 
4 calls.  THen we have conversion to a set and back to a list to be sorted. The sort algorithm is n log n on the worst case.
'''