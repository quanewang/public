"""
-LESSON
-- if min_req is not None => if min_req is not None
-- prev = x[2]

Drone Flight Planner
Youre an engineer at a disruptive drone delivery startup and your
CTO asks you to come up with an efficient algorithm that calculates
the minimum amount of energy required for the companys drone to
complete its flight. You know that the drone burns 1 kWh
(kilowatt-hour is an energy unit) for every mile it ascends,
and it gains 1 kWh for every mile it descends. Flying sideways
neither burns nor adds any energy.

Given an array route of 3D points, implement a function calcDroneMinEnergy
that computes and returns the minimal amount of energy the drone would
need to complete its route. Assume that the drone starts its flight at
the first point in route. That is, no energy was expended to place the
drone at the starting point.

For simplicity, every 3D point will be represented as an integer array
whose length is 3. Also, the values at indexes 0, 1, and 2 represent
the x, y and z coordinates in a 3D point, respectively.

Explain your solution and analyze its time and space complexities.

Example:

input:  route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

output: 5 # less than 5 kWh and the drone would crash before the finish
          # line. More than 5 kWh and itd end up with excess energy

"""

def calc_drone_min_energy(route):
    if not route or len(route)==1:
        return 0
    return max(0, -1 * plan(route[1:-1], route[0], route[1], []))

def plan(route, s, e, p):
    if not route:
        return compute(s, e, p)
    min_req = None
    for i in range(0, len(route)):
        p.append(route[i])
        cost = plan(route[0:i] + route[i+1:], s, e, p)
        min_req = min(min_req, cost) if min_req is not None else cost
        p.pop()
    return min_req

def compute(s, e, p):
    p.append(e)
    energy = 0
    req = 0
    prev=s[2]
    for x in p:
        energy += prev - x[2]
        req = min(energy, req)
        prev = x[2]
    p.pop()
    print p, req
    return req

print calc_drone_min_energy([[0,2,2],[3,5,38],[9,20,6],[10,12,15],[10,10,8]])