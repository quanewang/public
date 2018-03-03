"""
--LESSON
-- use stack

https://leetcode.com/problems/tag-validator/description/
"""

class Solution(object):
    def isValid(self, code):
        tag = self.extractTag(code)
        if not tag or len(tag)<3:
            return False
        end_tag = self.get_end_tag(tag)
        if code[len(code)-len(end_tag):]!=end_tag:
            return False
        low = len(tag)
        high = len(code) - len(end_tag) - 1
        stack = []
        while low<=high:
            if "<![CDATA["==code[low:low + len("<![CDATA[")]:
                low += len("<![CDATA[")
                while low<=high and code[low:low+len("]]>")]!="]]>":
                    low += 1
                if low>high:
                    return False
                low = low + len("]]>")
            elif code[low]=='<':
                tag = self.extractTag(code[low:])
                if not tag or len(tag)<3:
                    return False
                if self.is_end_tag(tag):
                    if not stack:
                        return False
                    elif stack[-1]==tag:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(self.get_end_tag(tag))
                low = low + len(tag)
            else:
                low = low + 1
        return not stack and low>=high

    def is_end_tag(self, tag):
        return tag[1]=='/'

    def get_end_tag(self, tag):
        return tag[:1] + '/' + tag[1:]

    def extractTag(self, code):
        if code[0]!='<' or code.find('>')<0:
            return None
        tag = code[:code.index('>')+1]
        if self.is_end_tag(tag):
            for x in tag[2:len(tag)-1]:
                if x < 'A' or x > 'Z':
                    return None
            if len(tag)>12:
                return None
        else:
            for x in tag[1:len(tag) - 1]:
                if x < 'A' or x > 'Z':
                    return None
            if len(tag)>11:
                return None
        return tag


s = Solution()
print s.isValid("<DIV><QUSQCBJ><![CDATA[ONHU]]></QUSQCBJ></DIV>")
