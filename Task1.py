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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
input: list of calls
output: number of numbers
"""
setOfNumbers = set()
for call in calls:
    setOfNumbers.add(call[0])
    setOfNumbers.add(call[1])

for text in texts:
    setOfNumbers.add(text[0])
    setOfNumbers.add(text[1])

print(f"There are {len(setOfNumbers)} different telephone numbers in the records.") 

'''
This algorithm worst case time seems to be O(2n + 1) which approximates to O(n) as it only must make two calls per item in the calls list.
'''