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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

input: calls and texts
output: sorted list of numbers that may be telemarketers
"""
setOfTelemarketers = set()
for call in calls:
    if call[0] not in setOfTelemarketers:
        isTelemarketer = True
        for acall in calls:
            if acall[1] == call[0]:
                isTelemarketer = False
                break

        if not isTelemarketer: continue

        for text in texts:
            if text[0] == call[0] or text[1] == call[0]:
                isTelemarketer = False
                break
    
    if isTelemarketer: setOfTelemarketers.add(call[0])

sortedListOfTelemarketers = list(setOfTelemarketers)
sortedListOfTelemarketers.sort()
print("These numbers could be telemarketers: ")
for tele in sortedListOfTelemarketers:
    print(tele)


"""
This algorithm would be O(2(n)^2 + n + n log n) which approximates to O(n^2) if we 
consider that going through the text list is the same as going through the calls list and the calls are our actual input
otherwise we would need multiple variables for input.
"""

