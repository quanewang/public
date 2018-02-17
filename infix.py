"""
--LESSON
- udpate method returns
- return stmt[idx], idx => return stmt[idx], idx, None

Prefix to Infix Conversion
4
Infix : An expression is called the Infix expression if the operator appears in between the operands in the expression. Simply of the form (operand1 operator operand2).
Example : (A+B) * (C-D)

Prefix : An expression is called the prefix expression if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2).
Example : *+AB-CD (Infix : (A+B) * (C-D) )
"""

def prefix_to_infix(stmt):
    text, idx, op = expr(stmt, 0)
    print text

def expr(stmt, idx):
    if not stmt or idx>=len(stmt):
        return '', idx
    if stmt[idx] in ['*', '+', '-']:
        text1, idx1, op1 = expr(stmt, idx+1)
        text2, idx2, op2 = expr(stmt, idx1+1)
        text1 = ('(' + text1 + ')') if op1 and stmt[idx]<op1 else text1
        text2 = ('(' + text2 + ')') if op2 and stmt[idx]<op2 else text2
        return text1 + stmt[idx] + text2, idx2, stmt[idx]
    else:
        return stmt[idx], idx, None


prefix_to_infix('*+AB-CD')