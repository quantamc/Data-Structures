"""
Using a stack to chek whether or not a string 
has balanced usage of paranthesis.

Example
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}}}], [][]]] <- Not balanced


Balanced Example: {[]}

Non-Balanced Example: (()

Non-Balanced Example: ))
"""

from stack import Stack


def is_match(p1, p2):
    return(p1 + p2) in ["()", "[]", "{}"]
    
def is_paren_balanced(paren_string):
    s = Stack()
    l = Stack()
    is_balanced = True
    index = 0
    marker = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            if s.is_empty():
                marker = index + 1

            
            s.push(paren)
            
        else:
            if s.is_empty():
                marker = index + 1
                is_balanced = False
                continue
            else:
                top = s.pop()
               
                l.push(top)
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return marker


print(is_paren_balanced("[](()"))
