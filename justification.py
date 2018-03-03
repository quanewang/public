"""
--LESSON
-- ((L - length) // (line[1] - line[0])) divided by ZERO
-- [''], 2
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""
INF = float('inf')
def text(words, L):
    cost = [INF]*len(words)
    parent = [0]*len(words)
    for i in range(0, len(words)):
        for j in range(i, -1, -1):
            est = estimate(words[j:i + 1], L)
            if est==INF:
                break
            old_cost = cost[i]
            if j==0:
                cost[i] = min(cost[i], est)
            else:
                cost[i] = min(cost[i], cost[j-1] + est)
            if old_cost != cost[i]:
                parent[i] = j
    return render(words, parent, L)

def estimate(words, L):
    length = sum([len(w) for w in words])
    if length+len(words)-1>L:
        return INF
    return pow(L - length, 3)

def render(words, parent, L):
    print words, parent
    i=len(words)-1
    lines=[]
    while i>=0:
        lines.insert(0, (parent[i], i))
        i = parent[i]-1
    result = []
    for line in lines:
        output=''
        length = sum([len(words[i]) for i in range(line[0], line[1]+1)])
        space = ' ' * (L - length)
        extra = 0
        if line[1]-line[0]:
            space = ' ' * ((L - length) // (line[1] - line[0]))
            extra = (L - length) % (line[1] - line[0])

        for i in range(line[0], line[1]+1):
            output+=words[i]
            if i!=line[1] or line[0]==line[1]:
                output += space
                if extra:
                    output+=' '
                    extra -= 1
        result.append(output)
    return result

print text(["This", "is", "an", "example", "of", "text", "justification."], 16)
print text([""], 16)



