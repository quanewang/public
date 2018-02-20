"""
H-Tree Construction
An H-tree is a geometric shape that consists of a repeating pattern resembles the letter H.

It can be constructed by starting with a line segment of arbitrary length,
drawing two segments of the same length at right angles to the first through its
endpoints, and continuing in the same vein, reducing (dividing) the length of the line
segments drawn at each stage by .

Here are some examples of H-trees at different levels of depth:

alt depth = 1

alt depth = 2

alt depth = 3

Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth. Assume that the starting line is parallel to the X-axis.

Use the function drawLine provided to implement your algorithm. In a production code, a drawLine function would render a real line between two points. However, this is not a real production environment, so to make things easier, implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, assume that drawLine's time and space complexities are constant, i.e. O(1).
"""
def drawHTree(x, y, length, depth):
    drawHTree_(x, y, length, depth)

def drawHTree_(x, y, length, depth):
    print 'depth=', depth
    drawLine(x - length / 2, y, x + length / 2, y)
    drawLine(x - length / 2, y - length / 2, x - length / 2, y + length / 2)
    drawLine(x + length / 2, y - length / 2, x + length / 2, y + length / 2)
    if depth > 1:
        next_length = length / 2
        drawHTree_(x - length / 2, y - length / 2, next_length, depth - 1)
        drawHTree_(x - length / 2, y + length / 2, next_length, depth - 1)
        drawHTree_(x + length / 2, y - length / 2, next_length, depth - 1)
        drawHTree_(x + length / 2, y + length / 2, next_length, depth - 1)


def drawLine(x, y, x1, y1):
    print x, y, x1, y1


drawHTree(0, 0, 10, 3)
