"""
--LESSON
--- [b[0], a[1]]=>[b[0], min(a[1], b[1])]
--- i += 1 => j += 1
--- [max(a[0], b[0]), min(a[1], b[1])]

Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return null.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each persons availability is represented by an array of pairs. Each pair is an epoch array of size two.
The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot.
The input variable dur is a positive integer that represents the duration of a meeting in seconds.
The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a persons availability are disjointed,
i.e, time slots in a persons availability dont overlap. Further assume that the slots are sorted by slots start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: null # since there is no common slot whose duration is 12
"""

def meeting_planner(slotsA, slotsB, dur):
  i , j = 0, 0
  while i<len(slotsA) and j<len(slotsB):
    slot = find_common(slotsA[i], slotsB[j])
    if slot and slot[1]-slot[0]>=dur:
      return [slot[0], slot[0]+dur]
    elif slotsA[i][1]==slotsB[j][1]:
      i += 1
      j += 1
    elif slotsA[i][1]>slotsB[j][1]:
      j += 1
    else:
      i += 1
  return []

def find_common(a, b):
  return [max(a[0], b[0]), min(a[1], b[1])]

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 12
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print meeting_planner(slotsA, slotsB, dur)