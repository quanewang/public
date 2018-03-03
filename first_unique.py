"""

"""

def first_unique(text):
    if not text:
        return None
    h = {}
    for x in text:
        if x in h:
            h[x]=h[x]+1
        else:
            h[x]=1
    for x in text:
        if h[x]==1:
            return x
    return None

print first_unique("aaabc")