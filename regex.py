'''
LESSSON
-- (.*, bc) => false
-- (.*, cc) => false
-- ("", a*)
-- no a*a
'''

def is_match1(text, pattern):
    stack = []
    for c in pattern:
        stack.append(c)
    pos = len(text)-1
    while len(stack)>0:
        p = stack.pop()
        if p == '*':
            p = stack.pop()
            if p=='.' and pos>=0:
                p = text[pos]
            while pos>=0 and match(p, text[pos]):
                pos -= 1
        elif pos>=0 and match(p, text[pos]):
            pos -= 1
        else:
            return False
    return len(stack)==0 and pos<0


def match(p, c):
    return p==c

def is_match(text, pattern):
    ti = 0
    pi = 0
    while pi<len(pattern):
        if is_star(pi, pattern):
            p = pattern[pi]
            if pattern[pi]=='.':
                if ti<len(text):
                    p = text[ti]
            while ti<len(text) and match(p, text[ti]):
                ti += 1
            pi += 2
        elif ti<len(text) and is_dot(pi, pattern):
            pi += 1
            ti += 1
        elif ti<len(text) and match(pattern[pi], text[ti]):
            pi += 1
            ti += 1
        else:
            return False
    return pi>=len(pattern) and ti>=len(text)

def is_star(pi, pattern):
    return pi<len(pattern)-1 and pattern[pi+1]=='*'

def is_dot(pi, pattern):
    return pi<len(pattern) and pattern[pi]=='.'

print is_match("a", ".")
print is_match("abbbca", "ab*c.c*")
print is_match("", "c*")
print is_match("aa", ".*")
print is_match("abaa", "a.*a*")