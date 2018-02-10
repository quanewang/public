'''
leecode
practive hard questions
45 minutes two questions
one hard question, two medium ones

system design session:
- scalability
- tinyurl

why do you want to work for fb
- the scale of the business
- technical read and conference videos

why do you leave cambia?
- like the work
- dislike the culture
-- locked office
-- nap in cubicle

why do you leave paypal
what is most challenging project
how would you do differently

give a conflict scenario and how do you resolve it
- conflicts with a peer
-- disagreement in design: event and db
-- manager sided with me
-- the lead is unhappy
-- had a conversation
---- nothing personal
---- pointed out his strength in clean coding and devop operation
---- we lack proper review and debate in the past
---- we can do great work together going forward


- manager kept being absent from daily standups

give a scenario you take initiative
(how do you work in a non-formatted environment)

'''

# Interview Questions
# Question 1: Given two ids and a function getFriends(id) to get the list of friends of
# that person id, write a function that returns the list of mutual friends

def get_mfriends(id1, id2):
    friends1 = get_friends(id1)
    friends2 = get_friends(id2)
    hash = {}
    result = []
    for f1 in friends1:
        hash[f] = 1
    for f2 in friends2:
        if f2 in hash:
            result.append(f2)
    return result

def get_friends(id):
    return [1, 2, 3, 4]

# Question 2: Given an id and a function getFriends(id) to get the list of friends of
# that person id, write a function that returns the list of friends of friends
# in the order of decreasing number of mutual friends, as in friend recommendations.

def get_friends_of_friends(id):
    friends = get_friends(id)
    pq = priority_queue
    for f in friends:
        f_friends = get_friends(f)
        for ff in f_friends:
            pq.add(len(get_mfriends(id, ff)), ff)


# Question 3: Given a number of time slots  start time and end time a b,
# find any specific time with the maximum number of overlapping. After solving
# the problem I had to prove my solution

def max_overlap(slots):
    START = 1
    END = -1
    count = 0
    start_time = 0
    end_time = 0
    events = priority_queue_by_time()
    id = 0
    for slot in slots:
        id +=1
        events.add([id, START, slot[0])
        events.add([id, END, slot[1])
    simulation = priority_queue_by_time()
    for event in events:
      if event[1] == START:
        simulation.add(event)
      else:
        if count<len(simulation):
          count = len(simulation)
          start_time = simulation.peek()
          end_time = event[2]
        simulation.remove(event[0])
    return count, start_time, end_time


# Question 4: Given an array of Integers, find the Longest sub-array whose elements are in Increasing Order

# Question 6: Given a Sorted Array which has been rotated, write the code to find a given Integer




