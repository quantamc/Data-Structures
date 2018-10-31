# python3

from collections import namedtuple
from stack import Stack

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    print(left, right)
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = Stack()

    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(next, i+1)
            opening_brackets_stack.push(bracket)
            print(opening_brackets_stack.get_stack())
            continue

        if next in ")]}":

            if opening_brackets_stack.is_empty():
                return i+1

            elif are_matching(opening_brackets_stack.pop().char, next):
                continue
            else:
                return i+1
    
    if not opening_brackets_stack.is_empty():

        return opening_brackets_stack.pop().position

 
def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    
    if mismatch == None:
        print("Success")

    else:
        print(mismatch)


if __name__ == "__main__":
    main()