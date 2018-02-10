# LESSON
#   -- wrong handling of global state cur_ts and cur_counter
#   -- while cursor<len(data) and ts == data[cursor][0]:
#        cursor += 1
#   -- max_ts = current_ts => max_ts = ts


# Busiest Time in The Mall
#
# Note that time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.
#
# Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.
#
# Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its time and space complexities.
#
# Example:
#
# input:  data = [ [1487799425, 14, 1],
#                  [1487799425, 4,  0],
#                  [1487799425, 2,  0],
#                  [1487800378, 10, 1],
#                  [1487801478, 18, 0],
#                  [1487801478, 18, 1],
#                  [1487901013, 1,  0],
#                  [1487901211, 7,  1],
#                  [1487901211, 7,  0] ]
#
# output: 1487800378 # since the increase in the number of people
#                    # in the mall is the highest at that point
#

def find_busiest_period(data):
    ts = None
    counter = None
    cur_ts = None
    cur_counter = 0
    for item in data:
        if not cur_ts:
            cur_ts = item[0]
            if item[2]:
                cur_counter = item[1]
            else:
                cur_counter = 0 - item[1]
            continue
        if item[0] != cur_ts:
            if cur_counter > counter:
                ts = cur_ts
                counter = cur_counter
            cur_ts = item[0]

        if item[2]:
            cur_counter = cur_counter + item[1]
        else:
            cur_counter = cur_counter - item[1]

    if cur_counter > counter:
        ts = cur_ts
        counter = cur_counter
    return ts


def find_busiest_period1(data):
    max = 0
    max_ts = 0
    current = 0
    cursor = 0
    while cursor<len(data):
        ts, current, cursor = process_ts(data, current, cursor)
        if ts:
            if current>max:
                max = current
                max_ts = ts
    return max_ts

def process_ts(data, current, cursor):
    if cursor>=len(data):
        return None, None, cursor
    ts = data[cursor][0]
    if data[cursor][2]:
      current += data[cursor][1]
    else:
      current -= data[cursor][1]
    cursor += 1
    while cursor<len(data) and ts == data[cursor][0]:
        if data[cursor][2]:
            current += data[cursor][1]
        else:
            current -= data[cursor][1]
        cursor += 1
    return ts, current, cursor

data1 = [ [1487799425, 14, 1]]
data2 = []
data = [[1487799425, 14, 1],
        [1487799425, 4, 0],
        [1487799425, 2, 0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 18, 1],
        [1487901013, 1, 0],
        [1487901211, 7, 0],
        [1487901211, 7, 1], ]

print find_busiest_period(data)

print find_busiest_period1(data)
