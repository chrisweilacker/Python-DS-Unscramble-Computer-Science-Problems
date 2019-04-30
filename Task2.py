"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""



def findMostTimeSpent(callList):
    callTimes = {}
    if len(callList) == 0: return []
    longestCallTimes =  ['' , 0]
    for call in callList:
        callTimes[call[0]] = callTimes[call[0]] + int(call[3]) if call[0] in callTimes else int(call[3])
        callTimes[call[1]] = callTimes[call[0]] + int(call[3]) if call[1] in callTimes else int(call[3])
        if callTimes[call[0]] > longestCallTimes[1]: longestCallTimes = [call[0], callTimes[call[0]]]
        if callTimes[call[1]] > longestCallTimes[1]: longestCallTimes = [call[1], callTimes[call[1]]]  
    return longestCallTimes

    
longestCaller = findMostTimeSpent(calls)
print(f"{longestCaller[0]} spent the longest time, {longestCaller[1]} seconds, on the phone during September 2016.")

'''
This algorithm worst case time is O(4n) or approximately O(n) as it must go through each individual call to 
pull out the time and update the calls to find the greatest.
'''