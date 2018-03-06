"""
--LESSON
--          progress.pop()
            return None
- progress<3 => len(progress)<3
- 010.1.0.0 => 10.1.0.0

https://leetcode.com/problems/restore-ip-addresses/description/
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        return restore(s, range(1, len(s)), [])

def restore(s, pos, progress):
    if not pos or len(progress)==3:
        ip = make_ip(s, progress)
        return [ip] if ip is not None else []
    if not progress:
        prev = 0
    else:
        prev = progress[-1]
    if pos[0] - prev < 4:
        result1 = restore(s, pos[1:], progress)
        progress.append(pos[0])
        result2 = restore(s, pos[1:], progress)
        progress.pop()
        return result1+result2
    else:
        return []

def make_ip(s, progress):
    if not s or len(s)<4 or len(progress)<3:
        return None
    prev=0
    ip=None
    progress.append(len(s))
    for x in progress:
        term = s[prev:x]
        if validate(term):
            if ip == None:
                ip = term
            else:
                ip = ip + '.' + term
        else:
            progress.pop()
            return None
        prev = x
    progress.pop()
    return ip

def validate(term):
    if int(term) >= 0 and int(term) <= 255:
        if term[0]=='0' and len(term)>1:
            return False
        return True
    return False

s = Solution()
print s.restoreIpAddresses("1111111111")
