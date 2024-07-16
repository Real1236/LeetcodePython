# Q1: O-Week Scheduling
# It's O-Week and you're trying to get the maximum value out of your time at Western because you turned down your acceptances to MIT and Harvard for the "experience".

# Given an array of O-week events with their starting and ending times, return the maximum number of events that can be attended. An event must be fully attended from start to finish, and two events cannot be attended simultaneously. An event is simultaneous if and only if the times at which they run overlap.

# For example, if the input is:

# [ [1,5], [2,4], [4,6] ]

# The first event [1,5] and the second event [2,4] cannot both be attended because the second one starts (at time 2) before the first one finishes (at time 5). But, the second and third event CAN both be attended, because the third event starts (at time 4) at the exact moment when the second one ends (at time 4).

# The length of the input is less than or equal to 10^5.

# The starting and ending times are between 1 and 10^9, inclusive. For an event with starting and ending times [s, e], s < e. (the ending time is always later than the starting time).

# Example 1:
# Input: [ [1,3], [2,5], [3,9], [6,8] ]

# Output: 2

# Explanation: The first event [1,3] and the fourth event [6,8] are not overlapping and thus can both be attended. No other events can be attended. It can be shown that the maximum number of events that can be attended is 2.

# Note that [2,5] and [6,8] is equally valid, but still attends at most 2 events.

def maxEvents(events):
    # Sort the events by their ending times
    events.sort(key=lambda x: x[1])
    
    # Initialize the end time of the last attended event as 0
    last_attended_time = 0
    
    # Initialize the count of attended events as 0
    count = 0
    
    # Iterate over the sorted events
    for event in events:
        # If the start time of the current event is later than the end time of the last attended event
        if event[0] > last_attended_time:
            # Attend the current event
            last_attended_time = event[1]
            count += 1
            
    return count

events = [[1,3], [2,5], [3,9], [6,8]]
print(maxEvents(events))

events = [[1,2], [2,3], [3,4], [4,5]]
print(maxEvents(events))

events = [[1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8], [8,9], [9,10], [10,11]]
print(maxEvents(events))

# The solution works by sorting the events based on their ending times and then iteratively selecting the event that ends the earliest and does not overlap with the previously selected one. This approach has a time complexity of O(nlogn) due to sorting, and a space complexity of O(n) for storing the events.